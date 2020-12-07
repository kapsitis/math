import csv
import io
import json
import time
from geopy.geocoders import Nominatim


'''
Recipe taken from here:
https://medium.com/analytics-vidhya/how-to-generate-lat-and-long-coordinates-of-city-without-using-apis-25ebabcaf1d5
It shows how to get coordinates from the name of a place without registering for any API.
'''



# Modify this to the place where this Python script and 'novadi_in.csv' file is located.
ROOT = 'c:/Users/kalvis.apsitis/workspace/math/src/math_py/visualizations'    

def get_csv_local():
    # Obtained from https://data.gov.lv/dati/lv/dataset/latvijas-iedzivotaju-skaits-pasvaldibas    
    IN_FILE = 'novadi_in.csv'
    csv_lines = list()
    path = '{}//{}'.format(ROOT,IN_FILE)
    with open(path, mode='r', encoding='utf-8') as csv_in:
        for csv_line in csv_in:
            csv_lines.append(csv_line)
        #csv_lines = csv_in.splitlines()
    result = csv.reader(csv_lines)
    return result



def main():
    csv_lines = get_csv_local()
    row_count = 0

    items_list = list()    
    for row in csv_lines:
        row_count += 1
        # skip headers
        if row_count == 1:
            continue
        # skip some larger rows
        if row_count > 5:
            break
        
        # pause 0.5 seconds
        time.sleep(0.5)
        # Request the latitude+longitude
        novads_name = row[0].strip()
        inhabitants = int(row[5].strip())
        full_name = novads_name + ', Latvia'
        geolocator = Nominatim(user_agent = 'Kalvis Apsitis')
        location = geolocator.geocode(full_name)
    
        item = {
            'novads':novads_name,
            'address':location.address,
            'inhabitants':inhabitants,
            'latitude':location.latitude,
            'longitude':location.longitude
        }
        items_list.append(item)
    
    OUT_FILE = 'novadi_out.json'
    novadi_outfile = '{}/{}'.format(ROOT,OUT_FILE)
    with io.open(novadi_outfile, 'w', encoding='utf8') as novadi_file:
        json.dump(items_list, novadi_file, ensure_ascii=False, sort_keys=True, indent=4)
    
    

if __name__ == '__main__':
    main()
    
