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

def normalize_text(text):
    text = text.lower()
    meta_start = text.find('<small>')
    if meta_start > 0:
        meta_end = text.find('</small>')
        text = text[0:meta_start] # Nomet uzdevumam metainformāciju (un atrisinājumu, ja tāds tur ir)
        text = text+'\n\n'+text[meta_end:]
    text = re.sub(r'\$[^\$]+?\$', '_EXPR_', text)  # Aizstāj formulas ar _EXPR_
    text = re.sub(r'[^\w\s\.\?!]', '', text)  # Izdzēš simbolus, kas nav burti, cipari vai .,?,!
    text = re.sub(r'\s+', ' ', text).strip()  # Aizstāj daudzus tukšumus ar vienu tukšumu
    return text

def category_number(arg):
    categories = {'Find.All':0, 'Find.Count':1, 'Find.Optimal':2, 'Find.Example':3, 'Prove':4, 'ProveDisprove':5, 'Algorithm':6}
    if arg in categories:
        return categories[arg]
    else:
        return -1

if __name__ == '__main__':
    questionType_re = re.compile(r'.+?questionType:([\w\.,]+).+?',re.DOTALL)
    problemList = extract_sections_from_md(f'{sys.argv[1]}/content.md')
    for (title, problem) in problemList:
        category = 'NA'
        m = questionType_re.match(problem)  # Mēģina atrast questionType
        if m:
            category = m.group(1)
        
        cat_num = category_number(category)
        print(f'{title}, {category} ({cat_num})')  # izdrukā uzdevuma ID un kategoriju
        problem = normalize_text(problem)
        print(problem)
        print()

