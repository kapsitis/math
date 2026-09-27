"""
Cut figures out of the page PNGs produced by pdf_ocr.py and save them under the
names used by the image placeholders in content_<lang>.md.

Usage:
    python extract_figures.py <parent_dir> <pdf_name> <config.yaml> [options]

    Same arguments as pdf_ocr.py. The output directory of pdf_ocr.py (e.g.
    sources/EE_PK/ee-pk-2006test/) must already contain the page PNGs of the
    problem and solution sources and content_<lang>.md of the language given by
    "figures: language". Settings are read from the "figures" key.

Options:
    --out DIR     output directory of pdf_ocr.py (default: config "output_dir")
    --dry-run     do not write figure PNGs; only the report and previews
    --no-llm      never call the cloud service (local heuristics only)
    --force       overwrite figure PNGs that already exist

How figures are found (all locally, from the PDF vector data):
  * Candidate figures are clusters of vector drawings (lines, curves, filled
    shapes) and embedded raster images, joined when closer than "gap" points and
    extended by the short text labels next to them (A, B, 114°, x, ...).
  * Problem statements: every candidate on the problem pages of a language is
    assigned to the problem whose number marker (e.g. "6." at the left margin,
    optionally in a given font) precedes it. If a problem has as many candidates as placeholders
    ![](...) before its <small> section, they are matched in reading order.
  * Solutions: placeholders after <small> are matched via the figure captions
    ("Joonis N", "rys. N") in the solution pages (the figure directly above the caption); the
    caption number is taken from the Markdown text of the solution.
  * Otherwise (count mismatch, no caption number) the cloud model gets the page
    image with numbered candidate boxes and picks the boxes (or gives its own
    bounding box). Without a model the largest candidates are used.
Every page with candidates gets a preview in figure_previews/ (red: candidates,
green: saved figures), and figures_report.txt lists where each figure came from.
"""
import argparse
import json
import os
import pathlib
import re
import sys

import yaml
from PIL import Image, ImageDraw, ImageOps

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from pdf_ocr import (Job, OpenAIClient, fill, problem_pages, solution_pages,  # noqa: E402
                     strip_fences)

PLACEHOLDER = re.compile(r"!\[[^\]]*\]\(([^)\s]+\.png)\)")


# ---------------------------------------------------------------- geometry helpers

def touches(a, b, margin=0.0) -> bool:
    """True if rectangles a and b (possibly degenerate lines) are within margin of each other."""
    return (a[0] - margin <= b[2] and b[0] - margin <= a[2] and
            a[1] - margin <= b[3] and b[1] - margin <= a[3])


def union(rects):
    return (min(r[0] for r in rects), min(r[1] for r in rects),
            max(r[2] for r in rects), max(r[3] for r in rects))


def reading_order(figs):
    """Sort figures in rows (vertically overlapping figures form a row), left to right."""
    figs = sorted(figs, key=lambda f: f.rect[1])
    rows = []
    for f in figs:
        for row in rows:
            r = union([g.rect for g in row])
            overlap = min(r[3], f.rect[3]) - max(r[1], f.rect[1])
            if overlap > 0.3 * min(r[3] - r[1], f.rect[3] - f.rect[1]):
                row.append(f)
                break
        else:
            rows.append([f])
    return [f for row in rows for f in sorted(row, key=lambda g: g.rect[0])]


def cluster(rects, margin):
    """Union-find clustering of rectangles closer than margin; returns lists of indices."""
    parent = list(range(len(rects)))

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    for i in range(len(rects)):
        for j in range(i + 1, len(rects)):
            if touches(rects[i], rects[j], margin):
                parent[find(i)] = find(j)
    groups = {}
    for i in range(len(rects)):
        groups.setdefault(find(i), []).append(i)
    return list(groups.values())


class PageRef:
    """A page of one of the job's sources (problems and solutions may be different PDFs)."""

    def __init__(self, src, no):
        self.src, self.no = src, no

    def key(self):
        return (self.src.name, self.no)

    def __eq__(self, other):
        return self.key() == other.key()

    def __hash__(self):
        return hash(self.key())

    def __lt__(self, other):
        return self.key() < other.key()

    def __str__(self):
        return f"{self.src.stem} p.{self.no}"


class Figure:
    def __init__(self, page, rect, items):
        self.page = page      # PageRef
        self.rect = rect      # (x0, y0, x1, y1) in PDF points
        self.items = items    # number of drawings/images it consists of
        self.id = None        # candidate number shown in previews and to the LLM

    @property
    def area(self):
        return (self.rect[2] - self.rect[0]) * (self.rect[3] - self.rect[1])


# ---------------------------------------------------------------- page analysis

class PageAnalyzer:
    def __init__(self, src, fcfg: dict):
        self.src = src
        self.doc = src.doc
        self.renderer = src.renderer
        self.c = fcfg.get("cluster", {})
        self.m = fcfg.get("marker", {})
        self.caption_rx = re.compile(fcfg.get("caption_regex", r"^\s*Joonis\s+(\d+)\s*$"))
        self._cache = {}

    def spans(self, page_no):
        page = self.doc[page_no - 1]
        return [(tuple(s["bbox"]), s["text"], s["font"])
                for b in page.get_text("dict")["blocks"] for l in b.get("lines", []) for s in l["spans"]
                if s["text"].strip()]

    def lines(self, page_no):
        page = self.doc[page_no - 1]
        return [(tuple(l["bbox"]), "".join(s["text"] for s in l["spans"]))
                for b in page.get_text("dict")["blocks"] for l in b.get("lines", [])
                if "".join(s["text"] for s in l["spans"]).strip()]

    def markers(self, page_no):
        """Problem number markers as (y, number)."""
        rx = re.compile(self.m.get("regex", r"^\s*(\d{1,2})\.\s*$"))
        font_rx = re.compile(self.m.get("font_regex", "."))
        max_x = self.m.get("max_x", 60)
        clip = self.renderer.clip_rect(page_no)
        out = []
        for bbox, text, font in self.spans(page_no):
            mm = rx.match(text)
            if mm and font_rx.search(font) and bbox[0] <= max_x and bbox[1] >= clip.y0:
                out.append((bbox[1], int(mm.group(1))))
        return sorted(out)

    def captions(self, page_no):
        """Figure captions as (bbox, number); whole lines, as "rys." and "1" may be separate spans."""
        out = []
        for bbox, text in self.lines(page_no):
            mm = self.caption_rx.match(text)
            if mm:
                out.append((bbox, int(mm.group(1))))
        return out

    def figures(self, page_no):
        if page_no in self._cache:
            return self._cache[page_no]
        c = self.c
        page = self.doc[page_no - 1]
        clip = tuple(self.renderer.clip_rect(page_no))

        rects = [tuple(d["rect"]) for d in page.get_drawings()]
        rects = [r for r in rects if touches(r, clip)]
        groups = cluster(rects, c.get("gap", 6))
        figs = []
        for g in groups:
            r = union([rects[i] for i in g])
            w, h = r[2] - r[0], r[3] - r[1]
            if w < c.get("min_width", 0):      # e.g. a column of empty answer boxes
                continue
            # fraction bars, overlines, underlines etc. are single thin strokes
            if (w >= c.get("min_size", 10) and h >= c.get("min_size", 10)) or \
               (len(g) >= c.get("min_items", 4) and max(w, h) >= c.get("min_long", 40)):
                figs.append(Figure(PageRef(self.src, page_no), r, len(g)))
        for info in page.get_image_info():
            r = tuple(info["bbox"])
            if min(r[2] - r[0], r[3] - r[1]) >= c.get("min_image_side", 8) and touches(r, clip):
                figs.append(Figure(PageRef(self.src, page_no), r, 1))

        # attach short text labels (point names, angles, axis labels). Whole text
        # lines are used, so that math symbols inside a sentence next to the
        # figure are not mistaken for labels.
        ignore = re.compile(c.get("ignore_text_regex", r"^[\s.…]+$"))
        marker_rx = re.compile(self.m.get("regex", r"^\s*(\d{1,2})\.\s*$"))
        labels = [bbox for bbox, text in self.lines(page_no)
                  if bbox[2] - bbox[0] <= c.get("label_max_width", 45)
                  and not ignore.match(text) and not self.caption_rx.match(text)
                  and not (marker_rx.match(text) and bbox[0] <= self.m.get("max_x", 60))]
        for f in figs:
            near = [l for l in labels if touches(f.rect, l, c.get("label_margin", 8))]
            if near:
                f.rect = union([f.rect] + near)
        # labels may have made figures overlap: merge them
        merged = []
        for g in cluster([f.rect for f in figs], 0):
            merged.append(Figure(PageRef(self.src, page_no), union([figs[i].rect for i in g]),
                                 sum(figs[i].items for i in g)))
        # keep only the part inside the rendered page area
        for f in merged:
            f.rect = (max(f.rect[0], clip[0]), max(f.rect[1], clip[1]),
                      min(f.rect[2], clip[2]), min(f.rect[3], clip[3]))
        self._cache[page_no] = merged
        return merged


# ---------------------------------------------------------------- markdown

def parse_placeholders(md: str) -> dict:
    """problem id -> {"problem": [names], "solution": [names], "problem_text": str, "solution_text": str}"""
    result = {}
    for block in re.split(r"(?m)^# <lo-sample/>\s*", md)[1:]:
        pid, _, body = block.partition("\n")
        cut = body.find("<small>")
        prob, sol = (body[:cut], body[cut:]) if cut >= 0 else (body, "")
        result[pid.strip()] = dict(problem=PLACEHOLDER.findall(prob), solution=PLACEHOLDER.findall(sol),
                                   problem_text=prob.strip(), solution_text=sol.strip())
    return result


def caption_numbers(solution_text: str, names: list, rx: re.Pattern) -> dict:
    """Guess the caption number ("Joonis N", "rys. N") for every solution placeholder.

    A caption line right after the placeholder wins; otherwise the numbers
    mentioned in the text are used in order of their first mention.
    """
    out = {}
    positions = [solution_text.find(f"({n})") for n in names] + [len(solution_text)]
    for i, n in enumerate(names):
        after = solution_text[positions[i]:positions[i + 1]].split(")", 1)[-1]
        first_line = after.strip().split("\n", 1)[0]
        mm = rx.fullmatch(first_line.strip())                           # caption line
        if mm:
            out[n] = int(mm.group(1))
    rest = [n for n in names if n not in out]
    mentioned = []
    for mm in rx.finditer(solution_text):
        num = int(mm.group(1))
        if num not in mentioned and num not in out.values():
            mentioned.append(num)
    if rest and len(mentioned) == len(rest):
        out.update(zip(rest, mentioned))
    elif rest:
        for i, n in enumerate(names):
            if n in rest:
                mm = rx.search(solution_text, positions[i], positions[i + 1])
                if mm:
                    out[n] = int(mm.group(1))
    return out


# ---------------------------------------------------------------- images

class PageImages:
    """Maps PDF coordinates of a page to its PNG rendered by pdf_ocr.py."""

    @staticmethod
    def path(pg: PageRef):
        path = pg.src.png_path(pg.no)
        if not path.exists():
            raise FileNotFoundError(f"page PNG {path} not found (run pdf_ocr.py first)")
        return path

    @staticmethod
    def to_px(pg: PageRef, rect, img, pad=0.0):
        clip = pg.src.renderer.clip_rect(pg.no)
        s = img.width / clip.width
        box = ((rect[0] - pad - clip.x0) * s, (rect[1] - pad - clip.y0) * s,
               (rect[2] + pad - clip.x0) * s, (rect[3] + pad - clip.y0) * s)
        return (max(0, int(box[0])), max(0, int(box[1])),
                min(img.width, int(box[2] + 1)), min(img.height, int(box[3] + 1)))


def trim_white(img, threshold=245):
    """Crop away white borders (used for boxes suggested by the model)."""
    mask = ImageOps.invert(img.convert("L")).point(lambda v: 255 if v > 255 - threshold else 0)
    bbox = mask.getbbox()
    return img.crop(bbox) if bbox else img


def overlay(images: PageImages, pg: PageRef, figs, saved=()):
    img = Image.open(images.path(pg)).convert("RGB")
    draw = ImageDraw.Draw(img)
    for f in figs:
        box = images.to_px(pg, f.rect, img, 2)
        draw.rectangle(box, outline=(220, 0, 0), width=3)
        draw.rectangle((box[0], box[1], box[0] + 34, box[1] + 26), fill=(220, 0, 0))
        draw.text((box[0] + 6, box[1] + 4), str(f.id), fill=(255, 255, 255), font_size=20)
    for name, box in saved:
        draw.rectangle(box, outline=(0, 160, 0), width=3)
        draw.text((box[0] + 4, box[3] + 2), name, fill=(0, 120, 0), font_size=16)
    return img


# ---------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser(description="Cut figures for image placeholders out of page PNGs.")
    ap.add_argument("parent_dir")
    ap.add_argument("pdf_name")
    ap.add_argument("config")
    ap.add_argument("--out")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-llm", action="store_true")
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()

    with open(args.config, encoding="utf-8") as f:
        cfg = yaml.safe_load(f)
    fcfg = cfg.get("figures", {})
    job = Job(cfg, args.parent_dir, args.pdf_name, args.out)
    out_dir, id_prefix = job.out_dir, job.id_prefix

    lang = fcfg.get("language", next(iter(cfg["languages"])))
    lcfg = cfg["languages"][lang]
    md_path = out_dir / lcfg["output"]
    if not md_path.exists():
        raise SystemExit(f"Error: {md_path} not found (run pdf_ocr.py first)")
    placeholders = parse_placeholders(md_path.read_text(encoding="utf-8"))

    analyzers = {name: PageAnalyzer(src, fcfg) for name, src in job.sources.items()}

    def figs_on(pg: PageRef):
        return analyzers[pg.src.name].figures(pg.no)

    images = PageImages()
    pad = fcfg.get("padding", 3)
    preview_dir = out_dir / fcfg.get("preview_subdir", "figure_previews")
    preview_dir.mkdir(exist_ok=True)

    # the cloud model, used only for ambiguous cases
    client = None
    if not args.no_llm and fcfg.get("use_llm", True):
        try:
            from dotenv import load_dotenv
            load_dotenv(pathlib.Path(__file__).resolve().parent.parent / ".env")
        except ImportError:
            pass
        if os.getenv(cfg["llm"].get("api_key_env", "OPENAI_API_KEY")):
            client = OpenAIClient(cfg["llm"])
        else:
            print("No API key found; ambiguous figures are resolved by local heuristics only.")

    # problem and solution pages per grade; number all candidates on them
    # (for previews and the model)
    prob_src = job.sources[lcfg["problems"]]
    by_grade = {g: [PageRef(prob_src, p) for p in ps] for g, ps in problem_pages(job, lcfg).items()}
    answer_pages = {}
    for g in by_grade:
        sol_src, ps = solution_pages(job, lcfg, g)
        answer_pages[g] = [PageRef(sol_src, p) for p in ps]
    all_pages = sorted({pg for ps in list(by_grade.values()) + list(answer_pages.values()) for pg in ps})
    next_id = 1
    for pg in all_pages:
        for f in reading_order(figs_on(pg)):
            f.id = next_id
            next_id += 1

    assignments = {}   # placeholder name -> (source, page, rect in PDF points | px box)
    report = []

    def ask_model(pid, names, part_text, pages, part):
        """Let the model choose candidate boxes (or give a bbox) for the placeholders."""
        pages = [pg for pg in pages if figs_on(pg)] or pages[:1]
        imgs = []
        for pg in pages:
            ov = preview_dir / f"llm_{pid}_{part}_{pg.src.stem}_p{pg.no:03d}.png"
            overlay(images, pg, figs_on(pg)).save(ov)
            imgs.append(ov)
        pr = fcfg["prompts"]
        user = fill(pr["select"], problem_id=pid, part=part, placeholders="\n".join(names),
                    text=part_text, pages=", ".join(f"image {i + 1} = {pg}" for i, pg in enumerate(pages)))
        reply = strip_fences(client.ask(pr["system"], user, imgs))
        mm = re.search(r"\{.*\}", reply, re.S)
        answer = json.loads(mm.group(0)) if mm else {}
        by_id = {f.id: f for pg in pages for f in figs_on(pg)}
        for name in names:
            val = answer.get(name)
            if isinstance(val, list) and val and all(i in by_id for i in val):
                figs = [by_id[i] for i in val]
                if len({f.page for f in figs}) == 1:
                    assignments[name] = ("llm", figs[0].page, union([f.rect for f in figs]))
                    continue
            if isinstance(val, dict) and "bbox" in val:
                idx = int(val.get("image", 1)) - 1
                if 0 <= idx < len(pages):
                    assignments[name] = ("llm-bbox", pages[idx], tuple(val["bbox"]))
                    continue
            report.append(f"{name}: model gave no usable answer ({val!r})")

    for g, pages in by_grade.items():
        # --- problem statements: candidates grouped by the preceding number marker
        markers = [(pi, y, n) for pi, pg in enumerate(pages) for y, n in analyzers[pg.src.name].markers(pg.no)]
        owned = {}   # problem number -> [figures]
        for pi, pg in enumerate(pages):
            for f in figs_on(pg):
                cy = (f.rect[1] + f.rect[3]) / 2
                prev = [mk for mk in markers if (mk[0], mk[1]) <= (pi, cy)]
                if prev:
                    owned.setdefault(prev[-1][2], []).append(f)
        numbers = [mk[2] for mk in markers]
        if numbers != sorted(numbers):
            report.append(f"grade {g}: suspicious marker sequence {numbers}")

        for pid, ph in placeholders.items():
            mm = re.fullmatch(re.escape(id_prefix) + r"\.([^.]+)\.(\d+)", pid)
            if not mm or mm.group(1) != str(g):
                continue
            n = int(mm.group(2))
            names = [x for x in ph["problem"] if x not in assignments]
            if names:
                cands = reading_order(owned.get(n, []))
                if len(cands) == len(names):
                    for name, f in zip(names, cands):
                        assignments[name] = ("local", f.page, f.rect)
                elif client:
                    mk_pages = sorted({pages[mk[0]] for mk in markers if mk[2] in (n, n + 1)} |
                                      {f.page for f in cands}) or pages
                    ask_model(pid, names, ph["problem_text"], mk_pages, "problem")
                else:
                    picked = reading_order(sorted(cands, key=lambda f: -f.area)[:len(names)])
                    for name, f in zip(names, picked):
                        assignments[name] = ("guess", f.page, f.rect)
                    report.append(f"{pid}: {len(names)} placeholder(s), {len(cands)} candidate(s) (guessed)")

            # --- solutions: figures above the "Joonis N" captions of the answer pages
            names = [x for x in ph["solution"] if x not in assignments]
            if not names:
                continue
            nums = caption_numbers(ph["solution_text"], names, re.compile(fcfg.get(
                "caption_mention_regex", r"[Jj]oonis\w*\s+(\d+)"), re.I))
            unresolved = []
            for name in names:
                found = None
                for pg in answer_pages[g]:
                    for cap, num in analyzers[pg.src.name].captions(pg.no):
                        if num != nums.get(name):
                            continue
                        above = [f for f in figs_on(pg)
                                 if f.rect[3] <= cap[1] + 2 and cap[1] - f.rect[3] <= fcfg.get("caption_max_gap", 40)]
                        # figures directly above the caption (side-by-side figures may
                        # have their own captions); otherwise the whole row above it
                        over = [f for f in above if f.rect[0] <= cap[2] + 20 and f.rect[2] >= cap[0] - 20]
                        if over:
                            best = max(over, key=lambda f: f.rect[3])
                            row_figs = [f for f in over if touches(f.rect, best.rect, 0)]
                            # parts stacked above each other (e.g. two bars) form one figure
                            stack_gap = fcfg.get("caption_stack_gap", 15)
                            grown = True
                            while grown:
                                box = union([f.rect for f in row_figs])
                                more = [f for f in analyzers[pg.src.name].figures(pg.no)
                                        if f not in row_figs and f.rect[3] <= box[1] + 1
                                        and box[1] - f.rect[3] <= stack_gap
                                        and f.rect[0] <= box[2] and f.rect[2] >= box[0]]
                                row_figs += more
                                grown = bool(more)
                        elif above:
                            best = max(above, key=lambda f: f.rect[3])
                            row_figs = [f for f in above if touches(f.rect, best.rect, 0) or
                                        abs(f.rect[3] - best.rect[3]) <= 10]
                        if above:
                            found = (pg, union([f.rect for f in row_figs]))
                if found:
                    assignments[name] = ("caption", found[0], found[1])
                else:
                    unresolved.append(name)
            if unresolved and client:
                ask_model(pid, unresolved, ph["solution_text"], answer_pages[g], "solution")
            elif unresolved:
                report.append(f"{pid}: solution figure(s) {unresolved} not found locally")

    # --- save figures and previews
    saved_boxes = {}
    saved_lines = []
    seen = {}
    placeholder_order = [n for ph in placeholders.values() for n in ph["problem"] + ph["solution"]]
    for name in [n for n in placeholder_order if n in assignments]:
        source, p, rect = assignments[name]
        if (p, rect) in seen:
            report.append(f"{name}: same region as {seen[(p, rect)]} (check the placeholders)")
        seen.setdefault((p, rect), name)
        img = Image.open(images.path(p)).convert("RGB")
        if source == "llm-bbox":
            box = tuple(int(v / 1000 * (img.width if i % 2 == 0 else img.height)) for i, v in enumerate(rect))
            crop = trim_white(img.crop(box))
        else:
            box = images.to_px(p, rect, img, pad)
            crop = img.crop(box)
        saved_boxes.setdefault(p, []).append((name, box))
        target = out_dir / name
        status = "dry-run"
        if not args.dry_run:
            if target.exists() and not args.force:
                status = "exists, kept"
            else:
                crop.save(target)
                status = "saved"
        saved_lines.append(f"{name}: {source}, {p}, {crop.width}x{crop.height}px, {status}")

    for pg in all_pages:
        if figs_on(pg) or pg in saved_boxes:
            overlay(images, pg, figs_on(pg), saved_boxes.get(pg, [])).save(
                preview_dir / f"{pg.src.stem}_p{pg.no:03d}.png")

    missing = [n for ph in placeholders.values() for n in ph["problem"] + ph["solution"] if n not in assignments]
    for n in missing:
        report.append(f"{n}: NOT FOUND")
    report = saved_lines + ([""] + report if report else [])
    (out_dir / "figures_report.txt").write_text("\n".join(report) + "\n", encoding="utf-8")
    print("\n".join(report))
    total = len(missing) + len(assignments)
    print(f"\n{len(assignments)} of {total} figures located; previews in {preview_dir}")


if __name__ == "__main__":
    main()
