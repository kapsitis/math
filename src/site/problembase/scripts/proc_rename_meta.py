import sys
import requests
import csv
import re

old_topics = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQvAsYeFYhuFLmLgtMiYFeQFeeO4e0DgteRXRg1zpQ2iMcWZr-mIgdyDYnh1IoKq4l5v9C-JAE1-Qcy/pub?gid=0&single=true&output=csv'
new_topics = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQvAsYeFYhuFLmLgtMiYFeQFeeO4e0DgteRXRg1zpQ2iMcWZr-mIgdyDYnh1IoKq4l5v9C-JAE1-Qcy/pub?gid=462395741&single=true&output=csv'
    

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



# To rename metainformation field 
# ```python proc_rename_meta.py file_name questionType "Find.All" "FindAll"```
# This command searches for all the patterns:
# * questionType:label1,label2,label3
# If any of labels equals "Find.All", it is renamed into "FindAll"
def main(in_file, out_file, prop_name, mydict):
    lines = []
    pattern = re.compile(r'^\* \[([^]]+)\]\(#\)')

    lines = []
    with open(in_file, mode="r") as f:
        for line in f.readlines():
            # Use re.sub with a function to replace found patterns
            def replace_match(match):
                key = match.group(1)  # This is the captured part of the pattern
                # Check if the key is in the dictionary and return the replacement
                if key in mydict:
                    return f"* {prop_name}:{mydict[key]}"
                # If no replacement is found, return the match unchanged
                return match.group(0)
            
            modified_line = pattern.sub(replace_match, line)
            lines.append(modified_line)

    with open(out_file, 'w') as of:
        for line in lines:
            of.write(line)

if __name__ == '__main__':
    get_spreadsheets()
    if len(sys.argv) < 6:
        print("Usage: python proc_rename_meta.py in_file out_file prop_name label1 label2")
    in_file = sys.argv[1]
    out_file = sys.argv[2]
    prop_name = sys.argv[3]
    label1 = sys.argv[4]
    label2 = sys.argv[5]
    mydict = get_old_topics()

    main(in_file, out_file, prop_name, mydict)


