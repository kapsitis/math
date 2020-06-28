import csv
import io
import json
import copy
import re

def get_csv_local():
    ROOT = 'c:/Users/kalvis.apsitis/workspace/math/src/site'
    csv_lines = list()
    path = '{}/data-structures/website-data/data-structures-topics.csv'.format(ROOT)
    with open(path) as csv_in:
        for csv_line in csv_in:
            csv_lines.append(csv_line)
        #csv_lines = csv_in.splitlines()
    result = csv.reader(csv_lines)
    return result


def get_schedule():
    ROOT = 'c:/Users/kalvis.apsitis/workspace/math/src/site'
    csv_lines = list()
    path = '{}/data-structures/website-data/schedule.csv'.format(ROOT)
    with open(path) as csv_in:
        for csv_line in csv_in:
            csv_lines.append(csv_line)
    result = csv.reader(csv_lines)
    return result

def make_lst(tasks):
    week_csv = get_schedule()
    week_dict = dict()
    for wweek in week_csv:
        curr_week = wweek[0].strip()
        curr_val = wweek[1].strip()
        week_dict[curr_week] = curr_val
    
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
    ROOT = 'c:/Users/kalvis.apsitis/workspace/linen-tracer-682'
    the_table = get_csv_local()    
    week_list = make_lst(the_table)
    fname = '{}/data/data_structures_topics.json'.format(ROOT)
    with io.open(fname, 'w', encoding='utf8') as json_file:
        json.dump(week_list, json_file, ensure_ascii=False, sort_keys=True, indent=4)
    
    
if __name__ == '__main__':
    main()


