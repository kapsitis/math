import spacy

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

def extract_keywords(doc):
    # Process the text using spaCy
    spacy_doc = nlp(doc)
    
    # Extract noun phrases and mathematical terms
    keywords = set()
    for token in spacy_doc:
        if token.text.lower() in math_terms or token.pos_ in ['NOUN', 'PROPN']:
            keywords.add(token.text.lower())
    
    return keywords

# Example mathematical problem
math_problem = "Find the prime factors of the given integer that is used in the equation."

# Extract keywords
keywords = extract_keywords(math_problem)
print("Keywords:", keywords)