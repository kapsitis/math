import csv
import io
import json
import copy
import re

from pandas_ods_reader import read_ods

def convert_file():
    ROOT = 'c:/Users/kalvis.apsitis/workspace/math/src/site'    
    path = '{}/data-structures/website-data/data-structures-topics.ods'.format(ROOT)
    
    # https://pypi.org/project/pandas-ods-reader/

    sheet_idx = 1
    df = read_ods(path, sheet_idx, columns=['Week', 'Class', 'Key', 'Value'])
    
    df.to_csv('{}/data-structures/website-data/data-structures-topics.csv'.format(ROOT), 
               index = False, header=True)

def get_csv_local():
    ROOT = 'c:/Users/kalvis.apsitis/workspace/math/src/site'
    csv_lines = list()
    path = '{}/data-structures/website-data/data-structures-topics.csv'.format(ROOT)
    with open(path, mode='r', encoding='utf-8') as csv_in:
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
    
    # Every week contains list of topics.
    empty_week = {
        'title': 'NA',
        'itemNum': 'NA',
        'links':[]
    }
    
    # One topic
    empty_topic = {
        'title': 'NA',
        'id': 'NA',
        'reading': 'NA',
        'video': [],
        'task': []
    }
    
    week_count = 0
    prev_week_id = 'W0'    
    row_count = 0
    
    for row in tasks:
        row_count += 1
        # The first row contains headers
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

        #curr_topic_id = row[1]
        if row[2] == 'id':
            week_list[len(week_list)-1]['links'].append(copy.deepcopy(empty_topic))
        curr_key = row[2]
        curr_value = row[3]
        
        # Replace stuff for MathJAX
        if curr_key == 'title' or curr_key == 'task':
            curr_value = re.sub(r'\$(.*)\$', r'<span class="math inline">\\( \1 \\)</span>', curr_value)            
        if curr_key in ['id', 'title', 'reading','video','task']:
            topWeek = week_list[len(week_list)-1]
            #print('len.topweek, rowcount = {},{}'.format(len(topWeek['links']), row_count))
            topTopic = topWeek['links'][len(topWeek['links']) - 1]
            if curr_key in ['id', 'title', 'reading']:
                topTopic[curr_key] = curr_value
            else:
                topTopic[curr_key].append(curr_value)
            
    return week_list


def main():
    convert_file()    
    ROOT = 'c:/Users/kalvis.apsitis/workspace/linen-tracer-682'
    the_table = get_csv_local()    
    week_list = make_lst(the_table)
    fname = '{}/data/data_structures_topics.json'.format(ROOT)
    with io.open(fname, 'w', encoding='utf8') as json_file:
        json.dump(week_list, json_file, ensure_ascii=False, sort_keys=True, indent=4)
    
    
if __name__ == '__main__':
    main()


