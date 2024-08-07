import re
import sys

# Read problems one by one from Markdown file "filepath"
def extract_sections_from_md(filepath):
    section_titles = []
    current_section = None
    sections = []
    title = "NA"

    heading_re = re.compile(r'^#\s+<lo-sample/>\s+(.*)')

    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            m = heading_re.match(line)
            if m:
                new_title = m.group(1)
                # append the previous (title, current_section)
                if current_section is not None:
                    sections.append((title, current_section))
                title = new_title
                current_section = line
            elif current_section is not None:
                # before seeing the first title, we do not append anything
                current_section += line
    # Append the last (title, current_section)
    if current_section:
        sections.append((title, current_section))
    return sections

def remove_small_tag(text):
    meta_start = text.find('<small>')
    meta_end = text.find('</small>')
    if meta_start > 0 and meta_end > 0:
        meta_end += len('</small>')
        text = text[0:meta_start]+'\n\n'+text[meta_end:]
    return text

if __name__ == '__main__':
    problemList = extract_sections_from_md(f'../{sys.argv[1]}/content.md')
    for (title, problem) in problemList:
        problem = remove_small_tag(problem)
        print(problem)
        print()