import os
import re

ROOT_DIR = "/Users/kapsitis/workspace-public/math/problembase/LV.AMO/"

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by problem header
    # We want to keep the delimiters to reconstruct the file later if needed, 
    # but for regex replacement it might be easier to process the whole string 
    # if we are careful about boundaries. 
    # However, each problem has its own <small> block.
    
    # Strategy: Find all <lo-sample/> blocks and process them individually? 
    # Or just iterate through the file line by line?
    # Iterate by blocks usually safer for context.
    
    # We can split by "# <lo-sample/>". 
    # But files start with one.
    
    parts = re.split(r'(?=# <lo-sample/>)', content)
    
    new_parts = []
    modified = False
    
    for part in parts:
        if not part.strip():
            new_parts.append(part)
            continue
            
        # Check if already has marking
        if "subdomain:DOM_GridCut" in part:
            new_parts.append(part)
            continue
            
        # Check for keywords
        # Must contain "rūtiņu" OR "rūtiņas"
        # AND "sagriezt" OR "sadalīt" OR "izgriezt"
        
        has_rutinu = re.search(r'rūtiņ(u|as)', part, re.IGNORECASE)
        has_action = re.search(r'(sagriezt|sadalīt|izgriezt)', part, re.IGNORECASE)
        
        if has_rutinu and has_action:
            # Check context - crude check: are they in lines before <small>?
            # We assume the problem statement is before <small>
            
            small_match = re.search(r'<small>(.*?)</small>', part, re.DOTALL)
            if small_match:
                # Add marking
                # insert before </small>
                # We want to insert "* subdomain:DOM_GridCut\n" before the closing tag, 
                # maintaining indentation if possible or just newline.
                
                # Check if indentation is used. usually just a list.
                
                replacement = r'\1* subdomain:DOM_GridCut\n</small>'
                new_part = re.sub(r'(<small>.*?)(\n\s*</small>)', r'\1\n* subdomain:DOM_GridCut\2', part, flags=re.DOTALL)
                
                # If regex didn't match (maybe no newline before </small>), try simpler
                if new_part == part:
                     new_part = part.replace("</small>", "* subdomain:DOM_GridCut\n</small>")
                
                new_parts.append(new_part)
                modified = True
                print(f"Marking problem in {filepath}")
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
