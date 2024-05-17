import spacy
import csv
import sys
import re

# Attempt to load the spaCy model, handle the case where the model is not found
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    print("Model 'en_core_web_sm' not found. Downloading and installing...")
    from spacy.cli import download
    download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

# Hypothetical list of mathematical terms
math_terms = set([
    "geometry", "theorem", "number", "combinatorics", "angle", "vertex",
    "matrix", "equation", "integer", "prime", "composite", "factor", "polynomial"
    # Add more terms as needed
])

stop_words_lv = ["un", "vai", "bet", "kā", "arī", "par", "no", "uz", "ir", "būt", "tas", "tā", "man", "te", "es", "tikai", "ka", "bet", "lai", "kādreiz",     "pēc", "par", "pie", "viņš", "viņa", "šis", "šeit", "bet", "vēl", "tāpēc", "jo", "kamēr", "ja", "jo", "tur", "to", "aiz", "ar", "bez", "vai", "jā"]

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

with open('resources/merged_concepts.csv', newline='', encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)  # Skip the header
    for row in csv_reader:
        if row[0] != 'NA':
            math_terms.add(row[1]) # 1 for lv, 0 for eng

sorted_terms = sorted(list(math_terms))
print(sorted_terms)

def extract_keywords(doc):
    # Process the text using spaCy
    spacy_doc = nlp(doc)
    
    keywords = set()
    terms_extracted = 0
    for token in spacy_doc:
        if token.text.lower() not in stop_words_lv:  # Filter out Latvian stop words
            if token.text.lower() in math_terms: # or token.pos_ in ['NOUN', 'PROPN']:
                if terms_extracted < 5:  # Limiting to 5 terms per problem
                    keywords.add(token.text.lower())
                    terms_extracted += 1
                else:
                    break
    
    return keywords

if __name__ == '__main__':

    # Example mathematical problem
    # math_problem = "Find the prime factors of the given integer that is used in the equation."
    problemList = extract_sections_from_md(f'../{sys.argv[1]}/content.md')
    
    for title, text in problemList:
        # Extract keywords
        keywords = extract_keywords(text)
        print(f"Keywords for '{title}':", keywords)
