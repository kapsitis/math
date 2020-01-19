import csv
import json
import io
import os
import re
import requests


def get_backlinks():    
    prob_dir_lst = ['numtheory-ee-pk' ,'numtheory-ee-lo', 'numtheory-ee-lvs', 
                    'numtheory-ee-lvt', 'numtheory-ee-tst',
                'numtheory-lv-no', 'numtheory-lv-vo', 'numtheory-lv-ao', 
                'numtheory-lv-tst', 'numtheory-lv-other',
                'numtheory-lt-ljkmo', 'numtheory-lt-lkmmo', 'numtheory-lt-ldk',
                'numtheory-lt-raj', 'numtheory-lt-vilnius', 'numtheory-lt-lmmo', 
                'numtheory-lt-vumif', 'numtheory-lt-tst',
                'numtheory-bbk-p1','numtheory-bbk-p2','numtheory-bbk-p3','numtheory-bbk-p4',
                'numtheory-bbk-p5','numtheory-bbk-p6','numtheory-bbk-p7','numtheory-bbk-p8','numtheory-bbk-p9']
    result = {}
    
    cur_skill = ''
    cur_probid = ''
    for prob_dir in prob_dir_lst:
        with open('src/site/problembase/%s/content.md' % prob_dir) as prob_input:
            for prob_lin in prob_input:
                if re.match('# <lo-sample/> .*', prob_lin):
                    cur_probid = re.sub('# <lo-sample/> ([^\s]+)','\g<1>', prob_lin).strip()
                elif re.match('\* \[[^\[\]]+\]\(#\).*', prob_lin):
                    cur_skill = re.sub('\* \[([^\[\]]+)\]\(#\).*','\g<1>', prob_lin).strip()
                    if cur_skill in result: 
                        result[cur_skill].append(cur_probid)
                    else:
                        result[cur_skill] = [cur_probid]    
    return result   




def get_label_lst(lst):
    the_concat = list()
    for i in range(0,len(lst)):
        int_item = int(lst[i])
        if int_item > 0:
            the_concat.append(lst[i])
    return the_concat

def get_task_table():
    response = requests.get('https://docs.google.com/spreadsheets/d/e/2PACX-1vQvAsYeFYhuFLmLgtMiYFeQFeeO4e0DgteRXRg1zpQ2iMcWZr-mIgdyDYnh1IoKq4l5v9C-JAE1-Qcy/pub?gid=0&single=true&output=csv')
    assert response.status_code == 200, 'Wrong status code'
    response.encoding = 'utf-8'
    csv_lines = response.text.splitlines()
    tasks = csv.reader(csv_lines)
    with open('src/site/numtheory/analysis/task-analysis.csv', 'w+') as csv_out:
        for csv_line in csv_lines:
            csv_out.write(csv_line)
            csv_out.write('\n')
    csv_out.close()
    return tasks;


def get_task_table_local():
    task_lines = list()
    with open('src/site/numtheory/analysis/task-analysis.csv') as csv_in:
        for csv_line in csv_in:
            task_lines.append(csv_line)
        #csv_lines = csv_in.splitlines()
    tasks = csv.reader(task_lines)
    return tasks




def make_lst(tasks):
    task_lst = list()
    nrow = 0
    for row in tasks:
        if nrow > 0:
            task_id = row[5].strip()
            levels = get_label_lst([row[0],row[1],row[2],row[3],row[4]])
            desc = row[6]
            task_lst.append({
                'levels':levels, 
                'id':task_id, 
                'desc':desc
            })
            #out.write('<tr class="%s"><td><code>%s</code> %s</td><td>%s</td><td>%s</td></tr>\n' % (rowclass, labels, skill_id, my_esc, backLinks))
        nrow = nrow + 1
    return task_lst



def main():
    the_dir = os.getcwd()
    print('os.getcwd()="%s"' % the_dir)
    if the_dir.endswith('/src/math_py/json_data'):
        os.chdir("../../..")
        print('Changed working directory to "%s"' % os.getcwd())
    
    the_table = get_task_table()
    #the_table = get_task_table_local()
    task_lst = make_lst(the_table)
    
    
    the_dict = get_backlinks()
    print('ss = %s' % type(the_dict))
    
    found_ids = list()
    for task in task_lst:
        task_id = task['id']
        found_ids.append(task_id)
        if task_id in the_dict:
            task['problems'] = the_dict[task_id]
        else:
            task['problems']=[]
    
    
    fname = '../../workspace-new/linen-tracer-682/data/tasks.json'
    with io.open(fname, 'w', encoding='utf8') as json_file:
        json.dump(task_lst, json_file, ensure_ascii=False, sort_keys=True, indent=4)

    ## Handle tasks found in annotations, but not in the official skill list
    nfound_ids = set(the_dict.keys()).difference(set(found_ids))
    nfound_ids_sorted = list(nfound_ids)
    nfound_ids_sorted.sort()
    nfound_lst = list()
    for task_id in nfound_ids_sorted:
        nfound_lst.append({'id':task_id, 'links': the_dict[task_id]})
    fname = '../../workspace-new/linen-tracer-682/data/nfound.json'
    with io.open(fname, 'w', encoding='utf8') as json_file:
        json.dump(nfound_lst, json_file, ensure_ascii=False, sort_keys=True, indent=4)
        



if __name__ == '__main__':
    main()
    
    