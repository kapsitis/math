import json
import io
import os
import re

from prob_utils import id_util


def robust_add(kkey,vval,mmap):
    if kkey in mmap:
        mmap[kkey].append(vval)
    else:
        mmap[kkey] = [vval]

def robust_add_all(kkey,vvals, mmap):
    vval_lst = vvals.split(',')
    for vval in vval_lst:
        robust_add(kkey,vval,mmap)

## seeAlso "get_backlinks()"
## This is similar, but the dictionary is built in the opposite direction:
## Problems -> Tasks
def get_prob_tasks():
    prob_dir_lst = id_util.get_problem_dir_list()    
#     prob_dir_lst = ['numtheory-ee-pk' ,'numtheory-ee-lo', 'numtheory-ee-lvs-lvt', 
#                 'numtheory-lv-no', 'numtheory-lv-vo', 'numtheory-lv-ao', 
#                 'numtheory-lt-lkmmo', 'numtheory-lt-ldk',
#                 'numtheory-lt-raj',  'numtheory-lt-lmmo', 'numtheory-lt-vumif',
#                 'numtheory-bbk-p1','numtheory-bbk-p2','numtheory-bbk-p3','numtheory-bbk-p4'
#                 ]
    
    ## List of problems with all sorts of metadata
    result = list()
    
    prob_id_lst = []
    tasks_map = {}
    qtypes_map = {}
    seealso_map = {}
    genre_map = {}
    concepts_map = {}
    
    cur_skill = ''
    cur_probid = ''
    
    for prob_dir in prob_dir_lst:
        with open('src/site/prob/%s/content.md' % prob_dir) as prob_input:
            for prob_lin in prob_input:
                if re.match('^# <lo-sample/> .*', prob_lin):
                    cur_probid = re.sub('# <lo-sample/> ([^\s]+)','\g<1>', prob_lin).strip()
                    prob_id_lst.append(cur_probid)
                elif re.match('^\* \[[^\[\]]+\]\(#\).*', prob_lin):
                    cur_skill = re.sub('\* \[([^\[\]]+)\]\(#\).*','\g<1>', prob_lin).strip()
                    robust_add(cur_probid,cur_skill,tasks_map)
                elif re.match('^seeAlso=(.+)', prob_lin):
                    cur_seealso = re.sub('seeAlso=(.+)','\g<1>', prob_lin).strip()
                    robust_add(cur_probid,cur_seealso,seealso_map)
                elif re.match('^questionType=(.+)',prob_lin):
                    cur_qtypes = re.sub('questionType=(.+)','\g<1>', prob_lin).strip()
                    robust_add_all(cur_probid,cur_qtypes,qtypes_map)
                elif re.match('^genre=(.+)',prob_lin):
                    cur_genre = re.sub('genre=(.+)','\g<1>', prob_lin).strip()
                    robust_add(cur_probid,cur_genre,genre_map)
                elif re.match('^concepts=(.+)',prob_lin):
                    cur_concepts = re.sub('concepts=(.+)','\g<1>', prob_lin).strip()
                    robust_add_all(cur_probid,cur_concepts,concepts_map)
    for prob_id in prob_id_lst:
        item = {'id': prob_id}
        if prob_id in tasks_map:
            item['tasks'] = tasks_map[prob_id]
        else: 
            item['tasks'] = []
        if prob_id in qtypes_map:
            item['qtypes'] = qtypes_map[prob_id]    
        else:
            item['qtypes'] = []
        if prob_id in seealso_map:
            item['seeAlso'] = seealso_map[prob_id]
        else:
            item['seeAlso'] = []
        if prob_id in genre_map:
            item['genre'] = genre_map[prob_id]
        else:
            item['genre'] = []
        if prob_id in concepts_map:
            item['concepts'] = concepts_map[prob_id]
        else:
            item['concepts'] = []
        result.append(item)
    return result   



### This file is meant to record metadata (markings/skills)
### about the problems. Problem content is NOT written for now. 

def main():
    the_dir = os.getcwd()
    print('os.getcwd()="%s"' % the_dir)
    if the_dir.endswith('/src/math_py/json_data'):
        os.chdir("../../..")
        print('Changed working directory to "%s"' % os.getcwd())
    
    the_prob_dict = get_prob_tasks()    
    fname = '../../workspace-new/linen-tracer-682/data/problems.json'
    with io.open(fname, 'w', encoding='utf8') as json_file:
        json.dump(the_prob_dict, json_file, ensure_ascii=False, sort_keys=True, indent=4)





if __name__ == '__main__':
    main()
    
    