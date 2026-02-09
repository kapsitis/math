import os
import sys
import re
import shutil
import glob

def parse_metadata_block(lines):
    """
    Extracts metadata from the <small>...</small> block.
    Returns the metadata dict and the lines without the block.
    """
    metadata = {}
    cleaned_lines = []
    in_small = False
    
    # regex to match metadata lines like "* key: value" or "* key:value"
    meta_regex = re.compile(r'^\s*\*\s*([^:]+):\s*(.*)$')
    
    for line in lines:
        if '<small>' in line:
            in_small = True
            continue # Skip the <small> tag line
        if '</small>' in line:
            in_small = False
            continue # Skip the </small> tag line
            
        if in_small:
            match = meta_regex.match(line)
            if match:
                key = match.group(1).strip()
                val = match.group(2).strip()
                # If value contains commas, it might be a list (like questionType)
                if ',' in val and key == 'questionType':
                     # The prompt implies questionType:Prove,FindAll -> but mostly it's single or comma separated strings.
                     # YAML handles "Prove,FindAll" as a string usually, unless list format is used.
                     # The user example showed:
                     # questionType: ProveDisprove
                     # The prompt example for list: "questionType: Prove,FindAll"
                     # The user said: "The YAML syntax could be as follows: ... questionType: ProveDisprove"
                     # But in the file we see "* questionType:Prove,FindAll"
                     # Let's keep it as is, or maybe split if it looks like a list?
                     # Simple YAML string is fine for now usually.
                     pass
                metadata[key] = val
        else:
            cleaned_lines.append(line)
            
    return metadata, cleaned_lines

def save_problem(output_dir, problem_id, content_lines):
    """
    Saves a single problem to its directory.
    """
    prob_dir = os.path.join(output_dir, problem_id)
    os.makedirs(prob_dir, exist_ok=True)
    
    # 1. Extract metadata from <small> block
    file_metadata, clean_content = parse_metadata_block(content_lines)
    
    # 2. Derive additional metadata from ID
    # ID format example: BBK2012.P1.1
    # source: BBK2012
    # year: 2012
    # regex to split ID
    # Assuming Source is everything before the first Dot.
    # And year is the 4 digits inside Source.
    
    parts = problem_id.split('.')
    source = parts[0] if parts else "Unknown"
    
    year_match = re.search(r'\d{4}', source)
    year = year_match.group(0) if year_match else ""
    
    # Construct full metadata
    meta_content = ""
    meta_content += f"id: {problem_id}\n"
    meta_content += f"source: {source}\n"
    if year:
        meta_content += f"year: {year}\n"
        
    for k, v in file_metadata.items():
        meta_content += f"{k}: {v}\n"
        
    # 3. Write meta.yml
    with open(os.path.join(prob_dir, "meta.yml"), 'w', encoding='utf-8') as f:
        f.write(meta_content)
        
    # 4. Write content_lv.md
    with open(os.path.join(prob_dir, "content_lv.md"), 'w', encoding='utf-8') as f:
        f.writelines(clean_content)

def main():
    if len(sys.argv) < 3:
        print("Usage: python split_problems.py <input_dir> <output_dir>")
        sys.exit(1)
        
    input_dir = sys.argv[1]
    output_dir = sys.argv[2]
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    content_file = os.path.join(input_dir, "content_lv.md")
    if not os.path.exists(content_file):
        print(f"Error: {content_file} not found.")
        sys.exit(1)
        
    # Copy PNGs
    print(f"Copying PNG files from {input_dir} to {output_dir}...")
    png_files = glob.glob(os.path.join(input_dir, "*.png"))
    for png in png_files:
        shutil.copy(png, output_dir)
        
    print(f"Processing {content_file}...")
    
    with open(content_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    main_content_lines = []
    current_problem_lines = []
    current_problem_id = None
    in_problem = False
    
    # Regex for problem header: # <lo-sample/> BBK2012.P1.1
    # Updated to match any lo- tag (e.g. lo-exercise)
    prob_header_regex = re.compile(r'^#\s*<lo-[^>]+/>\s*(\S+)')
    
    # Regex for any other header which terminates a problem
    # Note: A problem is followed by another problem OR by new theory snippet (H1, H2, H3...)
    # So basically any # Header starts a new block.
    # If it is <lo-sample/>, it's a new problem.
    # If it is NOT <lo-sample/>, it's theory.
    header_regex = re.compile(r'^#{1,3}\s+') 
    
    for line in lines:
        is_header = header_regex.match(line)
        prob_match = prob_header_regex.match(line)
        
        if prob_match:
            # We found a problem header
            new_problem_id = prob_match.group(1)
            
            # Save previous problem if we were in one
            if in_problem:
                save_problem(output_dir, current_problem_id, current_problem_lines)
                current_problem_lines = []
            
            # Start new problem
            in_problem = True
            current_problem_id = new_problem_id
            current_problem_lines.append(line) # Include the header in the problem file? 
            # The prompt says: "it still has the same theory snippets as before, but all the problems are now replaced by references"
            # And: "create these subdirectories... containing content_lv.md (these files are problems with their solutions)"
            # Usually the problem file DOES contain its own header to be valid markdown, or maybe not. 
            # The prompt example shows the main file having: 
            # {!BBK2012.P1.1/content_lv.md!}
            # If we include the header in the PROBLEM file, then including it back via reference might duplicate headers or be fine. 
            # The original structure had: # <lo-sample/> BBK2012...
            # The new structure replaces that block with the reference.
            # So the reference usually expands content.
            # I will include the header in the problem file so it remains self-contained.
            
            # Add reference to main content
            main_content_lines.append(f"\n{{!{new_problem_id}/content_lv.md!}}\n\n")
            
        elif is_header and in_problem:
            # Check if it is "Atrisinājums" - if so, it belongs to the problem
            if "Atrisinājums" in line:
                current_problem_lines.append(line)
            else:
                # We found a header that is NOT a problem header and NOT Atrisinājums
                # This means we encountered a Theory header while reading a Problem.
                # Save the problem and switch to normal mode.
                save_problem(output_dir, current_problem_id, current_problem_lines)
                current_problem_lines = []
                in_problem = False
                current_problem_id = None
                
                main_content_lines.append(line)
            
        else:
            # Not a header, or header handled above?
            # If prob_match was True, we processed it.
            # If is_header was True and not prob_match:
            #    If in_problem: handled above (switch to normal).
            #    If not in_problem: just append to main.
            
            if in_problem:
                current_problem_lines.append(line)
            else:
                main_content_lines.append(line)

    # End of loop. Save last problem if exists.
    if in_problem:
        save_problem(output_dir, current_problem_id, current_problem_lines)
        
    # Write main content_lv.md
    with open(os.path.join(output_dir, "content_lv.md"), 'w', encoding='utf-8') as f:
        f.writelines(main_content_lines)
        
    print("Done.")

if __name__ == '__main__':
    main()
