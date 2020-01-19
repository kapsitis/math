import csv
import io
import json

def get_csv_local():
    csv_lines = list()
    with open('/home/kalvis/workspace/math/src/site/discrete/static/website-data/discrete-readings.csv') as csv_in:
        for csv_line in csv_in:
            csv_lines.append(csv_line)
        #csv_lines = csv_in.splitlines()
    result = csv.reader(csv_lines)
    return result


def make_lst(tasks):
    task_lst = list()
    nrow = 0
    prev_id = -1
    # Stuff to insert:    
    title = 'N/A'
    name = 'N/A'
    description = 'N/A'
    links = list()
    url = 'N/A'
    link = 'N/A'
    note = 'N/A'
    for row in tasks:
        curr_id = row[0]
        curr_key = row[2]
        if (nrow <= 2):
            prev_id = curr_id
        if (curr_id != prev_id and nrow > 2):
            print('row_id = {}'.format(nrow))
            task_lst.append({
                'itemNum': prev_id,
                'title':title, 
                'name': name, 
                'description': description, 
                'links': links})
            prev_id = curr_id
            title = 'N/A'
            name = 'N/A'
            description = 'N/A'
            links = list()
        if (curr_key == 'title'):
            title = row[3]
        elif (curr_key == 'name'):
            name = row[3]
        elif (curr_key == 'description'):
            description = row[3]
        elif (curr_key == 'url'):
            url = row[3]
        elif (curr_key == 'link'):
            link = row[3]
        elif (curr_key == 'note'):
            note = row[3]
            links.append({'url':url, 'link':link, 'note':note})
            url = 'N/A'
            link = 'N/A'
            note = 'N/A'
        nrow = nrow + 1
    print('row_id = {}'.format(nrow))
    
    # Append one more line
    task_lst.append({
        'itemNum': prev_id,
        'title':title, 
        'name': name, 
        'description': description, 
        'links': links})
    return task_lst


def main():
    the_table = get_csv_local()    
    readings = make_lst(the_table)
    fname = '/home/kalvis/workspace-new/linen-tracer-682/data/discrete_readings.json'
    with io.open(fname, 'w', encoding='utf8') as json_file:
        json.dump(readings, json_file, ensure_ascii=False, sort_keys=True, indent=4)
    
    

if __name__ == '__main__':
    main()