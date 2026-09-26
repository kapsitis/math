"""
Configurable PDF -> PNG -> Markdown OCR pipeline (adapted from ../openai_ocr.py).

Usage:
    python pdf_ocr.py <parent_dir> <pdf_name> <config.yaml> [options]

    <parent_dir>   directory containing the CSV page list (e.g. list.csv) and the PDFs
    <pdf_name>     PDF file inside <parent_dir>; must be listed in the CSV
    <config.yaml>  page geometry, grade/answer detection rules and LLM prompts

Options:
    --out DIR      output directory (default: config "output_dir" template)
    --langs ee,ru  process only these languages (default: all in the config)
    --render-only  only render PNGs, do not call the cloud service
    --dry-run      render PNGs and write the prompts that would be sent (prompts/*.txt)
    --force        ignore cached LLM responses in <out>/raw/

Pipeline:
  1. For every language (e.g. "ee", "ru") read its page range from the CSV
     (1-based, both endpoints included) and render each page to a PNG, cropped
     to remove margins, the page header and the footer (see "geometry" in YAML).
  2. Split the pages of every language into grades (by a regex on the page
     header, or evenly across the configured grade list).
  3. Locate pages with official answers for every grade (e.g. "7. klass, I osa"
     after the problem pages) and render them as well (answer_pages/ subdir).
  4. Send one request per (language, grade) to the vision model; languages that
     declare "answers_from" receive the Markdown of that language as text
     instead of answer pages (so e.g. Russian reuses Estonian answers).
  5. Concatenate the responses into content_<lang>.md and validate that every
     problem has a <small> section with "answer" and "questionType:ShortAnswer".
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
                current = int(m.group(1))
            if current is not None:
                result.setdefault(current, []).append(p)
        if sorted(result) == sorted(grades) and sum(map(len, result.values())) == len(pages):
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

def validate_markdown(md: str, lang: str):
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
            if not re.search(r"^\*\s*questionType:\s*ShortAnswer\s*$", small.group(1), re.M):
                problems.append("no questionType:ShortAnswer")
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

    parent = pathlib.Path(args.parent_dir)
    pdf_path = parent / args.pdf_name
    if not pdf_path.is_file():
        raise SystemExit(f"Error: {pdf_path} not found")
    row = read_csv_row(parent / cfg.get("csv_file", "list.csv"), args.pdf_name, cfg.get("file_column", "File"))

    stem = pdf_path.stem
    m = re.search(cfg.get("year_regex", r"(\d{4})"), args.pdf_name)
    year = m.group(1) if m else stem
    tvars = dict(parent=parent.as_posix(), stem=stem, year=year)
    id_prefix = fill(cfg["problem_id_prefix"], **tvars)
    out_dir = pathlib.Path(args.out or fill(cfg["output_dir"], **tvars))
    out_dir.mkdir(parents=True, exist_ok=True)
    print(f"Processing {pdf_path} -> {out_dir} (problem IDs {id_prefix}.<grade>.<n>)")

    doc = pymupdf.open(pdf_path)
    renderer = PageRenderer(doc, cfg.get("geometry", {}), cfg.get("render", {}).get("dpi", 200))
    png_name = cfg.get("png_name", "{stem}_p{page}.png")

    def png_for(page_no: int, subdir: str | None = None) -> pathlib.Path:
        d = out_dir / subdir if subdir else out_dir
        d.mkdir(parents=True, exist_ok=True)
        path = d / fill(png_name, stem=stem, page=f"{page_no:03d}")
        renderer.render(page_no, path)
        return path

    languages = cfg["languages"]
    selected = args.langs.split(",") if args.langs else list(languages)
    grades = cfg["grades"]

    # 1-2. Render the page ranges and split them by grade.
    lang_pages = {}   # lang -> {grade: [png paths]}
    last_page = 0
    for lang, lcfg in languages.items():
        first, last = int(row[lcfg["first_column"]]), int(row[lcfg["last_column"]])
        last_page = max(last_page, last)
        if lang not in selected:
            continue
        pages = list(range(first, last + 1))
        by_grade = split_by_grade(renderer, pages, grades, lcfg.get("grade_regex"))
        print(f"  [{lang}] pages {first}-{last}: " +
              ", ".join(f"grade {g}: {ps}" for g, ps in by_grade.items()))
        lang_pages[lang] = {g: [png_for(p) for p in ps] for g, ps in by_grade.items()}

    # 3. Locate and render answer pages (searched after all problem ranges).
    answer_pngs = {}
    acfg = cfg.get("answers") or {}
    if acfg.get("enabled"):
        for g in grades:
            pages = find_answer_pages(renderer, acfg, g, last_page + 1)
            if not pages:
                print(f"  Warning: no answer pages found for grade {g}")
            else:
                print(f"  answers for grade {g}: pages {pages}")
            answer_pngs[g] = [png_for(p, acfg.get("png_subdir", "answer_pages")) for p in pages]

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
            images = list(pngs)
            if not source_lang:
                images += answer_pngs.get(g, [])
            pvars = dict(id_prefix=id_prefix, grade=g, year=year, stem=stem,
                         num_problem_pages=len(pngs),
                         num_answer_pages=0 if source_lang else len(answer_pngs.get(g, [])),
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
        validate_markdown(md, lang)

    print("\nProcessing complete.")


if __name__ == "__main__":
    main()
