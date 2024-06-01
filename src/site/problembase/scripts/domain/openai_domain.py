import re
import sys
import os
# sys.path.append('.')
# from site.problembase.scripts.get_metadata_from_openai import *

# Get the absolute path of the directory you want to include
relative_path = ".."
absolute_path = os.path.abspath(relative_path)

# Add the absolute path to the Python path if it's not already included
if absolute_path not in sys.path:
    sys.path.append(absolute_path)

from get_metadata_from_openai import *

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
                current_section = ''
            elif current_section is not None:
                # before seeing the first title, we do not append anything
                current_section += line
    # Append the last (title, current_section)
    if current_section:
        sections.append((title, current_section))
    return sections

def normalize_text(text):
    meta_start = text.find('<small>')
    if meta_start > 0:
        # meta_end = text.find('</small>')
        text = text[0:meta_start] # Nomet uzdevumam metainformāciju (un atrisinājumu, ja tāds tur ir)
        # text = text+'\n\n'+text[meta_end:]
    return text

def main(dir_name, starting_id): 
    categories = ["Alg", "Geom", "NT", "Comb"]

    #questionType_re = re.compile(r'.+?questionType:([\w\.,]+).+?',re.DOTALL)
    metadata_re = re.compile(r'.+?domain:([\w\.,]+).+?',re.DOTALL) 
    problemList = extract_sections_from_md(f'{dir_name}/content.md')

    # prepare training data: problem_data_set un category_data_set
    problem_data_set = []
    category_data_set = []
    title_data_set = []
    found_start = (starting_id == "")

    for (title, problem) in problemList:
        found_start = found_start or (title == starting_id)
        if not found_start:
            continue

        metadata = 'NA'
        m = metadata_re.match(problem)  # Mēģina atrast metadata vērtību
        if m:
            metadata = m.group(1)
        problem = normalize_text(problem)
        
        answer = classify_math_problem(problem,'domain_LV_updated') # problem un prompt nosaukums
        with open("domain_lv_openai_temp.csv", 'a', encoding='utf-8') as file1:
            file1.write(f'{title},"{metadata}","{answer}"\n')


        if metadata != 'NA':
            problem_data_set.append(problem)
            category_data_set.append(metadata)
            title_data_set.append(title)

        print(problem)
        print()



if __name__ == '__main__':
    if len(sys.argv) < 2: 
        print("Usage: python openai_domain.py <dir_name> [<starting-id>]")
        sys.exit(0)
    else: 
        dir_name = sys.argv[1]
        starting_id = ""
        if len(sys.argv) > 2:
            starting_id = sys.argv[2]
    main(dir_name, starting_id)