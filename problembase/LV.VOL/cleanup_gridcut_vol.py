import os
import re

ROOT_DIR = "/Users/kapsitis/workspace-public/math/problembase/LV.VOL/"

def matched_old_criteria(text):
    has_grid = re.search(r'rūtiņ(u|as)', text, re.IGNORECASE)
    has_action = re.search(r'(sagriezt|sadalīt|izgriezt)', text, re.IGNORECASE)
    return has_grid and has_action

def matched_new_criteria(text):
    has_grid = re.search(r'rūtiņ(u|as)', text, re.IGNORECASE)
    has_cut_explicit = re.search(r'(sagriezt|izgriezt)', text, re.IGNORECASE)
    has_split = re.search(r'sadalīt', text, re.IGNORECASE)
    has_split_target = re.search(r'(daļās|gabalos|figūrās|taisnstūros|kvadrātos|trijstūros)', text, re.IGNORECASE)
    has_bad_context = re.search(r'(kartītes|skaitļus|grupās)', text, re.IGNORECASE)
    
    valid_split = has_split and has_split_target and not has_bad_context
    return has_grid and (has_cut_explicit or valid_split)

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    parts = re.split(r'(?=# <lo-sample/>)', content)
    
    new_parts = []
    modified = False
    
    for part in parts:
        if not part.strip():
            new_parts.append(part)
            continue
            
        if "subdomain:DOM_GridCut" in part:
            text_match = re.search(r'(.*?)(?=<small>)', part, re.DOTALL)
            text = text_match.group(1).strip() if text_match else part
            
            if matched_old_criteria(text) and not matched_new_criteria(text):
                print(f"Removing tag from: {os.path.basename(filepath)} - {text[:50]}...")
                new_part = re.sub(r'\n?\s*\*\s*subdomain:DOM_GridCut', '', part)
                new_parts.append(new_part)
                modified = True
            else:
                new_parts.append(part)
        else:
            new_parts.append(part)

    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write("".join(new_parts))

def main():
    for root, dirs, files in os.walk(ROOT_DIR):
        for file in files:
            if file == "content_lv.md" or file == "content.md":
                filepath = os.path.join(root, file)
                process_file(filepath)

if __name__ == "__main__":
    main()
