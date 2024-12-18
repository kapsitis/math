import csv
import io
import json
import copy
import re

from pandas_ods_reader import read_ods
import time
from datetime import date
from datetime import timedelta





# SUBDIR = 'algorithms'
# SUBFILE = 'algorithms-topics'
# JSON_FILE = 'algorithms_topics.json'
# MODULES_FILE = 'algorithms_modules.json'
# FIRST_YEAR = 2020
# FIRST_MONTH = 9
# FIRST_DATE = 7

#SUBDIR = 'data-structures'
#SUBFILE = 'data-structures-topics'
#JSON_FILE = 'data_structures_topics.json'
#MODULES_FILE = 'data_structures_modules.json'
#FIRST_YEAR = 2020
#FIRST_MONTH = 8
#FIRST_DATE = 31

SUBDIR = 'discrete2021'
SUBFILE = 'topics-tasks-discrete-math'
JSON_FILE = 'discrete2021_topics.json'
MODULES_FILE = 'discrete2021_modules.json'
WEEK_LIST = 'schedule-spring-2021.csv'
FIRST_YEAR = 2021
FIRST_MONTH = 1
FIRST_DATE = 4

STATIC_ROOT = 'c:/Users/kalvis.apsitis/workspace/math/src/site'
MODULES_PATH = '{}/{}/website-data/modules-weeks.csv'.format(STATIC_ROOT,SUBDIR)
SCHEDULE_PATH = '{}/{}/website-data/{}'.format(STATIC_ROOT,SUBDIR,WEEK_LIST)
TOPICS_PATH = '{}/{}/website-data/{}.csv'.format(STATIC_ROOT,SUBDIR,SUBFILE)

OUT_ROOT = 'c:/Users/kalvis.apsitis/workspace/linen-tracer-682'



def get_csv_from_path(filePath):
    csv_lines = list()
    with open(filePath, mode='r', encoding='utf-8') as csv_in:
        for csv_line in csv_in:
            if csv_line.strip() == '':
                print('Skipping \' \' in \'{}\''.format(filePath))
            elif csv_line.startswith('#'):
                print('Skipping \'#\' in \'{}\''.format(filePath))
            else:
                csv_lines.append(csv_line)
    result = csv.reader(csv_lines)
    return result




def make_topic_list(tasks):
    week_csv = get_csv_from_path(SCHEDULE_PATH)
    week_dict = dict()
    for wweek in week_csv:
        curr_week = wweek[0].strip()
        curr_val = wweek[1].strip()
        week_dict[curr_week] = curr_val    
    week_list = []

    module_week_csv = get_csv_from_path(MODULES_PATH)
    module_week_dict = dict()
    #linecount = 1
    for mod_week in module_week_csv:
        #print('Processing mod_week line {}'.format(linecount))
        #linecount += 1
        curr_key = mod_week[0].strip()
        curr_val = mod_week[1].strip()
        module_week_dict[curr_key] = curr_val
    
    # Every week contains list of topics.
    empty_week = {
        'title': 'NA',
        'itemNum': 'NA',
        'links':[],
        'objectives':[]
    }
    
    # One topic
    empty_topic = {
        'title': 'NA',
        'id': 'NA',
        'description': 'NA',
        'readings': [],
        'videos': [],
        'tasks': []
    }
    
    empty_task1 = {
        'title': 'NA',
        'maths': [],
        'subtasks': [],
        'examples': [],
        'description': 'NA'
    }
    
    
    week_count = 0
    prev_week_id = 'W0'
    curr_week = 'W1'
    row_count = 0
    
    for row in tasks:
        row_count += 1
        # The first row contains headers
        if row_count == 1:
            continue

        #curr_tree_id = row[0].strip()
        #curr_key = row[1].strip()
        #curr_value = row[2].strip()
        curr_tree_id = row[1].strip()
        curr_key = row[2].strip()
        curr_value = row[3].strip()
        
        new_tree_id = curr_tree_id
        if re.match(r'^[0-9]+$', curr_tree_id):
            new_tree_id = '{}.1'.format(curr_tree_id)
        if re.match(r'^[0-9]+\.[0-9]+$', new_tree_id):
            curr_week = module_week_dict[new_tree_id]
        
        #print('curr_week, prev_week = {},{}'.format(curr_week, prev_week_id))
        if curr_week != prev_week_id:
            week_count += 1
            #print('Appending new week on {}; curr/prev = {}/{}'.format(row_count, curr_week, prev_week_id))
            week_list.append(copy.deepcopy(empty_week))
            topWeek = week_list[len(week_list)-1]
            if curr_week in week_dict:
                topWeek['title'] = week_dict[curr_week]
            else:
                topWeek['title'] = 'NA'
            topWeek['itemNum'] = week_count
            prev_week_id = curr_week
            #prev_topic_id = '0'
      
        if curr_key == 'topic' and re.match(r'^[0-9]+$', curr_tree_id):
            week_list[len(week_list)-1]['links'].append({'title':curr_value, 'topic':curr_tree_id})
        
        if curr_key == 'task' and re.match(r'^[0-9]+\.[0-9]+$', curr_tree_id):
            week_list[len(week_list)-1]['links'].append(copy.deepcopy(empty_topic))
        
        # Replace stuff for MathJAX
        if curr_key == 'title' or curr_key == 'task' or curr_key == 'description' or curr_key == 'example' or curr_key == 'math':
            curr_value = re.sub(r'\$([^\$]*)\$', r'<span class="math inline">\\( \1 \\)</span>', curr_value)            
        
        # Skip the top-level topics for now
        #if curr_key == 'topic':
        #    ii = 17        
        if curr_key in ['description','reading','video','task','example','math','objective']:
            # Skip some very high level topics
            if re.match(r'^[0-9]+$', curr_tree_id):
                continue
            topWeek = week_list[len(week_list)-1]
            #print('len.week_list, len.topweek, rowcount = {},{},{},{}'.format(len(week_list), len(topWeek['links']), row_count, curr_value))
            topTopic = topWeek['links'][len(topWeek['links']) - 1]
            if curr_key in ['reading']:
                m = re.search('^([^\(\)]+)\s+(\([^\(\)]+\))\s+(.+)$', curr_value)
                #m1 = re.search('^CH\d\dP\d\d$', curr_value)
                if m:
                    readingLink = {'url': m.group(1).strip(), 'ref': m.group(2).strip(), 'title': m.group(3).strip() }            
                    topTopic['readings'].append(readingLink)
                elif curr_value == 'NA':
                    print('Skipping reading on {}'.format(row_count))
                else:
                    print('ERROR on {}: Wrong reading format'.format(row_count))            
            elif curr_key == 'objective':
                print('**************** {} *****************'.format(curr_value))
                #topTopic['objectives'].append(curr_value)
                topWeek['objectives'].append(curr_value)
            elif curr_key in ['video']:
                m = re.search('^([^\(\)]+)\s+(\([^\(\)]+\))\s+(.+)$', curr_value)
                if m:
                    readingLink = {'url': m.group(1).strip(), 'ref': m.group(2).strip(), 'title': m.group(3).strip() }            
                    topTopic['videos'].append(readingLink)
                elif curr_value == 'NA':
                    print('Skipping video on {}'.format(row_count))
                else:
                    print('ERROR on {}: Wrong video format'.format(row_count))
            elif curr_key == 'task' and re.match(r'^[0-9]+\.[0-9]+$', curr_tree_id):
                topTopic['id'] = curr_tree_id
                topTopic['title'] = curr_value
            elif curr_key == 'description' and re.match(r'^[0-9]+\.[0-9]+$', curr_tree_id):
                topTopic['description'] = curr_value 
            elif curr_key == 'task' and re.match(r'^[0-9]+\.[0-9]+\.[0-9]+$', curr_tree_id):
                #week_list[len(week_list)-1]['links'].append(copy.deepcopy(empty_topic))
                topTopic['tasks'].append(copy.deepcopy(empty_task1))
                topSubtopic = topTopic['tasks'][len(topTopic['tasks']) - 1]
                topSubtopic['title'] = curr_value
            elif curr_key == 'description' and re.match(r'^[0-9]+\.[0-9]+\.[0-9]+$', curr_tree_id):
                topSubtopic['description'] = curr_value
            elif curr_key == 'task' and re.match(r'^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$', curr_tree_id):
                #ii = 1
                topSubtopic = topTopic['tasks'][len(topTopic['tasks']) - 1]
                topSubtopic['subtasks'].append({ 'title': curr_value })
            elif curr_key == 'example' and re.match(r'^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$', curr_tree_id):
                #ii = 1
                topSubtopic = topTopic['tasks'][len(topTopic['tasks']) - 1]
                topSubtopic['examples'].append({ 'title': curr_value })
            elif curr_key == 'math' and re.match(r'^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$', curr_tree_id):
                #ii = 1
                topSubtopic = topTopic['tasks'][len(topTopic['tasks']) - 1]
                topSubtopic['maths'].append({ 'title': curr_value })      
    return week_list


def main():
    topics_table = get_csv_from_path(TOPICS_PATH)    
    week_list = make_topic_list(topics_table)
    fname = '{}/data/{}'.format(OUT_ROOT,JSON_FILE)
    with io.open(fname, 'w', encoding='utf8') as json_file:
        json.dump(week_list, json_file, ensure_ascii=False, sort_keys=True, indent=4)

    module_list = list()    
    modules_weeks = get_csv_from_path(MODULES_PATH)
    
    
    module_week = list()
    prev_week = 'W0'
    curr_week = 'W1'
    
    first_date = date(FIRST_YEAR,FIRST_MONTH,FIRST_DATE)
    week_count = 0
    for module in modules_weeks:
        curr_week = module[1].strip()
        if curr_week != prev_week:
            if len(module_week) > 0:
                module_list.append(module_week)
                week_count += 1
            module_week = list()
        
        thedelta = timedelta(days=7*week_count)
        new_date = first_date + thedelta
        end_date = new_date + timedelta(days=4)
        
        item = {
            'subid':module[0].strip(),
            'week':module[1].strip(),
            'part':module[2].strip(),
            'title':module[3].strip(),
            'subdir':module[4].strip(),
            'show':module[5].strip(),
            'date':new_date.strftime("%Y-%m-%d"),
            'endDate':end_date.strftime("%Y-%m-%d")
        }
        module_week.append(item)
        prev_week = curr_week
        
    if len(module_week) > 0:
        module_list.append(module_week)
        
    mod_fname = '{}/data/{}'.format(OUT_ROOT,MODULES_FILE)
    #print('module_list = {}'.format(module_list))
    with io.open(mod_fname, 'w', encoding='utf8') as mod_file:
        json.dump(module_list, mod_file, ensure_ascii=False, sort_keys=True, indent=4)
                           
if __name__ == '__main__':
    main()


