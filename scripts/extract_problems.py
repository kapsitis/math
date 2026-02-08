import os
import re
import json

def extract_problems():
    base_dir = '/Users/kapsitis/workspace-public/math/problembase/LV.VOL'
    output_file = 'candidates.json'
    problems = []

    # Regex to match the problem header
    # Example: # <lo-sample/> LV.VOL.2016.9.1 or 10.1 or 9.5
    # Matches LV.VOL.YYYY.Grade.Num
    header_pattern = re.compile(r'^#\s*<lo-sample/>\s*(LV\.VOL\.(\d{4})\.(\d+)\.(\d+))\s*$')
    
    for year in range(2004, 2026):
        dir_name = f"lv-vol-{year}"
        file_path = os.path.join(base_dir, dir_name, "content_lv.md")
        
        if not os.path.exists(file_path):
            print(f"File not found: {file_path}")
            continue
            
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        current_problem = None
        buffer = []
        
        for line in lines:
            match = header_pattern.match(line)
            if match:
                # If we were tracking a problem, save it
                if current_problem:
                    current_problem['full_content'] = "".join(buffer)
                    problems.append(current_problem)
                
                # Start new problem
                problem_id = match.group(1)
                problem_year = int(match.group(2))
                problem_grade = int(match.group(3))
                problem_num = int(match.group(4))
                
                if problem_grade == 9 and problem_num <= 5: 
                    # Only keep Grade 9, first 5 problems
                    # Although user requirements said "extract Grade 9 problems (first 5 per year)"
                    # Usually there are only 5 problems per grade in these files, but let's be safe.
                    
                    current_problem = {
                        "id": problem_id,
                        "year": problem_year,
                        "num": problem_num,
                        "full_content": ""
                    }
                else:
                    current_problem = None
                    
                buffer = []
            elif current_problem:
                buffer.append(line)
        
        # Save the last problem if it was relevant
        if current_problem:
            current_problem['full_content'] = "".join(buffer)
            problems.append(current_problem)

    # Now process the content to separate problem text, images and solution
    # Problem text is everything before <small> or ## Atrisinājums
    processed_problems = []
    
    for p in problems:
        content = p['full_content']
        
        # Extract images
        # Format: ![](filename.png)
        images = re.findall(r'!\[.*?\]\((.*?\.png)\)', content)
        p['images'] = images
        
        # Split into problem text vs solution/metadata
        # Find first occurrence of <small> or ## Atrisinājums
        # We want the text for the problem statement
        
        split_markers = [content.find('<small>'), content.find('## Atrisinājums')]
        split_markers = [x for x in split_markers if x != -1]
        
        if split_markers:
            split_idx = min(split_markers)
            problem_text = content[:split_idx].strip()
            solution_text = content[split_idx:].strip()
        else:
            problem_text = content.strip()
            solution_text = ""
            
        p['problem_text'] = problem_text
        p['solution_text'] = solution_text # useful for difficulty judging
        del p['full_content']
        
        processed_problems.append(p)

    print(f"Found {len(processed_problems)} problems.")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(processed_problems, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    extract_problems()
