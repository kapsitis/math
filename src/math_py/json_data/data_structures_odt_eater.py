import csv
import io
import json
import copy
import re

from pandas_ods_reader import read_ods

ROOT = 'c:/Users/kalvis.apsitis/workspace/math/src/site/data-structures/website-data'
CSV_FILE = 'testcases.csv'
JSON_FILE = 'testcases.json'
# JSON param name
SUBITEMS = 'testItems'


def getLines():
    csv_lines = list()
    path = '{}/{}'.format(ROOT, CSV_FILE)
    with open(path, mode='r', encoding='utf-8') as csv_in:
        for csv_line in csv_in:
            csv_lines.append(csv_line)
        # csv_lines = csv_in.splitlines()
    result = csv.reader(csv_lines)
    return result


def getIdSubid(str):
    m = re.match(r'^([0-9]+)$', str)
    if m:
        return (int(m.group(1)), -1)
    m = re.match(r'^([0-9]+)\.([0-9]+)$', str)
    if m:
        return (int(m.group(1)), int(m.group(2)))
    return (-1, -1)


def getJsonOfLists(lines):
    bigItems = []
    subitem = dict() 
    row_count = 0
    
    prev_a = -2
    prev_b = -2
    
    item = {
    }
    
    subitem = {
    }

    for line in lines:
        row_count += 1
        if row_count == 1:
            continue
        
        curr_id = line[0].strip()
        curr_key = line[1].strip()
        curr_val = line[2].strip()

        (curr_a, curr_b) = getIdSubid(curr_id)

        if (curr_b == -1):
            prev_b = curr_b
            if (curr_a != prev_a):
                prev_a = curr_a
                bigItems.append(copy.deepcopy(item))
            topItem = bigItems[len(bigItems)-1]
            topItem[curr_key] = curr_val
        else:
            if (prev_b == -1 and curr_b > -1):
                #print('AAA = {}.{}'.format(curr_a,curr_b))
                prev_b = curr_b
                topItem = bigItems[len(bigItems)-1]            
                topItem[SUBITEMS] = []
                topItem[SUBITEMS].append(copy.deepcopy(subitem))
            elif (prev_b != curr_b):            
                #print('BBB = {}.{}'.format(curr_a,curr_b))
                prev_b = curr_b
                topItem = bigItems[len(bigItems)-1]
                topItem['testItems'].append(copy.deepcopy(subitem))
                topSubitem = topItem[SUBITEMS][len(topItem[SUBITEMS])-1]
                topSubitem[curr_key] = curr_val
            elif (curr_b > -1):
                #print('CCC = {}.{}'.format(curr_a,curr_b))
                prev_b = curr_b
                topItem = bigItems[len(bigItems)-1]
                topSubitem = topItem[SUBITEMS][len(topItem[SUBITEMS])-1]
                topSubitem[curr_key] = curr_val
    return bigItems
            


def main():
    lines = getLines()
    jsonOfLists = getJsonOfLists(lines)
    outFile = '{}/{}'.format(ROOT,JSON_FILE)
    with io.open(outFile, 'w', encoding='utf8') as mod_file:
        json.dump(jsonOfLists, mod_file, ensure_ascii=False, sort_keys=True, indent=4)


if __name__ == '__main__':
    main()
