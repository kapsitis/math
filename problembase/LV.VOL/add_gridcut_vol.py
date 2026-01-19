import os
import re

ROOT_DIR = "/Users/kapsitis/workspace-public/math/problembase/LV.VOL/"

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
            new_parts.append(part)
            continue
            
        has_rutinu = re.search(r'rūtiņ(u|as)', part, re.IGNORECASE)
        has_action = re.search(r'(sagriezt|sadalīt|izgriezt)', part, re.IGNORECASE)
        
        if has_rutinu and has_action:
            small_match = re.search(r'<small>(.*?)</small>', part, re.DOTALL)
            if small_match:
                new_part = re.sub(r'(<small>.*?)(\n\s*</small>)', r'\1\n* subdomain:DOM_GridCut\2', part, flags=re.DOTALL)
                if new_part == part:
                     new_part = part.replace("</small>", "* subdomain:DOM_GridCut\n</small>")
                new_parts.append(new_part)
                modified = True
                print(f"Marking problem in {os.path.basename(filepath)}")
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
