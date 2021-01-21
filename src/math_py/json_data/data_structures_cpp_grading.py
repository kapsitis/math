import csv
import io
import json
import copy
import re
import sys
import os

from pandas_ods_reader import read_ods
import time
from datetime import date
from datetime import timedelta

#sys.path.append(os.path.join(os.path.dirname(__file__)))
#from '.' import 
#os.system('data_structures_odt_eater.py')
import data_structures_odt_eater


ROOT = 'c:/Users/kalvis.apsitis/workspace/ddgatve-problems/data-structures/'
ODS_FILE = 'students-2020.ods' 
CSV_FILE = 'data-structures-ex01.csv'
GRADES_FILE = 'data_structures_grading.json'

WEBROOT = 'c:/Users/kalvis.apsitis/workspace/linen-tracer-682'

##
# THIS STUFF DOES NOT WORK!!
#def convert_file():
#    path = '{}/{}'.format(ROOT,ODS_FILE)
#    
#    sheet_idx = 1
#    df = read_ods(path, sheet_idx, 
#                  columns=['LongID', 'GITURL', 'Email', 'ShortID', 'Builds', 'T01', 'T11', 'T12', 'T13', 'T14', 'T15', 'Notes'])    
#    df.to_csv('{}/website-data/{}.csv'.format(ROOT,CSV_FILE), 
#               index = False, header=True)



def get_csv_local(input_file):
    csv_lines = list()
    path = '{}/{}'.format(ROOT,input_file)
    with open(path, mode='r', encoding='utf-8') as csv_in:
        for csv_line in csv_in:
            csv_lines.append(csv_line)
        #csv_lines = csv_in.splitlines()
    result = csv.reader(csv_lines)
    return result




def mainmain(input_file,ii):
    questionNumbers = [7,7,10,10,6,15,13,10]
    print('Processing file {}'.format(input_file))
    #convert_file()    
    grades = get_csv_local(input_file)    
    grade_list = []
    row_count = 0
    # How many columns precede grades
    front_columns = 5
    Qnum = questionNumbers[ii]
    
    all_items = {} 
    for grade in grades:
        row_count += 1
        if row_count == 1:
            continue
        
        studId = grade[4].strip()
        gradeList = list()
        #total = 0
        for i in range(front_columns,front_columns+Qnum):
            g = grade[i].strip()
            #print('row_count,i,g = {},{},{}'.format(row_count,i,g))
            gradeList.append(g)
            #total += int(g)                    
        #strTotal = '{}'.format(total)        
        note = grade[front_columns+Qnum].strip()
        strTotal = grade[front_columns+Qnum+1].strip()
        grade_list.append({'studID':studId, 'grades':gradeList, 'total': strTotal, 'notes':note})
        all_items[studId] = {'studID':studId, 'grades':gradeList, 'total': strTotal, 'notes':note}
        
    
    allIDs = all_items.keys()
    allIDsSorted = sorted(allIDs)
    grade_list = []
    for idid in allIDsSorted:
        grade_list.append(all_items[idid])
    return grade_list
    
def main():
    lines = data_structures_odt_eater.getLines()
    jsonOfLists = data_structures_odt_eater.getJsonOfLists(lines)    
    input_files = ['data-structures-ex01.csv','data-structures-ex02.csv', 'data-structures-ex03.csv', 'data-structures-ex04.csv',
                   'data-structures-ex05.csv', 'data-structures-ex06.csv', 'data-structures-ex07.csv', 'data-structures-ex08.csv']
    for ii in range(0,len(input_files)):
        grade_list = mainmain(input_files[ii],ii)
        jsonOfLists[ii]['students'] = grade_list
    
    
    mod_fname = '{}/data/{}'.format(WEBROOT,GRADES_FILE)
    with io.open(mod_fname, 'w', encoding='utf8') as mod_file:
        json.dump(jsonOfLists, mod_file, ensure_ascii=False, sort_keys=True, indent=4)
                           
    
    
    
if __name__ == '__main__':
    main()


