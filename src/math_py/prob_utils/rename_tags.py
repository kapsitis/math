import os
import re
import shutil
import sys
from prob_utils import id_util


## 
# Replace tag_from by tag_to in all problem files
##
def rename_all(tag_from,tag_to):
    the_dir = os.getcwd()
    if the_dir.endswith('/src/math_py/prob_utils'):
        os.chdir("../../..")
        print('Changed working directory to "%s"' % os.getcwd())


    prob_dir_lst = id_util.get_problem_dir_list()
    for prob_dir in prob_dir_lst:
        result_lines = list()
        found_tags = 0
        with open('src/site/prob/%s/content.md' % prob_dir) as prob_input:
            for prob_lin in prob_input:
                if re.match('^\* \[[^\[\]]+\]\(#\).*', prob_lin):
                    cur_skill = re.sub('\* \[([^\[\]]+)\]\(#\).*','\g<1>', prob_lin).strip()
                    if cur_skill == tag_from:
                        found_tags += 1
                        prob_lin = prob_lin.replace(tag_from, tag_to, 1)
                result_lines.append(prob_lin)
        if found_tags > 0:
            print('Found and replaced %d tags in %s' % (found_tags,prob_dir))
            with open('src/site/prob/%s/content2.md' % prob_dir, mode='wt', encoding='utf-8') as out_file:
                out_file.write(''.join(result_lines))
            os.rename('src/site/prob/%s/content.md' % prob_dir, 'src/site/prob/%s/content.md.bak' % prob_dir)
            os.rename('src/site/prob/%s/content2.md' % prob_dir, 'src/site/prob/%s/content.md' % prob_dir)




