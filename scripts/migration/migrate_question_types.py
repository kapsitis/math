"""One-off migration of legacy questionType values in content_lv.md files.

Usage:
    python migrate_question_types.py [problembase_dir] [--csv questionTypes2.csv] [--dry-run]

For each problem ("# <lo-sample/> PROBLEM.ID"; <lo-exercise/> textbook samples are
left as they are) the "* questionType:..." line in its
<small>...</small> block is rewritten:

1. Legacy values become QTY_ labels of questionTypes2.csv (see LEGACY_VALUES, taken
   from the "Vecās vērtības" table of the question type documentation).
   ShortAnswer is a response format, not a question type: its value is dropped
   (to be classified anew) and "* responseFormat:RSP_Answer" is added.
2. If the problem text has sub-parts **(A)**, **(B)**, ... and the line has as many
   values as there are sub-parts, it is split into one line per sub-part:
   "* questionType:A: QTY_...", "* questionType:B: QTY_...".
3. If the number of values differs, the sub-part lines are still created, with all
   the values on the first one ("* questionType:A: QTY_...,QTY_...") and the other
   ones empty.

A questionType line repeated with the same value is kept once. Problems with lines
that cannot be migrated safely are reported (SKIPPED, REVIEW) and left for manual
checking. Problems whose questionType lines are already split by sub-part are left
alone, so the script can be run again. Only the questionType lines change (plus the added
responseFormat lines); the rest of each file is kept byte for byte.
"""

import argparse
import csv
import os
import re
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_PROBLEMBASE = os.path.normpath(os.path.join(SCRIPT_DIR, '..', '..', 'problembase'))
DEFAULT_CSV = os.path.normpath(os.path.join(
    SCRIPT_DIR, '..', '..', '..', 'worksheet-generation-with-llms', 'scripts', 'setup', 'resources',
    'questionTypes2.csv'))

# Legacy value -> QTY_ label ("Vecās vērtības" in ontology_question_types/content_lv.md)
LEGACY_VALUES = {
    'Find': 'QTY_Find',
    'FindAll': 'QTY_FindAll',
    'FindOptimal': 'QTY_FindOptimal',
    'FindValue': 'QTY_FindValue',
    'FindCount': 'QTY_FindValue',
    'FindExample': 'QTY_ConstructExample',
    'Algorithm': 'QTY_ConstructProcedure',
    'Prove': 'QTY_Prove',
    'ProveExistence': 'QTY_ProveExistence',
    'ProveUniversal': 'QTY_ProveUniversal',
    'Decide': 'QTY_Decide',
    'DecideExistence': 'QTY_DecideExistence',
    'DecideUniversal': 'QTY_DecideUniversal',
    'DecideWinner': 'QTY_DecideWinner',
    'ProveDisprove': 'QTY_Decide',      # approximate; to be refined to a subtype
    'ProveDisproveNT': 'QTY_Decide',    # a misspelt ProveDisprove
}
SHORT_ANSWER = 'ShortAnswer'
SHORT_ANSWER_FORMAT = 'RSP_Answer'

# Section headings ("# <lo-sample/> ID", "# <lo-exercise/> ID", ...); only
# <lo-sample/> sections are problems whose metadata is migrated
HEADING_RE = re.compile(r'^#\s+<([A-Za-z-]+)\s*/>\s*(\S+)')
PROBLEM_TAG = 'lo-sample'
QUESTION_TYPE_RE = re.compile(r'^(\s*\*\s*)questionType\s*:(.*?)(\r?\n)?$')
SPLIT_LINE_RE = re.compile(r'^\s*\*\s*questionType\s*:\s*[A-Za-z0-9]{1,2}\s*:')
RESPONSE_FORMAT_RE = re.compile(r'^\s*\*\s*responseFormat\s*:')
SUBPART_RE = re.compile(r'\*\*\(([A-Za-z0-9]{1,2})\)\*\*')
PLAIN_SUBPART_RE = re.compile(r'^\s*\(([A-E])\)\s', re.M)


def load_labels(csv_path):
    with open(csv_path, encoding='utf-8') as f:
        return {row['Label'] for row in csv.DictReader(f) if row['Label'].startswith('QTY_')}


def map_value(value, labels):
    """(new value, is short answer) for one legacy value; raises ValueError if unknown."""
    if value in labels:
        return value, False
    if value == SHORT_ANSWER:
        return '', True
    if value in LEGACY_VALUES:
        return LEGACY_VALUES[value], False
    raise ValueError(f"unknown questionType value '{value}'")


def migrate_problem(lines, start, end, labels, title, report):
    """Rewrite the questionType line of the problem in lines[start:end]; returns the new lines."""
    section = lines[start:end]
    small = next((i for i, l in enumerate(section) if '<small>' in l), None)
    small_end = None if small is None else next((i for i in range(small, len(section)) if '</small>' in section[i]), None)
    if small_end is None:
        return section
    qt = [i for i in range(small + 1, small_end) if QUESTION_TYPE_RE.match(section[i])]
    if not qt or any(SPLIT_LINE_RE.match(section[i]) for i in qt):
        return section
    duplicates = []
    if len(qt) > 1:
        if len({QUESTION_TYPE_RE.match(section[i]).group(2).strip() for i in qt}) > 1:
            report('SKIPPED', title, f'{len(qt)} different questionType lines')
            return section
        duplicates = qt[1:]  # repeated identical lines: keep (and migrate) the first one
        report('DEDUPLICATED', title, f'removed {len(duplicates)} repeated questionType line(s)')

    problem_text = ''.join(section[1:small])
    subparts = list(dict.fromkeys(SUBPART_RE.findall(problem_text)))
    if len(subparts) < 2:
        subparts = []
        if PLAIN_SUBPART_RE.findall(problem_text):
            report('REVIEW', title, 'sub-parts without bold markers, e.g. "(A) ..."; not split')

    i = qt[0]
    m = QUESTION_TYPE_RE.match(section[i])
    prefix, raw, newline = m.group(1), m.group(2), m.group(3) or ''
    old_values = [v.strip() for v in raw.split(',') if v.strip()]
    try:
        mapped = [map_value(v, labels) for v in old_values]
    except ValueError as e:
        report('SKIPPED', title, str(e))
        return section
    values = [v for v, _ in mapped]
    short_answer = any(sa for _, sa in mapped)

    if not subparts:
        new_lines = [f'{prefix}questionType:{",".join(v for v in values if v)}{newline}']
        if len(values) > 1:
            report('REVIEW', title, f'{len(values)} values but no **(A)** sub-parts; kept as a list')
    elif len(values) == len(subparts):
        new_lines = [f'{prefix}questionType:{p}: {v}'.rstrip() + newline for p, v in zip(subparts, values)]
    else:
        first = ','.join(v for v in values if v)
        new_lines = [f'{prefix}questionType:{subparts[0]}: {first}'.rstrip() + newline]
        new_lines += [f'{prefix}questionType:{p}:{newline}' for p in subparts[1:]]
        if values:
            report('MISMATCH', title, f'{len(values)} values for {len(subparts)} sub-parts; all put under {subparts[0]}')
    if short_answer and not any(RESPONSE_FORMAT_RE.match(l) for l in section[small + 1:small_end]):
        new_lines.append(f'{prefix}responseFormat:{SHORT_ANSWER_FORMAT}{newline or chr(10)}')

    old_line = section[i]
    if new_lines != [old_line]:
        report('CHANGED', title, f'{old_line.strip()}  ->  ' + ' | '.join(l.strip() for l in new_lines))
    rest = [l for n, l in enumerate(section[i + 1:], start=i + 1) if n not in duplicates]
    return section[:i] + new_lines + rest


def migrate_file(path, labels, dry_run, report):
    with open(path, encoding='utf-8', newline='') as f:
        lines = f.read().splitlines(keepends=True)
    heads = [i for i, l in enumerate(lines) if HEADING_RE.match(l)] + [len(lines)]
    result = lines[:heads[0]]
    for start, end in zip(heads, heads[1:]):
        tag, title = HEADING_RE.match(lines[start]).groups()
        if tag != PROBLEM_TAG:
            result += lines[start:end]
            continue
        result += migrate_problem(lines, start, end, labels, title,
                                  lambda kind, pid, msg: report(kind, path, pid, msg))
    if result != lines and not dry_run:
        with open(path, 'w', encoding='utf-8', newline='') as f:
            f.write(''.join(result))
    return result != lines


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('problembase', nargs='?', default=DEFAULT_PROBLEMBASE,
                        help='Directory with content_lv.md files (default: math/problembase)')
    parser.add_argument('--csv', default=DEFAULT_CSV, help='questionTypes2.csv with the QTY_ labels')
    parser.add_argument('--dry-run', action='store_true', help='Report the changes without writing files')
    args = parser.parse_args(argv)

    labels = load_labels(args.csv)
    unknown = {v for v in LEGACY_VALUES.values() if v not in labels}
    if unknown:
        print(f'Error: not in {args.csv}: {", ".join(sorted(unknown))}')
        return 1

    counts = {}

    def report(kind, path, pid, msg):
        counts[kind] = counts.get(kind, 0) + 1
        print(f'{kind}: {os.path.relpath(path, args.problembase)}: {pid}: {msg}')

    changed_files = 0
    for root, dirs, files in os.walk(args.problembase):
        dirs.sort()
        if 'content_lv.md' in files:
            changed_files += migrate_file(os.path.join(root, 'content_lv.md'), labels, args.dry_run, report)

    verb = 'would change' if args.dry_run else 'changed'
    print(f'\nDone: {verb} {changed_files} files; ' + ', '.join(f'{k}: {v}' for k, v in sorted(counts.items())))
    return 1 if counts.get('SKIPPED') else 0


if __name__ == '__main__':
    sys.exit(main())
