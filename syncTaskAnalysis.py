import shutil
import subprocess

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src', 'math_py', 'analysis'))
import sync_tasks

def main(): 
    sync_tasks.main()

if __name__ == '__main__':
    main()



