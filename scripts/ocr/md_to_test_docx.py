#!/usr/bin/env python3
"""
Convert content_<lang>.md files (output of pdf_ocr.py / extract_figures.py) into
printable short-answer test sheets content_<lang>.docx for students.

Usage:
    python md_to_test_docx.py <dir-or-md-file> [...] [--config ee_pk_test.yaml] [--variant A]

    A directory argument converts every content_*.md in it. The .docx is written
    next to the .md file (content_ee.md -> content_ee.docx).

Layout (A4, one Word section per grade, each starting on a new page):
  * page header: "<test title> — 7. klase — I daļa — variants A" and a line
    "Vārds, uzvārds: ______ Klase: ____" (labels depend on the language, see
    the "docx" key of the YAML config);
  * every problem is a borderless table row that is never split across pages:
      [problem text | figure (if narrow) | answer column]
    The answer column (1/3 of the text width) is identical for all problems, so
    the answer boxes form one vertical column at the right margin. It holds the
    answer box (~45 x 12 mm, grey "Atbilde:" inside at the top), a small square
    for the teacher's points to its right, and up to 4 dotted lines below.
    Wide figures (wider than "wide_figure_ratio" of the text area) are placed
    under the problem text instead of beside it.
  * answers and solutions (<small> ... and everything after it) are omitted.

Math ($...$, $$...$$) becomes native Word equations via pandoc; python-docx then
builds the layout (same two-stage approach as nms-courses/scripts/md_to_docx.py).

Requirements: pandoc on PATH; Python packages python-docx, pyyaml, pillow.
"""
from __future__ import annotations

import argparse
import copy
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass

import docx
import yaml
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_ROW_HEIGHT_RULE, WD_CELL_VERTICAL_ALIGNMENT
from docx.enum.text import WD_TAB_ALIGNMENT, WD_TAB_LEADER, WD_LINE_SPACING
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Mm, Pt, RGBColor
from PIL import Image

# Defaults; every key can be overridden under "docx:" in the YAML config.
DEFAULTS = {
    "page": {"width": 210, "height": 297, "left": 15, "right": 15, "top": 26, "bottom": 15,
             "header_distance": 8},                       # mm
    "font": "Calibri",
    "font_size": 11,
    "answer_column": 60,          # mm, <= 1/3 of the text width (180 mm on A4)
    "answer_box": [45, 12],       # mm
    "points_box": 8,              # mm, square for the teacher's mark
    "reasoning_lines": 3,         # dotted lines under the answer box (0..4)
    "reasoning_line_height": 6,   # mm
    "figure_dpi": 200,            # resolution of the figure PNGs (render.dpi of pdf_ocr.py)
    "figure_scale": 1.0,          # 1.0 = same size as in the original PDF
    "wide_figure_ratio": 0.6,     # wider figures go under the text
    "max_side_figure_ratio": 0.6,   # figures beside the text may take this share
    "gap": 3,                     # mm between columns
    "grade_regex": r"\.([^.]+)\.(\d+)$",   # problem ID -> (grade, number)
    "labels": {
        "lv": {"title": "Matemātikas īso atbilžu tests — {grade}. klase — I daļa — variants {variant}",
               "name": "Vārds, uzvārds:", "class": "Klase:", "answer": "Atbilde:"},
        "ee": {"title": "Matemaatika lühivastustega test — {grade}. klass — I osa — variant {variant}",
               "name": "Ees- ja perekonnanimi:", "class": "Klass:", "answer": "Vastus:"},
        "ru": {"title": "Тест по математике с короткими ответами — {grade} класс — I часть — вариант {variant}",
               "name": "Имя, фамилия:", "class": "Класс:", "answer": "Ответ:"},
        "en": {"title": "Mathematics short-answer test — Grade {grade} — Part I — variant {variant}",
               "name": "Name, surname:", "class": "Class:", "answer": "Answer:"},
    },
}

PLACEHOLDER = re.compile(r"!\[[^\]]*\]\(([^)\s]+)\)(\{[^}]*\})?")
SENTINEL = "QQSENT-{kind}-{key}-QQ"
SENTINEL_RX = re.compile(r"^QQSENT-(TEXT|FIG|WIDE|END)-(\d+)-QQ$")


def merge(base: dict, extra: dict) -> dict:
    out = copy.deepcopy(base)
    for k, v in (extra or {}).items():
        out[k] = merge(out[k], v) if isinstance(v, dict) and isinstance(out.get(k), dict) else v
    return out


# ---------------------------------------------------------------- markdown

def parse_problems(md: str, grade_rx: re.Pattern) -> list:
    """List of dicts: id, grade, number, text (statement only), figures (file names)."""
    problems = []
    for block in re.split(r"(?m)^# <lo-sample/>\s*", md)[1:]:
        pid, _, body = block.partition("\n")
        pid = pid.strip()
        statement = body.split("<small>")[0]
        statement = re.split(r"(?m)^##\s", statement)[0]      # no solution without <small>
        figures = [m.group(1) for m in PLACEHOLDER.finditer(statement)]
        text = PLACEHOLDER.sub("", statement)
        text = re.sub(r"\n{3,}", "\n\n", text).strip()
        m = grade_rx.search(pid)
        grade, number = (m.group(1), m.group(2)) if m else ("", pid)
        problems.append(dict(id=pid, grade=grade, number=number, text=text, figures=figures))
    return problems


def figure_size_mm(path: pathlib.Path, cfg: dict):
    with Image.open(path) as im:
        w, h = im.size
    k = 25.4 / cfg["figure_dpi"] * cfg["figure_scale"]
    return w * k, h * k


def plan_layout(problems, md_dir: pathlib.Path, cfg: dict):
    """Decide for every figure: beside the text or under it, and its width in mm.

    Figures of one problem are placed next to each other in one line. They go
    beside the text if they fit into "max_side_figure_ratio" of the text area
    (and none of them is wider than "wide_figure_ratio"), otherwise under it.
    """
    page = cfg["page"]
    text_area = page["width"] - page["left"] - page["right"] - cfg["answer_column"]
    gap = cfg["gap"]
    for p in problems:
        p["side"], p["wide"], p["missing"] = [], [], []
        figs = []
        for name in p["figures"]:
            path = md_dir / name
            if path.exists():
                figs.append((name, figure_size_mm(path, cfg)[0]))
            else:
                p["missing"].append(name)
        total = sum(w for _, w in figs) + gap * max(0, len(figs) - 1)
        if figs and all(w <= cfg["wide_figure_ratio"] * text_area for _, w in figs)                 and total <= cfg["max_side_figure_ratio"] * text_area:
            p["side"] = figs
            p["side_width"] = total
        else:
            k = min(1.0, (text_area - 4) / total) if figs else 1.0
            p["wide"] = [(n, w * k) for n, w in figs]
            p["side_width"] = 0
    return text_area


def build_pandoc_markdown(problems) -> str:
    """Problem statements separated by sentinel paragraphs, to be split again in the .docx."""
    out = []
    for i, p in enumerate(problems):
        text = p["text"]
        # bold problem number in front of the first paragraph
        text = f"**{p['number']}.** " + text if text and not text.startswith("$$") else f"**{p['number']}.**\n\n" + text
        out.append(SENTINEL.format(kind="TEXT", key=i))
        out.append(text)
        for name in p["missing"]:
            out.append(f"*[figure {name} is missing]*")
        if p["side"]:
            out.append(SENTINEL.format(kind="FIG", key=i))
            out.append(" ".join(f"![]({n}){{width={w:.1f}mm}}" for n, w in p["side"]))
        if p["wide"]:
            out.append(SENTINEL.format(kind="WIDE", key=i))
            out.append(" ".join(f"![]({n}){{width={w:.1f}mm}}" for n, w in p["wide"]))
        out.append(SENTINEL.format(kind="END", key=i))
    return "\n\n".join(out) + "\n"


def run_pandoc(src: str, resource_dir: pathlib.Path, docx_path: pathlib.Path):
    pandoc = shutil.which("pandoc")
    if not pandoc:
        sys.exit("pandoc not found on PATH")
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".md", dir=resource_dir,
                                     delete=False) as tmp:
        tmp.write(src)
    try:
        subprocess.run([pandoc, tmp.name, "-o", str(docx_path), "--from", "markdown",
                        "--resource-path", str(resource_dir)], check=True)
    finally:
        pathlib.Path(tmp.name).unlink(missing_ok=True)


# ---------------------------------------------------------------- docx helpers

def set_cell_borders(cell, sz=8, color="000000", sides=("top", "left", "bottom", "right"), val="single"):
    tcPr = cell._tc.get_or_add_tcPr()
    borders = tcPr.find(qn("w:tcBorders"))
    if borders is None:
        borders = OxmlElement("w:tcBorders")
        tcPr.append(borders)
    for side in ("top", "left", "bottom", "right"):
        el = OxmlElement(f"w:{side}")
        if side in sides:
            el.set(qn("w:val"), val)
            el.set(qn("w:sz"), str(sz))
            el.set(qn("w:color"), color)
        else:
            el.set(qn("w:val"), "nil")
        borders.append(el)


def set_table_fixed(table, widths_mm, cell_margin_mm=1.0):
    tbl = table._tbl
    tblPr = tbl.tblPr
    layout = OxmlElement("w:tblLayout")
    layout.set(qn("w:type"), "fixed")
    tblPr.append(layout)
    tblW = tblPr.find(qn("w:tblW"))
    if tblW is None:
        tblW = OxmlElement("w:tblW")
        tblPr.append(tblW)
    tblW.set(qn("w:w"), str(int(sum(widths_mm) / 25.4 * 1440)))
    tblW.set(qn("w:type"), "dxa")
    mar = OxmlElement("w:tblCellMar")
    for side in ("left", "right"):
        el = OxmlElement(f"w:{side}")
        el.set(qn("w:w"), str(int(cell_margin_mm / 25.4 * 1440)))
        el.set(qn("w:type"), "dxa")
        mar.append(el)
    tblPr.append(mar)
    table.autofit = False
    for i, w in enumerate(widths_mm):
        table.columns[i].width = Mm(w)
        for cell in table.columns[i].cells:
            cell.width = Mm(w)


def row_cant_split(row):
    trPr = row._tr.get_or_add_trPr()
    trPr.append(OxmlElement("w:cantSplit"))


def tiny_paragraph(p, size=2):
    """Make a paragraph (e.g. an empty cell paragraph) almost invisible."""
    fmt = p.paragraph_format
    fmt.space_before = fmt.space_after = Pt(0)
    fmt.line_spacing = Pt(size)
    fmt.line_spacing_rule = WD_LINE_SPACING.EXACTLY


def move_into_cell(cell, elements):
    """Move body elements (paragraphs, tables) into a table cell."""
    first = cell.paragraphs[0]._p
    for el in elements:
        first.addprevious(el)
    if elements and elements[-1].tag == qn("w:p"):
        first.getparent().remove(first)       # the default empty paragraph is not needed


def add_answer_column(cell, cfg, label):
    """Grey label, answer box with a points square to its right, dotted lines below."""
    box_w, box_h = cfg["answer_box"]
    sq = cfg["points_box"]
    gap = cfg["answer_column"] - box_w - sq - 2
    pad = (box_h - sq) / 2
    lab = cell.paragraphs[0]
    tiny_paragraph(lab, 9)
    lab.paragraph_format.space_after = Pt(1)
    run = lab.add_run(label)
    run.font.size = Pt(7)
    run.font.color.rgb = RGBColor(0x80, 0x80, 0x80)
    # 3 rows (pad, square, pad); the box is drawn by the borders of its 3 cells
    # (Word does not draw borders of vertically merged cells reliably)
    t = cell.add_table(rows=3, cols=3)
    set_table_fixed(t, [box_w, gap, sq], cell_margin_mm=0)
    for r, h in zip(t.rows, (pad, sq, pad)):
        r.height = Mm(h)
        r.height_rule = WD_ROW_HEIGHT_RULE.EXACTLY
    set_cell_borders(t.cell(0, 0), sides=("top", "left", "right"))
    set_cell_borders(t.cell(1, 0), sides=("left", "right"))
    set_cell_borders(t.cell(2, 0), sides=("left", "right", "bottom"))
    set_cell_borders(t.cell(1, 2), sz=6)
    for c in t._cells:
        for par in c.paragraphs:
            tiny_paragraph(par)
    for _ in range(max(0, min(4, cfg["reasoning_lines"]))):
        par = cell.add_paragraph()
        fmt = par.paragraph_format
        fmt.space_before = fmt.space_after = Pt(0)
        fmt.line_spacing = Mm(cfg["reasoning_line_height"])
        fmt.line_spacing_rule = WD_LINE_SPACING.EXACTLY
        fmt.tab_stops.add_tab_stop(Mm(cfg["answer_column"] - 3), WD_TAB_ALIGNMENT.RIGHT, WD_TAB_LEADER.DOTS)
        r = par.add_run("	")
        r.font.color.rgb = RGBColor(0x80, 0x80, 0x80)
    if cfg["reasoning_lines"] <= 0:
        tiny_paragraph(cell.add_paragraph())


def fill_header(section, cfg, labels, grade, variant):
    section.header.is_linked_to_previous = False
    hdr = section.header
    text_w = cfg["page"]["width"] - cfg["page"]["left"] - cfg["page"]["right"]
    p1 = hdr.paragraphs[0]
    p1.text = ""
    r = p1.add_run(labels["title"].format(grade=str(grade).replace("_", "–"), variant=variant))
    r.bold = True
    r.font.size = Pt(12)
    p1.paragraph_format.space_after = Pt(8)
    p2 = hdr.add_paragraph()
    tabs = p2.paragraph_format.tab_stops
    tabs.add_tab_stop(Mm(text_w * 0.68), WD_TAB_ALIGNMENT.LEFT, WD_TAB_LEADER.HEAVY)
    tabs.add_tab_stop(Mm(text_w), WD_TAB_ALIGNMENT.RIGHT, WD_TAB_LEADER.HEAVY)
    p2.add_run(f"{labels['name']} \t {labels['class']} \t")
    for p in (p1, p2):
        p.paragraph_format.space_before = Pt(0)


def style_document(document, cfg):
    for style in document.styles:
        if style.type == 1:   # paragraph styles
            try:
                style.paragraph_format.space_before = Pt(0)
                style.paragraph_format.space_after = Pt(4)
            except AttributeError:
                pass
    normal = document.styles["Normal"]
    normal.font.name = cfg["font"]
    normal.font.size = Pt(cfg["font_size"])
    rpr = normal.element.get_or_add_rPr()
    fonts = rpr.find(qn("w:rFonts"))
    if fonts is None:
        fonts = OxmlElement("w:rFonts")
        rpr.append(fonts)
    for attr in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        fonts.set(qn(attr), cfg["font"])
    for name in ("Body Text", "First Paragraph", "Compact"):
        if name in [s.name for s in document.styles]:
            document.styles[name].font.name = cfg["font"]
            document.styles[name].font.size = Pt(cfg["font_size"])


def set_page(section, cfg):
    pg = cfg["page"]
    section.page_width, section.page_height = Mm(pg["width"]), Mm(pg["height"])
    section.left_margin, section.right_margin = Mm(pg["left"]), Mm(pg["right"])
    section.top_margin, section.bottom_margin = Mm(pg["top"]), Mm(pg["bottom"])
    section.header_distance = Mm(pg["header_distance"])


# ---------------------------------------------------------------- conversion

def convert(md_path: pathlib.Path, cfg: dict, variant: str):
    lang = re.sub(r"^content_", "", md_path.stem)
    labels = cfg["labels"].get(lang) or cfg["labels"]["lv"]
    problems = parse_problems(md_path.read_text(encoding="utf-8"), re.compile(cfg["grade_regex"]))
    if not problems:
        print(f"Skipping {md_path}: no problems found")
        return
    text_area = plan_layout(problems, md_path.parent, cfg)
    docx_path = md_path.with_suffix(".docx")
    run_pandoc(build_pandoc_markdown(problems), md_path.parent, docx_path)

    document = docx.Document(str(docx_path))
    body = document.element.body
    # split the pandoc output at the sentinels
    parts = {}          # (kind, index) -> [elements]
    current = None
    for el in list(body):
        if el.tag == qn("w:sectPr"):
            continue
        text = "".join(t.text or "" for t in el.iter(qn("w:t"))) if el.tag == qn("w:p") else ""
        m = SENTINEL_RX.match(text.strip())
        body.remove(el)
        if m:
            current = None if m.group(1) == "END" else (m.group(1), int(m.group(2)))
            if current:
                parts[current] = []
        elif current:
            parts[current].append(el)

    style_document(document, cfg)
    set_page(document.sections[0], cfg)
    ans_w, gap = cfg["answer_column"], cfg["gap"]
    grades = []
    for i, p in enumerate(problems):
        if not grades or grades[-1] != p["grade"]:
            if grades:
                document.add_section(WD_SECTION.NEW_PAGE)
            grades.append(p["grade"])
        side = parts.get(("FIG", i), [])
        side_w = p["side_width"] + gap if side else 0
        widths = [text_area - side_w] + ([side_w] if side else []) + [ans_w]
        table = document.add_table(rows=1, cols=len(widths))
        set_table_fixed(table, widths)
        row_cant_split(table.rows[0])
        cells = table.rows[0].cells
        for c in cells:
            c.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.TOP
        move_into_cell(cells[0], parts.get(("TEXT", i), []) + parts.get(("WIDE", i), []))
        if side:
            move_into_cell(cells[1], side)
        add_answer_column(cells[-1], cfg, labels["answer"])
        spacer = document.add_paragraph()
        tiny_paragraph(spacer, 8)

    for section, grade in zip(document.sections, grades):
        set_page(section, cfg)
        fill_header(section, cfg, labels, grade, variant)
    document.save(str(docx_path))
    n_fig = sum(len(p["side"]) + len(p["wide"]) for p in problems)
    missing = [m for p in problems for m in p["missing"]]
    print(f"Wrote {docx_path}: {len(problems)} problems, grades {', '.join(grades)}, {n_fig} figures"
          + (f", MISSING figures: {', '.join(missing)}" if missing else ""))


def main():
    ap = argparse.ArgumentParser(description="Convert content_<lang>.md into short-answer test .docx files.")
    ap.add_argument("inputs", nargs="+", help="content_<lang>.md files or directories containing them")
    ap.add_argument("--config", help="YAML config; its 'docx' key overrides the layout defaults")
    ap.add_argument("--variant", default="A", help="test variant shown in the title (default: A)")
    args = ap.parse_args()

    cfg = DEFAULTS
    if args.config:
        with open(args.config, encoding="utf-8") as f:
            cfg = merge(DEFAULTS, (yaml.safe_load(f) or {}).get("docx", {}))
    files = []
    for inp in map(pathlib.Path, args.inputs):
        files += sorted(inp.glob("content_*.md")) if inp.is_dir() else [inp]
    if not files:
        sys.exit("No content_*.md files found")
    for f in files:
        convert(f, cfg, args.variant)


if __name__ == "__main__":
    main()
