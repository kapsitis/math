import os
import re
import csv

def normalize_text(text):
    """Normalize text by removing extra whitespace."""
    if not text:
        return ""
    return " ".join(text.split())

def process_file(filepath):
    """
    Parses a content_lv.md file and extracts problem data.
    Returns a list of dictionaries with problem data.
    """
    problems = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return []

    # Regex to find problem titles
    # Example: # <lo-sample/> LV.VOL.2004.9.1
    title_pattern = re.compile(r'^# <lo-sample/>\s+(LV\.\w+\.\d+\.\d+\.\d+)', re.MULTILINE)
    
    # Split content by title to get chunks for each problem
    # The first split will be empty or pre-amble, subsequent splits will be title + content
    parts = title_pattern.split(content)
    
    # parts[0] is pre-amble/empty
    # parts[1] is first title ID
    # parts[2] is content for first problem
    # parts[3] is second title ID
    # parts[4] is content for second problem
    # ...
    
    if len(parts) < 3:
        return []

    for i in range(1, len(parts), 2):
        full_title = parts[i]
        problem_content_raw = parts[i+1]
        
        olympiad = ""
        year = ""
        grade = ""
        num = ""

        # Parse title parts
        # Format: OLYMPIAD.YEAR.GRADE.NUM
        try:
            # Regex for parsing the ID itself
            # Support LV.AMO.2014.9.1
            # But also be flexible.
            # The example was LV.VOL.2004.9.1
            # Maybe some have 3 parts?
            # Let's try splitting by dot first.
            
            # Remove any trailing dot if present
            clean_title = full_title.strip().rstrip('.')
            t_parts = clean_title.split('.')
            
            if len(t_parts) >= 4:
                # Last 3 are usually year, grade, num
                num = t_parts[-1]
                grade = t_parts[-2]
                year = t_parts[-3]
                olympiad = ".".join(t_parts[:-3])
            else:
                 print(f"Skipping malformed title structure: {full_title}")
                 continue

        except Exception as e:
            print(f"Error parsing title {full_title}: {e}")
            continue

        # Extract problem text and solution
        # Problem text is from start of content until <small> or ## Atrisinājums
        # Solution is from ## Atrisinājums until end (or next header, but we splitted by header already)
        
        # Find start of metadata or solution
        # Metadata starts with <small>
        # Solution starts with ## Atrisinājums
        
        # We need to find which comes first to chop off the problem text
        
        problem_text = ""
        solution_text = ""
        
        # Check for <small>
        small_match = re.search(r'<small>', problem_content_raw)
        solution_match = re.search(r'## Atrisinājums', problem_content_raw)
        
        problem_end_index = len(problem_content_raw)
        
        if small_match:
            problem_end_index = min(problem_end_index, small_match.start())
        if solution_match:
            problem_end_index = min(problem_end_index, solution_match.start())
            
        problem_text_raw = problem_content_raw[:problem_end_index]
        problem_text = normalize_text(problem_text_raw)
        
        # Solution text
        if solution_match:
            solution_start = solution_match.end()
            solution_content = problem_content_raw[solution_start:]
            # Solution goes until the end of this chunk.
            # But wait, next problem title (H1) starts the next chunk.
            # Is there anything else to exclude? 
            # The split by title_pattern consumes the H1 line.
            # So everything after ## Atrisinājums in this chunk is the solution.
            solution_text = normalize_text(solution_content)
        else:
            solution_text = ""

        problems.append({
            'title': full_title,
            'olympiad': olympiad,
            'year': year,
            'grade': grade,
            'num': num,
            'problem_text_ch': len(problem_text),
            'problem_solution_ch': len(solution_text)
        })

    return problems

def main():
    base_dir = "problembase" # Assuming running from root
    target_dirs = ["LV.AMO", "LV.NOL", "LV.VOL"]
    output_csv = "problem_lengths.csv"
    
    # Verify we are in the right place or find the path
    # The user instruction says "Under 'scripts/' create...". 
    # So if we run from root, problembase is at ./problembase
    
    if not os.path.exists(base_dir):
        # Maybe we are in scripts?
        if os.path.exists("../problembase"):
            base_dir = "../problembase"
            output_csv = "../problem_lengths.csv" # Or keep it in scripts?
            # User said "The script should just write this output CSV" - usually where it runs.
            # Let's assume we run it from the root of the repo as is common.
        else:
            print(f"Warning: {base_dir} not found.")

    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['title', 'olympiad', 'year', 'grade', 'num', 'problem_text_ch', 'problem_solution_ch']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for subdir in target_dirs:
            dir_path = os.path.join(base_dir, subdir)
            if not os.path.exists(dir_path):
                print(f"Directory not found: {dir_path}")
                continue
            
            for root, dirs, files in os.walk(dir_path):
                for file in files:
                    if file == "content_lv.md":
                        full_path = os.path.join(root, file)
                        print(f"Processing: {full_path}")
                        try:
                            file_problems = process_file(full_path)
                            for p in file_problems:
                                writer.writerow(p)
                        except Exception as e:
                            print(f"Failed to process {full_path}: {e}")

if __name__ == "__main__":
    main()
