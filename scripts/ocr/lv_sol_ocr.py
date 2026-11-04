"""
LV.SOL archive (sources/LV.SOL.ARCHIVE/so<NN>_uzd.pdf + so<NN>_atr.pdf) -> page PNGs ->
Markdown (problembase/LV.SOL/lv-sol-<YYYY>/content_lv.md) with the figures cut out as
LV.SOL.<YYYY>.<grade>.<n>.png (problem statement) and ...<n>A.png, ...<n>B.png (solution).

Usage (from the math/ directory):
    python scripts/ocr/lv_sol_ocr.py sources/LV.SOL.ARCHIVE so38 [so39 ...] [options]
    python scripts/ocr/lv_sol_ocr.py sources/LV.SOL.ARCHIVE --all --skip so70

Options:
    --config FILE   default: lv_sol.yaml next to this script
    --stage S       render | ocr | assemble | figures | all (default: all; every stage
                    runs the earlier ones that are not cached yet)
    --force         redo the given stage even if its results are cached
    --workers N     parallel requests to the cloud service (default: config llm.workers)

Pipeline (all intermediate files are in <output_dir>/work/):
  1. render    every page of both PDFs -> work/pages/<stem>_p001.png, cropped to the
               page content (margins, page numbers and the URL footer removed);
               figure candidates (clusters of vector drawings and raster images, as in
               extract_figures.py) -> work/boxes/<stem>_p001.json, and the same page
               with numbered red boxes -> work/boxes/<stem>_p001.png
  2. ocr       one request per page (the boxed PNG) -> work/ocr/<stem>_p001.md:
               faithful Markdown + LaTeX; figures are written as [[FIG <stem>-p001-3]]
               (red box 3) or [[FIG <stem>-p001-bbox-x0,y0,x1,y1]] (box given by the model)
  3. assemble  one text-only request per grade with the whole problems and solutions
               transcriptions -> work/grades/<grade>.md (problems with IDs and solutions)
  4. figures   [[FIG ...]] lines -> PNG files with the problem IDs, the <small> metadata
               placeholder before every "## Atrisinājums", content_lv.md, work/report.txt
To fix a problem by hand, edit a file in work/ocr or work/grades and rerun the later
stages (e.g. --stage figures), which reuse everything that is cached.
"""
import argparse
import concurrent.futures as cf
import json
import os
import pathlib
import re
import sys
import threading
import time
import traceback

import yaml
import pymupdf
from PIL import Image, ImageDraw, ImageOps

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from pdf_ocr import OpenAIClient, PageRenderer, fill, strip_fences  # noqa: E402
from extract_figures import PageAnalyzer, union  # noqa: E402

SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
MATH_DIR = SCRIPT_DIR.parent.parent
FIG_RX = re.compile(r"\[\[FIG\s+([^\]]+?)\s*\]\]")
_print_lock = threading.Lock()


def log(*args):
    with _print_lock:
        print(*args, flush=True)


# ---------------------------------------------------------------- one PDF

class Pdf:
    """One PDF (problems or solutions) of a year; the attributes PageAnalyzer needs."""

    def __init__(self, year_job, kind: str, path: pathlib.Path):
        cfg = year_job.cfg
        self.job, self.kind, self.path = year_job, kind, path
        self.name, self.stem = kind, path.stem
        self.doc = pymupdf.open(path)
        self.dpi = cfg["render"]["dpi"]
        self.renderer = PageRenderer(self.doc, cfg.get("geometry", {}), self.dpi)
        self.analyzer = PageAnalyzer(self, cfg["figures"])
        self.pages = list(range(1, len(self.doc) + 1))

    def tag(self, page_no):
        return f"{self.stem}-p{page_no:03d}"

    def page_png(self, page_no):
        return self.job.work / "pages" / f"{self.stem}_p{page_no:03d}.png"

    def boxed_png(self, page_no):
        return self.job.work / "boxes" / f"{self.stem}_p{page_no:03d}.png"

    def boxes_json(self, page_no):
        return self.job.work / "boxes" / f"{self.stem}_p{page_no:03d}.json"

    def ocr_md(self, page_no):
        return self.job.work / "ocr" / f"{self.stem}_p{page_no:03d}.md"

    # -- stage 1
    def render(self, page_no, force=False):
        png, js, boxed = self.page_png(page_no), self.boxes_json(page_no), self.boxed_png(page_no)
        if png.exists() and js.exists() and boxed.exists() and not force:
            return
        for p in (png, js, boxed):
            p.parent.mkdir(parents=True, exist_ok=True)
        clip = self.renderer.clip_rect(page_no)
        pix = self.doc[page_no - 1].get_pixmap(dpi=self.dpi, clip=clip)
        img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
        # trim the white border, keep a little padding
        pad = self.job.cfg["render"].get("trim_padding", 12)
        mask = ImageOps.invert(img.convert("L")).point(lambda v: 255 if v > 10 else 0)
        bbox = mask.getbbox() or (0, 0, img.width, img.height)
        crop = (max(0, bbox[0] - pad), max(0, bbox[1] - pad),
                min(img.width, bbox[2] + pad), min(img.height, bbox[3] + pad))
        img = img.crop(crop)
        img.save(png)

        scale = self.dpi / 72
        fcfg = self.job.cfg["figures"]
        max_area = fcfg.get("max_page_fraction", 0.6) * clip.width * clip.height
        cands = []
        page = self.doc[page_no - 1]
        drawings = [tuple(d["rect"]) for d in page.get_drawings()]
        min_h = fcfg.get("min_image_only_height", 20)
        for f in self.analyzer.figures(page_no):
            if f.area > max_area:
                continue
            r = f.rect
            # inline formulas embedded as raster images (one text line high, no vector lines)
            if r[3] - r[1] < min_h and not any(
                    d[0] < r[2] and r[0] < d[2] and d[1] < r[3] and r[1] < d[3] for d in drawings):
                continue
            r = f.rect
            px = [int((r[0] - clip.x0) * scale - crop[0]), int((r[1] - clip.y0) * scale - crop[1]),
                  int((r[2] - clip.x0) * scale - crop[0]) + 1, int((r[3] - clip.y0) * scale - crop[1]) + 1]
            px = [max(0, px[0]), max(0, px[1]), min(img.width, px[2]), min(img.height, px[3])]
            if px[2] - px[0] < 4 or px[3] - px[1] < 4:
                continue
            cands.append(dict(rect_pt=list(r), box_px=px))
        cands.sort(key=lambda c: (c["box_px"][1], c["box_px"][0]))
        for i, c in enumerate(cands, 1):
            c["id"] = i
        js.write_text(json.dumps(dict(clip=list(clip), crop=list(crop), scale=scale,
                                      size=[img.width, img.height], candidates=cands), indent=1),
                      encoding="utf-8")
        boxed_img = img.copy()
        draw = ImageDraw.Draw(boxed_img)
        for c in cands:
            b = c["box_px"]
            draw.rectangle(b, outline=(230, 0, 0), width=2)
            ty = b[1] - 22 if b[1] >= 22 else b[1]
            draw.rectangle((b[0], ty, b[0] + 28, ty + 22), fill=(230, 0, 0))
            draw.text((b[0] + 5, ty + 2), str(c["id"]), fill=(255, 255, 255), font_size=18)
        boxed_img.save(boxed)

    def boxes(self, page_no):
        return json.loads(self.boxes_json(page_no).read_text(encoding="utf-8"))


# ---------------------------------------------------------------- one year

class YearJob:
    def __init__(self, cfg, archive: pathlib.Path, nn: str):
        self.cfg = cfg
        self.nn = nn
        self.year = cfg.get("year_offset", 1950) + int(nn)
        self.school_year = f"{self.year - 1}./{self.year}."
        self.id_prefix = fill(cfg["problem_id_prefix"], year=self.year)
        self.out = pathlib.Path(fill(cfg["output_dir"], math=MATH_DIR.as_posix(), year=self.year))
        self.work = self.out / "work"
        self.pdfs = {}
        for kind in cfg["kinds"]:
            path = archive / f"so{nn}_{kind}.pdf"
            if not path.is_file():
                raise SystemExit(f"Error: {path} not found")
            self.pdfs[kind] = Pdf(self, kind, path)

    def __str__(self):
        return f"{self.id_prefix} (so{self.nn})"

    def tokens(self):
        """All valid figure token prefixes -> (pdf, page)."""
        return {pdf.tag(p): (pdf, p) for pdf in self.pdfs.values() for p in pdf.pages}

    def kind_md(self, kind):
        pdf = self.pdfs[kind]
        parts = []
        for p in pdf.pages:
            f = pdf.ocr_md(p)
            if not f.exists():
                raise SystemExit(f"Error: {f} is missing (run --stage ocr)")
            parts.append(f"<!-- {pdf.path.name}, page {p} -->\n" + f.read_text(encoding="utf-8").strip())
        return "\n\n".join(parts)

    def grades(self):
        override = (self.cfg.get("grades_override") or {}).get(self.year)
        if override:
            return list(override)
        text = self.kind_md("uzd")
        found = []
        for m in re.finditer(r"(?<![\d.])(\d{1,2})\.\s*klase", text):
            g = int(m.group(1))
            if 4 <= g <= 12 and g not in found:
                found.append(g)
        if not found:
            raise SystemExit(f"Error: {self}: no grade headings found; set grades_override")
        return sorted(found)

    def grade_md(self, grade):
        return self.work / "grades" / f"{grade}.md"


# ---------------------------------------------------------------- cloud requests

class Llm:
    def __init__(self, cfg):
        try:
            from dotenv import load_dotenv
            load_dotenv(SCRIPT_DIR.parent / ".env")
        except ImportError:
            pass
        if not os.getenv(cfg["llm"].get("api_key_env", "OPENAI_API_KEY")):
            raise SystemExit("Error: no API key (scripts/.env OPENAI_API_KEY)")
        self.client = OpenAIClient(cfg["llm"])

    def ask(self, system, user, images=(), what=""):
        for attempt in range(4):
            try:
                text = strip_fences(self.client.ask(system, user, list(images)))
                if text.strip():
                    return text
                raise RuntimeError("empty response")
            except Exception as e:  # noqa: BLE001
                if type(e).__name__ in ("AuthenticationError", "PermissionDeniedError"):
                    raise SystemExit(f"Error: the cloud service rejected the API key: {e}")
                wait = 10 * (attempt + 1)
                log(f"  {what}: {type(e).__name__}: {e} - retrying in {wait}s")
                time.sleep(wait)
        raise RuntimeError(f"{what}: no answer after 4 attempts")


def run_parallel(tasks, workers, label):
    """tasks: list of (name, callable). Errors are reported, not raised."""
    if not tasks:
        return 0
    log(f"{label}: {len(tasks)} requests, {workers} in parallel")
    failed = 0
    with cf.ThreadPoolExecutor(max_workers=workers) as ex:
        futs = {ex.submit(fn): name for name, fn in tasks}
        for i, fut in enumerate(cf.as_completed(futs), 1):
            name = futs[fut]
            try:
                fut.result()
                log(f"  [{i}/{len(tasks)}] {name}")
            except SystemExit:
                raise
            except Exception:  # noqa: BLE001
                failed += 1
                log(f"  [{i}/{len(tasks)}] {name} FAILED")
                traceback.print_exc()
    return failed


# ---------------------------------------------------------------- stage 2: page OCR

def ocr_page(llm, cfg, pdf: Pdf, page_no):
    p = cfg["prompts"]
    kind_text = "problems" if pdf.kind == "uzd" else "solutions"
    user = fill(p["ocr_page"], page=page_no, file=pdf.path.name, kind_text=kind_text,
                school_year=pdf.job.school_year)
    # image 1: the clean page (for reading); image 2: the same page with numbered figure boxes
    md = llm.ask(p["ocr_system"], user, [pdf.page_png(page_no), pdf.boxed_png(page_no)],
                 what=pdf.tag(page_no))
    raw = pdf.ocr_md(page_no).with_suffix(".raw.md")
    raw.parent.mkdir(parents=True, exist_ok=True)
    raw.write_text(md, encoding="utf-8")
    ids = {c["id"] for c in pdf.boxes(page_no)["candidates"]}
    tag = pdf.tag(page_no)

    def repl(m):
        body = m.group(1).replace(" ", "")
        if re.fullmatch(r"\d+(\+\d+)*", body) and all(int(n) in ids for n in body.split("+")):
            return f"[[FIG {tag}-{body}]]"
        nums = re.fullmatch(r"(\d+),(\d+),(\d+),(\d+)", body)
        if nums:
            return f"[[FIG {tag}-bbox-{body}]]"
        return f"<!-- FIG? {m.group(1)} -->"
    pdf.ocr_md(page_no).write_text(FIG_RX.sub(repl, md).strip() + "\n", encoding="utf-8")


# ---------------------------------------------------------------- stage 3: per grade

def example_text(cfg):
    path = pathlib.Path(fill(cfg["example_md"], math=MATH_DIR.as_posix()))
    if not path.exists():
        return ""
    text = re.sub(r"(?s)<small>.*?</small>\s*", "", path.read_text(encoding="utf-8"))
    text = text[:cfg.get("example_chars", 3500)]
    cut = text.rfind("# <lo-sample/>")
    return text[:cut].strip() if cut > 0 else text.strip()


def assemble_grade(llm, cfg, job: YearJob, grade, grades):
    p = cfg["prompts"]
    user = fill(p["assemble_grade"], uzd_file=job.pdfs["uzd"].path.name,
                atr_file=job.pdfs["atr"].path.name, school_year=job.school_year,
                grades=", ".join(map(str, grades)), grade=grade, id_prefix=job.id_prefix,
                example=example_text(cfg))
    # the transcriptions may contain braces: insert them after the template is filled
    user = user.replace("{uzd_md}", job.kind_md("uzd")).replace("{atr_md}", job.kind_md("atr"))
    md = llm.ask(p["assemble_system"], user, what=f"{job} grade {grade}")
    out = job.grade_md(grade)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(md.strip() + "\n", encoding="utf-8")


# ---------------------------------------------------------------- stage 4: figures, final Markdown

def crop_token(job: YearJob, token: str, tokens: dict):
    """[[FIG token]] -> (PIL image, width in pt) or None."""
    m = re.fullmatch(r"(so\d\d_\w+-p\d{3})-(.+)", token)
    if not m or m.group(1) not in tokens:
        return None
    pdf, page = tokens[m.group(1)]
    info = pdf.boxes(page)
    img = Image.open(pdf.page_png(page)).convert("RGB")
    rest = m.group(2)
    if rest.startswith("bbox-"):
        try:
            x0, y0, x1, y1 = (int(v) for v in rest[5:].split(","))
        except ValueError:
            return None
        box = (img.width * x0 // 1000, img.height * y0 // 1000,
               img.width * x1 // 1000 + 1, img.height * y1 // 1000 + 1)
        if box[2] - box[0] < 5 or box[3] - box[1] < 5:
            return None
        part = img.crop(box)
        mask = ImageOps.invert(part.convert("L")).point(lambda v: 255 if v > 10 else 0)
        if mask.getbbox():
            part = part.crop(mask.getbbox())
        return part, part.width / info["scale"]
    cands = {c["id"]: c for c in info["candidates"]}
    try:
        chosen = [cands[int(n)] for n in rest.split("+")]
    except (KeyError, ValueError):
        return None
    r = union([c["rect_pt"] for c in chosen])
    pad = job.cfg["figures"].get("padding", 4)
    clip, crop, s = info["clip"], info["crop"], info["scale"]
    box = (int((r[0] - pad - clip[0]) * s - crop[0]), int((r[1] - pad - clip[1]) * s - crop[1]),
           int((r[2] + pad - clip[0]) * s - crop[0]) + 1, int((r[3] + pad - clip[1]) * s - crop[1]) + 1)
    box = (max(0, box[0]), max(0, box[1]), min(img.width, box[2]), min(img.height, box[3]))
    return img.crop(box), r[2] - r[0] + 2 * pad


def side_by_side(images, gap=30):
    h = max(i.height for i in images)
    w = sum(i.width for i in images) + gap * (len(images) - 1)
    out = Image.new("RGB", (w, h), "white")
    x = 0
    for i in images:
        out.paste(i, (x, (h - i.height) // 2))
        x += i.width + gap
    return out


def width_attr(cfg, width_pt):
    f = cfg["figures"]
    px = round(width_pt * f.get("width_px_per_pt", 1.3) / 50) * 50
    return max(f.get("min_width_px", 100), min(f.get("max_width_px", 500), px))


def finalize(job: YearJob, grades, report: list):
    cfg = job.cfg
    tokens = job.tokens()
    meta = cfg["metadata_block"].rstrip("\n")
    for old in job.out.glob(f"{job.id_prefix}.*.png"):
        old.unlink()
    blocks_out = []
    for g in grades:
        f = job.grade_md(g)
        if not f.exists():
            report.append(f"grade {g}: MISSING {f.name}")
            continue
        text = f.read_text(encoding="utf-8")
        blocks = re.split(r"(?m)^(?=# <lo-sample/>)", text)
        blocks = [b for b in blocks if b.startswith("# <lo-sample/>")]
        expected = [f"{job.id_prefix}.{g}.{i}" for i in range(1, len(blocks) + 1)]
        ids = [b.splitlines()[0].replace("# <lo-sample/>", "").strip() for b in blocks]
        line = f"grade {g}: {len(blocks)} problems"
        if ids != expected:
            line += f"  WARNING: IDs {ids}"
        if len(blocks) not in (3, 5):
            line += "  WARNING: unusual number of problems"
        report.append(line)
        for pid, block in zip(ids, blocks):
            blocks_out.append(finalize_problem(job, pid, block, tokens, meta, report))
    md = "\n\n\n".join(b.strip() for b in blocks_out) + "\n"
    (job.out / cfg.get("output_md", "content_lv.md")).write_text(md, encoding="utf-8")


def finalize_problem(job, pid, block, tokens, meta, report):
    cfg = job.cfg
    head, sep, sol = block.partition("\n## Atrisinājums")
    if not sep:
        sol = "\n\n<!-- TODO: atrisinājums nav atrasts -->\n"
        report.append(f"  {pid}: no '## Atrisinājums' heading")
    if "TODO: atrisinājums nav atrasts" in sol:
        report.append(f"  {pid}: no solution found")

    # statement: all figures in one PNG at the place of the first one
    figs = [(m, crop_token(job, m.group(1), tokens)) for m in FIG_RX.finditer(head)]
    good = [(m, c) for m, c in figs if c]
    for m, c in figs:
        if not c:
            report.append(f"  {pid}: bad figure reference [[FIG {m.group(1)}]]")
    if good:
        img = side_by_side([c[0] for _, c in good]) if len(good) > 1 else good[0][1][0]
        img.save(job.out / f"{pid}.png")
        width = width_attr(cfg, sum(c[1] for _, c in good))
        first = good[0][0].group(0)
        head = head.replace(first, f"![]({pid}.png){{ width={width}px }}", 1)
    head = FIG_RX.sub(lambda m: "" if any(m.group(0) == g[0].group(0) for g in good)
                      else f"<!-- FIG? {m.group(1)} -->", head)

    # solution: one PNG per figure, A, B, C, ...
    letters = iter("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    def repl(m):
        c = crop_token(job, m.group(1), tokens)
        if not c:
            report.append(f"  {pid}: bad figure reference [[FIG {m.group(1)}]] in the solution")
            return f"<!-- FIG? {m.group(1)} -->"
        name = f"{pid}{next(letters)}.png"
        c[0].save(job.out / name)
        return f"![]({name}){{ width={width_attr(cfg, c[1])}px }}"
    sol = FIG_RX.sub(repl, sol)
    head = re.sub(r"\n{3,}", "\n\n", head.rstrip()) + "\n\n"
    sol = re.sub(r"\n{3,}", "\n\n", sol.strip("\n"))
    return f"{head}{meta}\n\n## Atrisinājums\n\n{sol.strip()}\n"


# ---------------------------------------------------------------- main

STAGES = ["render", "ocr", "assemble", "figures"]


def main():
    ap = argparse.ArgumentParser(description="LV.SOL archive PDFs -> content_lv.md + figures")
    ap.add_argument("archive")
    ap.add_argument("names", nargs="*", help="so38 so39 ... (or 38, 1988)")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--skip", nargs="*", default=[])
    ap.add_argument("--config", default=str(SCRIPT_DIR / "lv_sol.yaml"))
    ap.add_argument("--stage", choices=STAGES + ["all"], default="all")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--workers", type=int)
    args = ap.parse_args()

    cfg = yaml.safe_load(pathlib.Path(args.config).read_text(encoding="utf-8"))
    archive = pathlib.Path(args.archive)
    rx = re.compile(cfg["file_regex"])
    available = sorted({m.group(1) for f in archive.iterdir() if (m := rx.match(f.name))})

    def norm(n):
        n = str(n).lower().removeprefix("so")
        return f"{int(n) - cfg.get('year_offset', 1950):02d}" if len(n) == 4 else n
    names = available if args.all else [norm(n) for n in args.names]
    names = [n for n in names if n not in {norm(s) for s in args.skip}]
    if not names:
        raise SystemExit("Nothing to do: give so<NN> names or --all")
    jobs = [YearJob(cfg, archive, n) for n in names]
    last = STAGES.index(args.stage) if args.stage != "all" else len(STAGES) - 1
    forced = args.stage if args.force else None
    workers = args.workers or cfg["llm"].get("workers", 6)

    # 1. render
    for job in jobs:
        for pdf in job.pdfs.values():
            for p in pdf.pages:
                pdf.render(p, force=forced in ("render",))
        log(f"{job}: pages rendered -> {job.work / 'pages'}")
    if last == 0:
        return

    llm = Llm(cfg)
    # 2. ocr
    tasks = []
    for job in jobs:
        for pdf in job.pdfs.values():
            for p in pdf.pages:
                if forced == "ocr" or not pdf.ocr_md(p).exists():
                    tasks.append((pdf.tag(p), lambda pdf=pdf, p=p: ocr_page(llm, cfg, pdf, p)))
    if run_parallel(tasks, workers, "OCR of pages"):
        log("Some pages failed; rerun to retry them (cached pages are skipped).")
        return
    if last == 1:
        return

    # 3. assemble
    tasks, year_grades = [], {}
    for job in jobs:
        grades = job.grades()
        year_grades[job.year] = grades
        log(f"{job}: grades {grades}")
        for g in grades:
            if forced == "assemble" or not job.grade_md(g).exists():
                tasks.append((f"{job} grade {g}",
                              lambda job=job, g=g, gs=grades: assemble_grade(llm, cfg, job, g, gs)))
    if run_parallel(tasks, workers, "Assembling grades"):
        log("Some grades failed; rerun to retry them.")
    if last == 2:
        return

    # 4. figures + content_lv.md
    for job in jobs:
        report = [f"{job}: {job.pdfs['uzd'].path.name}, {job.pdfs['atr'].path.name}"]
        finalize(job, year_grades[job.year], report)
        (job.work / "report.txt").write_text("\n".join(report) + "\n", encoding="utf-8")
        log("\n".join(report))
        log(f"Wrote {job.out / cfg.get('output_md', 'content_lv.md')}\n")


if __name__ == "__main__":
    main()
