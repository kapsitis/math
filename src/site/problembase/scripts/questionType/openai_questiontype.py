# -*- coding: utf-8 -*-
import re
import sys
#sys.path.append('.')
#from site.problembase.scripts.get_metadata_from_openai import *
sys.path.append('..')
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

# def category_number(arg):
#     categories = {'Find.All':0, 'Find.Count':1, 'Find.Optimal':2, 'Find.Example':3, 'Prove':4, 'ProveDisprove':5, 'Algorithm':6}
#     if arg in categories:
#         return categories[arg]
#     else:
#         return -1

if __name__ == '__main__':
     categories = ["Find.All", "Find.Count", "Find.Optimal", "Find.Example", 
                  "Prove", "ProveDisprove", "Algorithm"]

questionType_re = re.compile(r'.+?questionType:([\w\.,]+).+?',re.DOTALL)
#problemList = extract_sections_from_md(f'../{sys.argv[1]}/content.md')
problemList = extract_sections_from_md('../../workspace-private/nms-uzdevumi/lv-vol-2019/content.md')

# prepare training data: problem_data_set un category_data_set
problem_data_set = []
category_data_set = []
title_data_set = []
for (title, problem) in problemList:
    category = 'NA'
    m = questionType_re.match(problem)  # Mēģina atrast questionType
    if m:
        category = m.group(1)
    problem = normalize_text(problem)
    
    answer = classify_math_problem(problem,'questionType_LV') # problem un prompt nosaukums
    with open("questiontype_openai-17.csv", 'a', encoding='utf-8') as file1:
        file1.write(f'{title},"{category}","{answer}"\n')


    if category != 'NA':
        problem_data_set.append(problem)
        category_data_set.append(category)
        title_data_set.append(title)

    print(problem)
    print()
