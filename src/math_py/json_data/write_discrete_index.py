import csv
import io
import json
import copy
import re

def get_csv_local():
    csv_lines = list()
    with open('/home/kalvis/workspace/math/src/site/discrete/static/website-data/discrete-index.csv') as csv_in:
        for csv_line in csv_in:
            csv_lines.append(csv_line)
        #csv_lines = csv_in.splitlines()
    result = csv.reader(csv_lines)
    return result


def make_lst(tasks):
    week_dict = {
        'W1': '2020-01-06 to 2020-01-10',
        'W2': '2020-01-13 to 2020-01-17',
        'W3': '2020-01-20 to 2020-01-24',
        'W4': '2020-01-27 to 2020-01-31',      
        'W5': '2020-02-03 to 2020-02-07',
        'W6': '2020-02-10 to 2020-02-14',
        'W7': '2020-02-17 to 2020-02-21',
        'W8': '2020-02-24 to 2020-02-28',       
        'W9': '2020-03-02 to 2020-03-06',
        'W10': '2020-03-09 to 2020-03-13',
        'W11': '2020-03-16 to 2020-03-20',
        'W12': '2020-03-23 to 2020-03-27',        
        'W13': '2020-03-30 to 2020-04-03',
        'W14': '2020-04-06 to 2020-04-17',
        'W15': '2020-04-20 to 2020-01-24',
        'W16': '2020-04-27 to 2020-01-31'        
    }
    
    week_list = []
    
    empty_week = {
        'title': 'NA',
        'itemNum': 'NA',
        'links':[]
    }
    
    empty_topic = {
        'title': 'NA',
        'subsection': 'NA',
        'reading': 'NA',
        'video': [],
        'task': []
    }
    
    week_count = 0
    prev_week_id = 'W0'    
    row_count = 0
    
    for row in tasks:
        row_count += 1
        if row_count == 1:
            continue
        curr_week = row[0].strip()
        if curr_week != prev_week_id:
            week_count += 1
            week_list.append(copy.deepcopy(empty_week))
            topWeek = week_list[len(week_list)-1]
            if curr_week in week_dict:
                topWeek['title'] = week_dict[curr_week]
            else:
                topWeek['title'] = 'NA'
            topWeek['itemNum'] = week_count
            prev_week_id = curr_week
            prev_topic_id = '0'

        curr_topic_id = row[1]
        if curr_topic_id != prev_topic_id:
            week_list[len(week_list)-1]['links'].append(copy.deepcopy(empty_topic))
            prev_topic_id = curr_topic_id
        curr_key = row[2]
        curr_value = row[3]
        if curr_key == 'title' or curr_key == 'task':
            curr_value = re.sub(r'\$(.*)\$', r'<span class="math inline">\\( \1 \\)</span>', curr_value)
            #print('transformed to {}'.format(curr_value))
        if curr_key in ['subsection', 'title', 'reading','video','task']:
            topWeek = week_list[len(week_list)-1]
            topTopic = topWeek['links'][len(topWeek['links']) - 1]
            if curr_key in ['subsection', 'title', 'reading']:
                topTopic[curr_key] = curr_value
            else:  
                topTopic[curr_key].append(curr_value)
            
    return week_list


def main():
    the_table = get_csv_local()    
    week_list = make_lst(the_table)
    fname = '/home/kalvis/workspace-new/linen-tracer-682/data/discrete_index.json'
    with io.open(fname, 'w', encoding='utf8') as json_file:
        json.dump(week_list, json_file, ensure_ascii=False, sort_keys=True, indent=4)
    
    
if __name__ == '__main__':
    main()


