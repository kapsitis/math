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
def main(in_file, out_file, old_prop, new_prop, changes):
    pattern = re.compile(rf'^(\* ({old_prop})):(\S+)$')

    lines = []
    with open(in_file, mode="r") as f:
        for line in f.readlines():
            def replace_match(match):
                key = match.group(2)
                multi_value = match.group(3).strip()
                multi_list = multi_value.split(',')

                # Track if any replacement occurs
                replacement_occurred = False
                new_multi_list = []

                for item in multi_list:
                    # Check if the current item should be replaced
                    if item in changes:
                        new_multi_list.append(changes[item])
                        replacement_occurred = True
                    else:
                        new_multi_list.append(item)

                # If no replacement occurred, return the original line
                if not replacement_occurred:
                    return match.group(0)

                # Otherwise replace the property name and its value
                new_multi_value = ','.join(new_multi_list)
                return f'* {new_prop}:{new_multi_value}'

            modified_line = pattern.sub(replace_match, line)
            lines.append(modified_line)

    with open(out_file, 'w') as of:
        for line in lines:
            of.write(f'{line}')

if __name__ == '__main__':
    if len(sys.argv) < 5:
        print("Usage: python proc_rename_meta.py old_prop new_prop old_value new_value")
    old_prop = sys.argv[1]
    new_prop = sys.argv[2]
    old_value = sys.argv[3]
    new_value = sys.argv[4]


    # changes = {'LTDivisibility': 'Divisibility', 
    #            'LTEquationSystems': 'EquationSystems',
    #            'LTLogic': 'Logic', 
    #            'LTCuttingCoversColoring': 'CuttingCoversColoring', 
    #            'LTInvariant': 'FixedInvariant', 
    #            'LTCongruenceModulo': 'Congruences', 
    #            'LTNumeralSystems': 'NumeralSystems', 
    #            'LTEquations': 'Equations', 
    #            'LTObjectSystemsGeometry': 'ObjectSystemsGeometry'}



    changes = {'LTGraphs': 'Graphs', 
               'LTInequalities': 'Inequalities', 
               'LTCircleAndRelatedAngles': 'CirclesAndRelatedAngles', 
               'LTGames': 'CombinatorialGames'}

    
    in_files = get_input_files() 
    for in_file in in_files:
        out_file = in_file[:-3] + "2.md"
        print(f'{in_file} --> {out_file}')
        main(in_file, out_file, old_prop, new_prop, changes)


