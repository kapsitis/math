"""
Configurable PDF -> PNG -> Markdown OCR pipeline (adapted from ../openai_ocr.py).

Usage:
    python pdf_ocr.py <parent_dir> <pdf_name> <config.yaml> [options]

    <parent_dir>   directory containing the PDFs (and the optional page list CSV)
    <pdf_name>     the main PDF inside <parent_dir>, e.g. pk2006.pdf or test-2011.pdf
    <config.yaml>  sources (PDFs and page ranges), page geometry, grade/solution
                   detection rules and LLM prompts; see ee_pk_test.yaml, pl_omj_test.yaml

Options:
    --out DIR      output directory (default: config "output_dir" template)
    --langs ee,ru  process only these languages (default: all in the config)
    --render-only  only render PNGs, do not call the cloud service
    --dry-run      render PNGs and write the prompts that would be sent (prompts/*.txt)
    --force        ignore cached LLM responses in <out>/raw/

Configuration model:
  sources     named PDF files with page ranges, e.g. the test pages of one
              language, or a separate solutions PDF. File names and page numbers
              are templates: {pdf} = <pdf_name>, {stem} = its name without .pdf,
              {csv:column} = a column of this PDF's row in the optional
              "page_list" CSV, "end" = last page, "+1"/"-1" offsets. Pages are
              1-based and both ends are included; without "pages" all are used.
  languages   one Markdown output per language: which source holds the
              problems, which source holds the official solutions (optionally
              narrowed per grade by "solutions_find"), or "answers_from" another
              language whose Markdown is passed as text instead.
  grades      problem groups; the problem pages are split among them by
              "grade_regex" (page header) or evenly. One LLM request per
              (language, grade); a single group such as "7_8" takes all pages.

Pipeline:
  1. Render the pages of all sources to PNGs, cropped to remove margins, page
     header and footer ("geometry"); solution pages may go to a subdirectory.
  2. Send one request per (language, grade) to the vision model with the
     problem pages and the matching solution pages (or the Markdown of the
     "answers_from" language).
  3. Concatenate the responses into content_<lang>.md and validate that every
     problem has a <small> section with "answer" and the expected questionType.
"""
import argparse
import base64
import csv
import os
import pathlib
import re
import sys
import traceback

import yaml
import pymupdf


# ---------------------------------------------------------------- helpers

def fill(template: str, **values) -> str:
    """Replace {name} placeholders with values; other braces (LaTeX, etc.) are left as-is."""
    def repl(m):
        key = m.group(1)
        return str(values[key]) if key in values else m.group(0)
    return re.sub(r"\{([A-Za-z_][A-Za-z0-9_]*)\}", repl, template)


def strip_fences(text: str) -> str:
    text = text.strip()
    text = re.sub(r"^```[a-zA-Z]*\s*\n", "", text)
    text = re.sub(r"\n?```\s*$", "", text)
    return text.strip()


def encode_image_to_base64(image_path) -> str:
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")


def read_csv_row(csv_path: pathlib.Path, pdf_name: str, file_column: str) -> dict:
    with open(csv_path, newline="", encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            row = {k.strip(): (v or "").strip() for k, v in row.items()}
            if row.get(file_column) == pdf_name:
                return row
    raise SystemExit(f"Error: '{pdf_name}' is not listed in {csv_path}")


class Job:
    """Paths, template values and PDF sources for one run (shared by all scripts)."""

    def __init__(self, cfg: dict, parent_dir: str, pdf_name: str, out: str | None = None):
        self.cfg = cfg
        self.parent = pathlib.Path(parent_dir)
        self.pdf_name = pdf_name
        if not (self.parent / pdf_name).is_file():
            raise SystemExit(f"Error: {self.parent / pdf_name} not found")
        stem = pathlib.Path(pdf_name).stem
        m = re.search(cfg.get("year_regex", r"(\d{4})"), pdf_name)
        self.tvars = dict(parent=self.parent.as_posix(), pdf=pdf_name, stem=stem,
                          year=m.group(1) if m else stem)
        self.year = self.tvars["year"]
        self.id_prefix = fill(cfg["problem_id_prefix"], **self.tvars)
        self.out_dir = pathlib.Path(out or fill(cfg["output_dir"], **self.tvars))
        self.dpi = cfg.get("render", {}).get("dpi", 200)
        self._row = None
        self._docs = {}
        self.sources = {name: Source(self, name, scfg) for name, scfg in cfg["sources"].items()}

    def csv_row(self) -> dict:
        if self._row is None:
            pl = self.cfg.get("page_list")
            if not pl:
                raise SystemExit("Error: {csv:...} is used, but the config has no 'page_list'")
            self._row = read_csv_row(self.parent / pl["file"], self.pdf_name, pl.get("key_column", "File"))
        return self._row

    def open_pdf(self, path: pathlib.Path):
        if path not in self._docs:
            if not path.is_file():
                raise SystemExit(f"Error: {path} not found")
            self._docs[path] = pymupdf.open(path)
        return self._docs[path]

    def resolve_page(self, spec, n_pages: int) -> int:
        """1-based page number from an int, "end", or a template like "{csv:ru_last}+1"."""
        text = str(spec).strip()
        if text == "end":
            return n_pages
        text = re.sub(r"\{csv:([^}]+)\}", lambda m: self.csv_row()[m.group(1)], text)
        m = re.fullmatch(r"(\d+)\s*([+-]\s*\d+)?", text)
        if not m:
            raise SystemExit(f"Error: cannot understand page number '{spec}'")
        return int(m.group(1)) + (int(m.group(2).replace(" ", "")) if m.group(2) else 0)


class Source:
    """A PDF file of a job and the pages used from it."""

    def __init__(self, job: Job, name: str, scfg: dict):
        self.job, self.name = job, name
        self.path = job.parent / fill(scfg.get("file", "{pdf}"), **job.tvars)
        self.stem = self.path.stem
        self.doc = job.open_pdf(self.path)
        geometry = {**job.cfg.get("geometry", {}), **(scfg.get("geometry") or {})}
        self.renderer = PageRenderer(self.doc, geometry, job.dpi)
        first, last = scfg.get("pages", [1, "end"])
        n = len(self.doc)
        self.pages = list(range(job.resolve_page(first, n), job.resolve_page(last, n) + 1))
        self.png_dir = job.out_dir / scfg["png_subdir"] if scfg.get("png_subdir") else job.out_dir

    def png_path(self, page_no: int) -> pathlib.Path:
        name = fill(self.job.cfg.get("png_name", "{stem}_p{page}.png"), stem=self.stem, page=f"{page_no:03d}")
        return self.png_dir / name

    def render(self, page_no: int) -> pathlib.Path:
        path = self.png_path(page_no)
        path.parent.mkdir(parents=True, exist_ok=True)
        self.renderer.render(page_no, path)
        return path


def problem_pages(job: Job, lcfg: dict) -> dict:
    """grade -> problem pages of a language."""
    src = job.sources[lcfg["problems"]]
    return split_by_grade(src.renderer, src.pages, job.cfg["grades"], lcfg.get("grade_regex"))


def solution_pages(job: Job, lcfg: dict, grade) -> tuple:
    """(source, pages) with the official solutions of a grade, or (None, [])."""
    if not lcfg.get("solutions"):
        return None, []
    src = job.sources[lcfg["solutions"]]
    find = lcfg.get("solutions_find")
    if not find:
        return src, list(src.pages)
    pages = find_answer_pages(src.renderer, find, grade, src.pages[0])
    return src, [p for p in pages if p in src.pages]


# ---------------------------------------------------------------- page geometry

class PageRenderer:
    """Renders single PDF pages to PNGs, cropping margins, header and footer."""

    def __init__(self, doc, geometry: dict, dpi: int):
        self.doc = doc
        self.dpi = dpi
        self.margins = geometry.get("margins", {})
        self.header = geometry.get("header") or {}
        self.footer = geometry.get("footer") or {}

    def page_text(self, page_no: int) -> str:
        return self.doc[page_no - 1].get_text()

    def header_text(self, page_no: int) -> str:
        """Text of the blocks inside the header search zone (used for grade detection)."""
        page = self.doc[page_no - 1]
        zone = self.header.get("zone", 0)
        blocks = page.get_text("blocks")
        return "\n".join(b[4] for b in blocks if b[3] <= page.rect.y0 + zone)

    def clip_rect(self, page_no: int) -> pymupdf.Rect:
        page = self.doc[page_no - 1]
        r = page.rect
        m = self.margins
        # odd/even pages may have mirrored margins
        side = "odd" if page_no % 2 == 1 else "even"
        m = {**m, **(self.margins.get(side) or {})}
        x0 = r.x0 + m.get("left", 0)
        x1 = r.x1 - m.get("right", 0)
        y0 = r.y0 + m.get("top", 0)
        y1 = r.y1 - m.get("bottom", 0)

        blocks = page.get_text("blocks")
        # Header: text blocks near the top that match the header regex; crop below them.
        if self.header.get("regex"):
            rx = re.compile(self.header["regex"], re.S)
            zone = r.y0 + self.header.get("zone", 0)
            hits = [b for b in blocks if b[3] <= zone and rx.search(b[4])]
            if hits:
                y0 = max(y0, max(b[3] for b in hits) + self.header.get("padding", 0))
        # Footer: text blocks near the bottom that match the footer regex; crop above them.
        if self.footer.get("regex"):
            rx = re.compile(self.footer["regex"], re.S)
            zone = r.y1 - self.footer.get("zone", 0)
            hits = [b for b in blocks if b[1] >= zone and rx.search(b[4])]
            if hits:
                y1 = min(y1, min(b[1] for b in hits) - self.footer.get("padding", 0))
        # Footer separated by a long horizontal rule (e.g. above sponsor logos); crop above it.
        if self.footer.get("rule_min_width"):
            zone = r.y1 - self.footer.get("zone", 0)
            rules = [d["rect"] for d in page.get_drawings()
                     if d["rect"].y0 >= zone and d["rect"].height <= 1.5
                     and d["rect"].width >= self.footer["rule_min_width"]]
            if rules:
                y1 = min(y1, min(rr.y0 for rr in rules) - self.footer.get("padding", 0))
        return pymupdf.Rect(x0, y0, x1, y1)

    def render(self, page_no: int, out_path: pathlib.Path):
        page = self.doc[page_no - 1]
        pix = page.get_pixmap(dpi=self.dpi, clip=self.clip_rect(page_no))
        pix.save(str(out_path))


# ---------------------------------------------------------------- grades and answers

def split_by_grade(renderer: PageRenderer, pages: list, grades: list, grade_regex: str | None) -> dict:
    """Map grade -> list of pages. Uses the header regex; falls back to an even split."""
    result = {}
    if grade_regex:
        rx = re.compile(grade_regex, re.S)
        current = None
        for p in pages:
            m = rx.search(renderer.header_text(p))
            if m:
                found = m.group(1)
                current = next((g for g in grades if str(g) == found), found)
            if current is not None:
                result.setdefault(current, []).append(p)
        if sorted(map(str, result)) == sorted(map(str, grades)) and sum(map(len, result.values())) == len(pages):
            return result
        print(f"  Warning: grade detection found {dict(result)}; falling back to even split.")
    if len(pages) % len(grades) != 0:
        raise SystemExit(f"Error: cannot split pages {pages} evenly among grades {grades}")
    k = len(pages) // len(grades)
    return {g: pages[i * k:(i + 1) * k] for i, g in enumerate(grades)}


def find_answer_pages(renderer: PageRenderer, cfg: dict, grade: int, search_from: int) -> list:
    """Pages from the first match of start_regex (after search_from) to the first match of end_regex."""
    n = len(renderer.doc)
    start_rx = re.compile(fill(cfg["start_regex"], grade=grade), re.S)
    end_rx = re.compile(fill(cfg["end_regex"], grade=grade), re.S) if cfg.get("end_regex") else None
    must = re.compile(cfg["must_contain"], re.S) if cfg.get("must_contain") else None
    max_pages = cfg.get("max_pages", 4)

    start, start_pos = None, 0
    for p in range(search_from, n + 1):
        text = renderer.page_text(p)
        m = start_rx.search(text)
        if m and (must is None or must.search(text)):
            start, start_pos = p, m.end()
            break
    if start is None:
        return []
    pages = []
    for p in range(start, min(n, start + max_pages - 1) + 1):
        pages.append(p)
        text = renderer.page_text(p)
        # on the start page, look for the end marker only after the start marker
        if end_rx and end_rx.search(text[start_pos:] if p == start else text):
            break
    return pages


# ---------------------------------------------------------------- cloud service

class OpenAIClient:
    def __init__(self, llm_cfg: dict):
        import openai
        self.client = openai.OpenAI(api_key=os.getenv(llm_cfg.get("api_key_env", "OPENAI_API_KEY")))
        self.model = os.getenv(llm_cfg.get("model_env", "OPENAI_MODEL"), llm_cfg.get("model", "gpt-5.5"))
        self.cfg = llm_cfg
        print(f"Using OpenAI model: {self.model}")

    def ask(self, system_prompt: str, user_prompt: str, images: list) -> str:
        content = [{"type": "text", "text": user_prompt}]
        for img in images:
            content.append({
                "type": "image_url",
                "image_url": {"url": f"data:image/png;base64,{encode_image_to_base64(img)}",
                              "detail": self.cfg.get("image_detail", "high")},
            })
        kwargs = dict(
            model=self.model,
            messages=[{"role": "system", "content": system_prompt},
                      {"role": "user", "content": content}],
            max_completion_tokens=self.cfg.get("max_completion_tokens", 16000),
        )
        # Reasoning models (gpt-5.5, o-series) accept only the default temperature.
        if self.cfg.get("temperature") is not None:
            kwargs["temperature"] = self.cfg["temperature"]
        response = self.client.chat.completions.create(**kwargs)
        return response.choices[0].message.content or ""


# ---------------------------------------------------------------- validation

def validate_markdown(md: str, lang: str, question_type: str = "ShortAnswer"):
    blocks = re.split(r"(?m)^# <lo-sample/>\s*", md)[1:]
    print(f"  content_{lang}.md: {len(blocks)} problems")
    for b in blocks:
        pid = b.splitlines()[0].strip()
        small = re.search(r"<small>(.*?)</small>", b, re.S)
        problems = []
        if not small:
            problems.append("no <small> section")
        else:
            if not re.search(r"^\*\s*answer:\s*\S", small.group(1), re.M):
                problems.append("no answer")
            if not re.search(rf"^\*\s*questionType:\s*{question_type}\s*$", small.group(1), re.M):
                problems.append(f"no questionType:{question_type}")
        if problems:
            print(f"    Warning: {pid}: {', '.join(problems)}")


# ---------------------------------------------------------------- main pipeline

def main():
    ap = argparse.ArgumentParser(description="Render PDF page ranges to PNGs and OCR them into Markdown.")
    ap.add_argument("parent_dir")
    ap.add_argument("pdf_name")
    ap.add_argument("config")
    ap.add_argument("--out")
    ap.add_argument("--langs")
    ap.add_argument("--render-only", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()

    with open(args.config, encoding="utf-8") as f:
        cfg = yaml.safe_load(f)
    job = Job(cfg, args.parent_dir, args.pdf_name, args.out)
    out_dir, id_prefix, year = job.out_dir, job.id_prefix, job.year
    out_dir.mkdir(parents=True, exist_ok=True)
    print(f"Processing {job.parent / job.pdf_name} -> {out_dir} (problem IDs {id_prefix}.<grade>.<n>)")

    languages = cfg["languages"]
    selected = args.langs.split(",") if args.langs else list(languages)
    grades = cfg["grades"]

    # 1. Render problem pages (split by grade) and solution pages.
    lang_pages = {}   # lang -> {grade: [png paths]}
    answer_pngs = {}  # lang -> {grade: [png paths]}
    for lang in selected:
        lcfg = languages[lang]
        src = job.sources[lcfg["problems"]]
        by_grade = problem_pages(job, lcfg)
        print(f"  [{lang}] {src.path.name} pages {src.pages[0]}-{src.pages[-1]}: " +
              ", ".join(f"grade {g}: {ps}" for g, ps in by_grade.items()))
        lang_pages[lang] = {g: [src.render(p) for p in ps] for g, ps in by_grade.items()}
        answer_pngs[lang] = {}
        for g in by_grade:
            sol, pages = solution_pages(job, lcfg, g)
            if sol is None:
                continue
            if not pages:
                print(f"  Warning: [{lang}] no solution pages found for grade {g}")
            else:
                print(f"  [{lang}] solutions for grade {g}: {sol.path.name} pages {pages}")
            answer_pngs[lang][g] = [sol.render(p) for p in pages]

    if args.render_only:
        print("PNG rendering complete (--render-only).")
        return

    # 4. Ask the cloud service, one request per (language, grade).
    client = None
    if not args.dry_run:
        try:
            from dotenv import load_dotenv
            # API keys live in scripts/.env (the parent of this script's directory)
            load_dotenv(pathlib.Path(__file__).resolve().parent.parent / ".env")
        except ImportError:
            pass
        if not os.getenv(cfg["llm"].get("api_key_env", "OPENAI_API_KEY")):
            print("No API key found; PNGs are rendered. Use --dry-run to inspect the prompts.")
            return
        client = OpenAIClient(cfg["llm"])

    prompts = cfg["prompts"]
    raw_dir = out_dir / "raw"
    raw_dir.mkdir(exist_ok=True)
    results = {}   # lang -> {grade: markdown}
    # languages that reuse answers of another language must run after it
    order = sorted(selected, key=lambda l: 1 if languages[l].get("answers_from") else 0)
    for lang in order:
        lcfg = languages[lang]
        results[lang] = {}
        for g, pngs in lang_pages[lang].items():
            source_lang = lcfg.get("answers_from")
            source_md = results.get(source_lang, {}).get(g, "") if source_lang else ""
            if source_lang and not source_md:
                cached = raw_dir / f"{source_lang}_{g}.md"
                source_md = cached.read_text(encoding="utf-8") if cached.exists() else ""
            solution_pngs = answer_pngs[lang].get(g, [])
            images = list(pngs) + solution_pngs
            pvars = dict(id_prefix=id_prefix, grade=g, year=year, stem=job.tvars["stem"],
                         num_problem_pages=len(pngs), num_answer_pages=len(solution_pngs),
                         source_markdown=source_md)
            system_prompt = fill(prompts["system"], **pvars)
            user_prompt = fill(prompts[lcfg["prompt"]], **pvars)

            raw_path = raw_dir / f"{lang}_{g}.md"
            if args.dry_run:
                pdir = out_dir / "prompts"
                pdir.mkdir(exist_ok=True)
                (pdir / f"{lang}_{g}.txt").write_text(
                    "=== SYSTEM ===\n" + system_prompt + "\n=== USER ===\n" + user_prompt +
                    "\n=== IMAGES ===\n" + "\n".join(p.name for p in images) + "\n", encoding="utf-8")
                continue
            if raw_path.exists() and not args.force:
                print(f"  [{lang}] grade {g}: using cached {raw_path.name}")
                results[lang][g] = raw_path.read_text(encoding="utf-8")
                continue
            try:
                print(f"  [{lang}] grade {g}: sending {len(images)} images...")
                md = strip_fences(client.ask(system_prompt, user_prompt, images))
                raw_path.write_text(md, encoding="utf-8")
                results[lang][g] = md
            except Exception as e:
                # a rejected API key fails every request the same way: stop right away
                if type(e).__name__ in ("AuthenticationError", "PermissionDeniedError"):
                    raise SystemExit(f"Error: the cloud service rejected the API key: {e}")
                print(f"  An error occurred for [{lang}] grade {g}; skipping.")
                traceback.print_exc()

    if args.dry_run:
        print(f"Prompts written to {out_dir / 'prompts'} (--dry-run).")
        return

    # 5. Assemble content_<lang>.md.
    for lang in order:
        parts = [results[lang][g] for g in grades if g in results[lang]]
        if not parts:
            continue
        md = "\n\n\n".join(parts).rstrip() + "\n"
        out_md = out_dir / languages[lang]["output"]
        out_md.write_text(md, encoding="utf-8")
        print(f"Wrote {out_md}")
        validate_markdown(md, lang, cfg.get("question_type", "ShortAnswer"))

    print("\nProcessing complete.")


if __name__ == "__main__":
    main()
