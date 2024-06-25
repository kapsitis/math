import re
import sys
import os

relative_paths = ['.', '..']

for relative_path in relative_paths:
    absolute_path = os.path.abspath(relative_path)
    if absolute_path not in sys.path:
        sys.path.append(absolute_path)

from translate-md import extract_sections_from_md

def main():
    if len(sys.argv) < 2: 
        print('Usage: python check_md_structure.py <dirname>')
    problem_text = extract_sections_from_md(args[1])
    



if __name__ == '__main__':
    main()

