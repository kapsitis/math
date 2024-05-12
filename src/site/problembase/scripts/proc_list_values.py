import sys
import requests
import csv
import re

url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSsIUjRXRU6L_MGgEmgUZlfwvygclZun964ilvH-l6F3TZ9w0I2MDce9VXqJgd4p2GZxF7vJ6OY5jcT/pub?output=csv"

def getGoogleSpreadsheet(url):  # Funkcija, kas iegūst Google Spreadsheet dokumentu ar olimpiāžu uzdevumu datiem'
    response = requests.get(url)
    open("resources/concepts.csv", "wb").write(response.content)

def readCSVfile():  # Funkcija, kas lasa CSV failu
    result = dict()
    with open('resources/concepts.csv', 'r',  encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                result[row[0]] = ((row[1], row[2]))
                line_count += 1
        print(f'Processed {line_count} lines.')
    return result

def merge(url,all_concepts):
    getGoogleSpreadsheet(url)
    # 1.solis - savākt vārdnīcu no readCVSVfile(), atgriež vārdnīcu
    existing_concepts = readCSVfile()
    # 2.solis - izveidojam paši savu tukšu vārdnīcu
    new_concepts = {}
    # 3.solis - for each - katram vārdam no all_concepts dara 1 no 2 zariem:
    #   Ja šis vārds nav esošajā vārdnīcā, tad jaunajai vārdnīcai pievieno vērtību ('NA', 'NA')
    #   Ja šis vārds jau ir esošajā vārdnīcā, tad jaunajai vārdnīcai pievieno jau esošo vērtību, kas ir latviešu tulkojums un skaidrojums
    for concept in all_concepts:
        if concept not in existing_concepts:
            new_concepts[concept] = ('NA', 'NA')
        else:
            new_concepts[concept] = existing_concepts[concept]
    # Pašās beigās var izrēķināt, cik ir tādu vārdu, kuri vecajā vārdnīcā bija, bet all_concepts sarakstā nav. 
    # To iegūst, kā 2 kopu starpību, atņem no esošās vārdnīcas atslēgām all_concepts sarakstu
    missing_concepts = set(existing_concepts.keys()) - set(all_concepts)
    # Pašās pašās beigās sakārto jaunās vārdnīcas atslēgas alfabētiski
    new_concepts = dict(sorted(new_concepts.items()))
    # Un sāk drukāt csv, kur ir atslēga [en] un tulkojums [lv] (1.elements no pārīša) un skaidrojums (2.elements no pārīša)
    # Rezultātu ieglabā csv failā
    with open('resources/merged_concepts.csv', 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['en', 'lv', 'skaidrojums'])  # Virsraksts
    for key, value in new_concepts.items():
        writer.writerow([key, value[0], value[1]])  # Rakstam rindiņas

    return missing_concepts


def get_input_files():
    result = []
    with open('resources/input_files.csv', 'r',  encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            result.append(row[0])
            line_count += 1
    return result

def main(in_file, prop_name):
    # ^ - rindas sākums, ((\\* )? - {...} - neobligāts numurējums ar *, 
    # {prop_name} - Python stringa mainīgā ievietošana (ekstrapulēšana), ([:=]) - atdalītājsimbols
    # (\\S+)$ - S - 1 vai vairāk burti, kas nav tukšumi, pašas metadatu vērtības
    pattern = re.compile(f'^((\\* )?{prop_name})([:=])(\\S+)$')

    concepts = []
    # Atveram uzdevuma failu lasīšanai
    with open(in_file, mode="r", encoding='utf-8') as f:
        # Katrai faila rindiņai 
        for line in f.readlines():
            # Ja rindiņa satur prop_name:v1,v2,v3 
            m = pattern.match(line)
            if m:
                value = m.group(4)
                concepts.extend(value.split(',')) # sašķelšana pret komatu
    return concepts

# This script parses all files with olympiad problems and extracts values for some metadata property
# Such as "concepts", all the values are collected in a long list and list is sorted and printed out

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python proc_list_values.py prop_name")
    prop_name = sys.argv[1]

    all_concepts = []
    
    in_files = get_input_files() # 
    for in_file in in_files:
        print(f'Processing {in_file}')
        a = main(in_file,prop_name)
        all_concepts.extend(a)

    all_concepts = list(set(all_concepts)) # set uztaisa par kopu (kopā nav atļauti atkārtojumi) un pēc tam pārtaisa atpakaļ par sarakstu
    all_concepts.sort()
    print(all_concepts)
    print(len(all_concepts))


