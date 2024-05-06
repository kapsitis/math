import sys
import requests
import csv
import re

# Atgriežam sarakstu, kurā ir pārīši row[5], row[8]
def get_old_topics():  
    result = dict()
    with open('resources/old_topics.csv', 'r',  encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names: [{",".join(row)}]')
                line_count += 1
            else:
                result[row[5]] = row[8]
                line_count += 1
        print(f'Processed {line_count} lines.')
    return result

def get_input_files():
    result = []
    with open('resources/input_files.csv', 'r',  encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            result.append(row[0])
            line_count += 1
    return result


# To rename metainformation field 
# ```python proc_rename_meta.py file_name questionType "Find.All" "FindAll"```
# This command searches for all the patterns:
# * questionType:label1,label2,label3
# If any of labels equals "Find.All", it is renamed into "FindAll"
def main(in_file, out_file, prop_name, mydict):
    lines = []
    # pattern = re.compile(r'^\* \[([^]]+)\]\(#\)$')
    pattern = re.compile(f'^((\\* )?{prop_name})([:=])(\\S+)$')

    lines = []
    with open(in_file, mode="r") as f:
        for line in f.readlines():
            def replace_match(match):
                key = match.group(1)
                sep = match.group(3)
                value = match.group(4)
                for kk in mydict: 
                    value = value.replace(kk, mydict[kk])
                return f'{key}{sep}{value}'
            # def replace_match(match):
            #     key = match.group(1)
            #     if key in mydict:
            #         return f"* {prop_name}:{mydict[key]}"
            #     return match.group(0)
            modified_line = pattern.sub(replace_match, line)
            lines.append(modified_line)

    with open(out_file, 'w') as of:
        for line in lines:
            of.write(f'{line}')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python proc_rename_meta.py in_file out_file prop_name")
    prop_name = sys.argv[1]
    # mydict = get_old_topics()
    mydict = {'Find.All': 'FindAll', 
              'Find.Count': 'FindCount', 
              'Find.Optimal': 'FindOptimal',
              'Find.Example': 'FindExample',
              'Find.Any': 'FindExample',
              'Find.Only': 'FindAll', 
              'Prove.ForAll': 'Prove', 
              'Prove.Exists': 'Prove',
              'Prove.NotExists': 'Prove',
              'Prove.Other': 'Prove',
              'ProveDisprove.Exists': 'ProveDisprove',
              'ProveDisprove.ForAll': 'ProveDisprove',
              'ProveDisprove.Other': 'ProveDisprove',
              'Find.Min': 'FindOptimal',
              'Find.Max': 'FindOptimal',
              'Find.Only': 'FindAll',         
              }
    
    in_files = get_input_files()
    for in_file in in_files:
        out_file = in_file[:-3] + "2.md"
        print(f'{in_file} --> {out_file}')
        main(in_file, out_file, prop_name, mydict)


