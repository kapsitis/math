
import json
import os
import shutil
import re

def curate_problems():
    candidates_file = 'candidates.json'
    curricula_dir = '../curricula'
    output_readme = os.path.join(curricula_dir, 'README.md')
    
    # Ensure curricula directory exists
    if not os.path.exists(curricula_dir):
        os.makedirs(curricula_dir)
        
    with open(candidates_file, 'r', encoding='utf-8') as f:
        problems = json.load(f)
        
    scored_problems = []
    
    for p in problems:
        problem_text = p.get('problem_text', '')
        solution_text = p.get('solution_text', '')
        images = p.get('images', [])
        
        # Scoring metrics
        problem_len = len(problem_text)
        solution_len = len(solution_text)
        
        # Count markdown structures in solution (lists, bolding, etc.)
        # Naive count of *, -, # characters as proxies for markdown richness
        markdown_count = solution_text.count('*') + solution_text.count('- ') + solution_text.count('#')
        
        image_count = len(images)
        
        # Calculate Score
        # Weights: Solution length and visual/structure complexity are prioritized
        score = (problem_len * 1.0) + (solution_len * 2.0) + (image_count * 500) + (markdown_count * 50)
        
        p['score'] = score
        scored_problems.append(p)
        
    # Sort by score descending
    scored_problems.sort(key=lambda x: x['score'], reverse=True)
    
    # Select top 30
    selected_problems = scored_problems[:33] # Aiming for roughly 30-33
    
    # Sort selected problems naturally by year and number for the final output, or keep ranking?
    # Usually curricula vary, but let's sort by Year/Num for coherent reading.
    selected_problems.sort(key=lambda x: (x['year'], x['num']))
    
    print(f"Selected {len(selected_problems)} problems.")
    
    readme_content = "# Izlases 9. klases matemātikas uzdevumi\n\n"
    
    for p in selected_problems:
        p_id = p['id']
        p_text = p['problem_text']
        p_images = p.get('images', [])
        
        readme_content += f"## {p_id}\n\n"
        readme_content += f"{p_text}\n\n"
        
        # Handle images
        # We need to find where the images are located.
        # Based on extract_problems.py, we know the directory structure is problembase/LV.VOL/lv-vol-YYYY/
        # But candidates.json doesn't have the full path, so we reconstruct it.
        
        year = p['year']
        src_dir = f"../problembase/LV.VOL/lv-vol-{year}"
        
        for img_name in p_images:
            src_path = os.path.join(src_dir, img_name)
            dest_path = os.path.join(curricula_dir, img_name)
            
            if os.path.exists(src_path):
                shutil.copy2(src_path, dest_path)
                # readme_content += f"![{img_name}]({img_name})\n\n" 
                # The text usually already contains ![](filename.png), so we don't need to append it again 
                # IF the problem_text includes it. 
                # extract_problems.py split problem_text before images/solution usually?
                # Let's check candidates.json content again.
                # In candidates.json, 'images' list is populated, but 'problem_text' might NOT contain the markdown image link 
                # if it was at the end of the problem or in the solution part.
                # Let's verify if image links are in problem_text.
                # Looking at view_file output of candidates.json in history:
                # "problem_text": "..." 
                # "solution_text": "... ![](LV.VOL.2019.12.2A.png)"
                # It seems images are often in the solution or at the end.
                # The goal is to show the problem statement images.
                # Only images appearing in problem_text should be rendered in the problem statement section?
                # Or should we include all images associated with the problem?
                # Typically geometry problems have an image with the statement.
                # If the image markdown is NOT in problem_text, we should probably add it.
                
                if img_name not in p_text:
                     readme_content += f"![](file://{os.path.abspath(dest_path)})\n\n"
            else:
                print(f"Warning: Image {img_name} not found at {src_path}")

        readme_content += "---\n\n"

    with open(output_readme, 'w', encoding='utf-8') as f:
        f.write(readme_content)
        
    print(f"Generated {output_readme}")

if __name__ == "__main__":
    curate_problems()
