import shutil
import subprocess

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src', 'math_py'))
from prob_utils import rename_tags

def main(): 
    if len(sys.argv) != 3:
        print('Usage: python3 rename.py tag_from tag_to') 
        sys.exit(0)
    tag_from = sys.argv[1]
    tag_to = sys.argv[2]
    rename_tags.rename_all(tag_from,tag_to)

if __name__ == '__main__':
    main()



