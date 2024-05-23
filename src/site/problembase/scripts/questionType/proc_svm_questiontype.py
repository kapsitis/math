import re
import sys
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score


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
    text = text.lower()
    meta_start = text.find('<small>')
    if meta_start > 0:
        # meta_end = text.find('</small>')
        text = text[0:meta_start] # Nomet uzdevumam metainformāciju (un atrisinājumu, ja tāds tur ir)
        # text = text+'\n\n'+text[meta_end:]
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
    categories = ["Find.All", "Find.Count", "Find.Optimal", "Find.Example", 
                  "Prove", "ProveDisprove", "Algorithm"]

    questionType_re = re.compile(r'.+?questionType:([\w\.,]+).+?',re.DOTALL)
    problemList = extract_sections_from_md(f'../../{sys.argv[1]}/content.md')

    problem_data_set = []
    category_data_set = []
    for (title, problem) in problemList:
        category = 'NA'
        m = questionType_re.match(problem)  # Mēģina atrast questionType
        if m:
            category = m.group(1)
        
        cat_num = category_number(category)
        # print(f'{title}, {category} ({cat_num})')  # izdrukā uzdevuma ID un kategoriju
        problem = normalize_text(problem)

        if category != 'NA':
            problem_data_set.append(problem)
            category_data_set.append(cat_num)

        print(problem)
        print()


    print(f'My data lengths are {len(problem_data_set)}, {len(category_data_set)}')
    vectorizer = TfidfVectorizer()
    X_transformed = vectorizer.fit_transform(problem_data_set)

    X_train, X_test, y_train, y_test = train_test_split(X_transformed, category_data_set, test_size=0.3, random_state=42)

    model = SVC(kernel='linear')
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print(f'y_test = {y_test}')
    print(f'y_pred = {y_pred}')


