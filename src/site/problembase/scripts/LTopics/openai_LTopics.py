import re
import os
import sys
#sys.path.append('.')
#from site.problembase.scripts.get_metadata_from_openai import *

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
        text = text[0:meta_start] # Nomet uzdevumam metainformāciju (un atrisinājumu, ja tāds tur ir)
    return text


if __name__ == '__main__':

    categories = ["LTDivisibility", "LTPrimeFactors", "LTNumeralSystems", "LTCongruenceModulo", "LTTransformsNumTheory", "LTInequalitiesNumTheory", "LTEquationsNumTheory", "LTNumTheoryByCases", "LTNumTheoryExamples", "LTIntegerPolynomials"]

    methods = ["LTInduction", "LTExtremeElement", "LTMeanValuePrinciple", "LTInvariant", "LTContradiction", "LTInterpretation", "LTExpressionTransforms", "LTStructureAugmentation"]

    #questionType_re = re.compile(r'.+?questionType:([\w\.,]+).+?',re.DOTALL)
    concept_re = re.compile(r'.+?LTopic:([\w\.,]+).+?',re.DOTALL) 
    problemList = extract_sections_from_md(f'../{sys.argv[1]}/content.md')

    # prepare training data: problem_data_set un category_data_set
    problem_data_set = []
    category_data_set = []
    title_data_set = []
    methods_data_set = []
    for (title, problem) in problemList:
        category = 'NA'
        m = concept_re.match(problem)  # Mēģina atrast questionType
        if m:
            category = m.group(1)
        problem = normalize_text(problem)
        
        answer = classify_math_problem(problem,'LTopics_EN') # problem un prompt nosaukums
        with open("LTopics_EN_openai.csv", 'a', encoding='utf-8') as file1:
            file1.write(f'{title},"{category}","{answer}", "{methods}"\n')


        if category != 'NA':
            problem_data_set.append(problem)
            category_data_set.append(category)
            title_data_set.append(title)

        print(problem)
        print()
