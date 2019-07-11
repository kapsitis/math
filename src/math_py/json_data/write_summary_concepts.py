# -*- coding: utf-8 -*-

import io
import json
import os
from prob_utils import id_util

def main():
    the_dir = os.getcwd()
    print('os.getcwd()="%s"' % the_dir)
    if the_dir.endswith('/src/math_py/json_data'):
        os.chdir("../../..")
        print('Changed working directory to "%s"' % os.getcwd())

    with open('../../workspace-new/linen-tracer-682/data/problems.json') as f:
        lst_problems = json.load(f)
    
    
    gg1 = 0
    gg2 = 0
    gg3 = 0
    for prob in lst_problems:
        gradeGroup = id_util.get_gradegroup_by_id(prob['id'])
        if gradeGroup == '9':
            gg1 += 1
        elif gradeGroup == '12':
            gg2 += 1
        elif gradeGroup == 'other':
            gg3 += 1
    print('(1,2,3) = (%d,%d,%d)' % (gg1,gg2,gg3))

    concept_map = {}
    for prob in lst_problems:
        concepts = prob['concepts']
        prob_id = prob['id']
        for concept in concepts: 
            if concept in concept_map: 
                concept_map[concept].append(prob_id)
            else:
                concept_map[concept] = [prob_id]
        
    json_summary = []
    colors = ["#FF0000", "#FF8000", "#FFFF00", "#80FF00", "#00FF00", 
              "#00FF80", "#00FFFF", "#0080FF", "#0000FF", "#8000FF"]
    
    for concept in sorted(concept_map):
        jun_total = 0
        sen_total = 0
        for prob in concept_map[concept]:
            gg = id_util.get_gradegroup_by_id(prob)
            if gg == '9':
                jun_total += 1
            else:
                sen_total += 1
        colidx = round(10*sen_total/(jun_total + sen_total) - 0.51)
        if colidx < 0:
            colidx = 0
        elif colidx > 9:
            colidx = 9
        item = {'c_id':concept, 'pp': concept_map[concept], 'jun': jun_total, 'sen': sen_total, 'col': colors[colidx], 'colidx': colidx}
        json_summary.append(item)
    
    #json_summary2 = sorted(json_summary, key = lambda item: len(item['pp']), reverse=True)
    json_summary2 = sorted(json_summary, key = lambda item: item['sen']/(item['jun']+item['sen']))    
    
    fname = '../../workspace-new/linen-tracer-682/data-js/summary_concepts.json'
    with io.open(fname, 'w', encoding='utf8') as json_file:
        json_file.write('allConcepts = ')
        json.dump(json_summary2, json_file, ensure_ascii=False, sort_keys=True, indent=4)
        json_file.write(';')
    fname2 = '../../workspace-new/linen-tracer-682/data/summary_concepts.json'
    with io.open(fname2, 'w', encoding='utf8') as json_file2:
        json.dump(json_summary2, json_file2, ensure_ascii=False, sort_keys=True, indent=4)

if __name__ == '__main__':
    main()
    
    
