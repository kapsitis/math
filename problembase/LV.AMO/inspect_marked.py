import os
import re

ROOT_DIR = "/Users/kapsitis/workspace-public/math/problembase/LV.AMO/"

def inspect_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    parts = re.split(r'(?=# <lo-sample/>)', content)
    
    for part in parts:
        if not part.strip():
            continue
            
        if "subdomain:DOM_GridCut" in part:
            # Extract title
            title_match = re.search(r'# <lo-sample/> (.*)', part)
            title = title_match.group(1).strip() if title_match else "Unknown"
            
            # Extract problem text (up to <small>)
            text_match = re.search(r'(.*?)(?=<small>)', part, re.DOTALL)
            text = text_match.group(1).strip() if text_match else part
            
            # Highlight keywords
            has_rutinu = re.search(r'rūtiņ(u|as)', text, re.IGNORECASE)
            has_action = re.search(r'(sagriezt|sadalīt|izgriezt)', text, re.IGNORECASE)
            
            print(f"File: {os.path.basename(filepath)}")
            print(f"Problem: {title}")
            print(f"Keywords found: {'rūtiņu' if has_rutinu else ''} {'Action' if has_action else ''}")
            # Print snippet with keywords
            print("-" * 20)
            print(text[:300] + "...")
            print("=" * 40)

def main():
    for root, dirs, files in os.walk(ROOT_DIR):
        for file in files:
            if file == "content_lv.md" or file == "content.md":
                filepath = os.path.join(root, file)
                inspect_file(filepath)

if __name__ == "__main__":
    main()
