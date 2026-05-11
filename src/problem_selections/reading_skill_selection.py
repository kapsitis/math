import sys
import os
import re
import shutil

def main():
    if len(sys.argv) != 3:
        print("Usage: python reading_skill_selection.py <grades_comma_separated> <output_directory>")
        sys.exit(1)

    grades = sys.argv[1].split(',')
    output_dir = sys.argv[2]

    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_file_path = os.path.join(output_dir, 'content.md')
    
    # Ensure the output file is empty initially
    with open(output_file_path, 'w', encoding='utf-8') as f:
        pass

    # We visit problembase/LV.AMO and problembase/LV.NOL
    base_dirs = ['problembase/LV.AMO', 'problembase/LV.NOL']
    
    for base_dir in base_dirs:
        if not os.path.exists(base_dir):
            continue
            
        for root, dirs, files in os.walk(base_dir):
            if 'content_lv2.md' in files:
                file_path = os.path.join(root, 'content_lv2.md')
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                parts = content.split('# <lo-sample/> ')
                for part in parts[1:]:
                    part = '# <lo-sample/> ' + part
                    
                    # Look for the title line
                    first_line_end = part.find('\n')
                    if first_line_end == -1:
                        continue
                    
                    title_line = part[:first_line_end].strip()
                    title_parts = title_line.split()
                    if len(title_parts) < 3:
                        continue
                        
                    problem_id = title_parts[-1]
                    id_parts = problem_id.split('.')
                    if len(id_parts) < 2:
                        continue
                        
                    # Next to last part is the grade
                    grade = id_parts[-2]
                    
                    if grade not in grades:
                        continue
                        
                    # Check readingDifficulty
                    small_start = part.find('<small>')
                    small_end = part.find('</small>')
                    
                    if small_start == -1 or small_end == -1:
                        continue
                        
                    metadata_section = part[small_start:small_end]
                    if '* _readingDifficulty: high' not in metadata_section:
                        continue
                        
                    # Extract the snippet (title and problem text, no <small> portion)
                    snippet = part[:small_start].rstrip()
                    
                    with open(output_file_path, 'a', encoding='utf-8') as f:
                        f.write(snippet + '\n\n')
                        
                    # Also find PNGs referenced in this snippet and copy them
                    images = re.findall(r'!\[.*?\]\((.*?\.png)\)', snippet)
                    for img in images:
                        img_path = os.path.join(root, img)
                        if os.path.exists(img_path):
                            shutil.copy(img_path, os.path.join(output_dir, img))
                            
                    # Explicitly copy problem_id.png if it exists as requested
                    explicit_img_path = os.path.join(root, f"{problem_id}.png")
                    if os.path.exists(explicit_img_path):
                        shutil.copy(explicit_img_path, os.path.join(output_dir, f"{problem_id}.png"))

if __name__ == '__main__':
    main()
