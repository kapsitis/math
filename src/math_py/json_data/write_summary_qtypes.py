# -*- coding: utf-8 -*-

import io
import json
import os
import re
from prob_utils import id_util

def main():
    the_dir = os.getcwd()
    print('os.getcwd()="%s"' % the_dir)
    if the_dir.endswith('/src/math_py/json_data'):
        os.chdir("../../..")
        print('Changed working directory to "%s"' % os.getcwd())

    with open('../../workspace-new/linen-tracer-682/data/problems.json') as f:
        lst_problems = json.load(f)
        
    EEjun = 0
    EEsen = 0
    LVjun = 0
    LVsen = 0
    LTjun = 0
    LTsen = 0
    OOsen = 0
    
    qtype_map = {}
    
    for prob in lst_problems:
        cat = id_util.get_category(prob['id'])
        if cat == 'EEjun':
            EEjun += 1
        elif cat == 'EEsen':
            EEsen += 1
        elif cat == 'LVjun':
            LVjun += 1
        elif cat == 'LVsen':
            LVsen += 1
        elif cat == 'LTjun':
            LTjun += 1
        elif cat == 'LTsen':
            LTsen += 1
        else:
            OOsen += 1
        qtypes = prob['qtypes']
        for qt in qtypes:
            if qt in qtype_map:
                qtype_map[qt].append(cat)
            else:
                qtype_map[qt] = [cat]
    print('(EEjun,EEsen,LVjun,LVsen,LTjun,LTsen,OOsen)=(%d,%d,%d,%d,%d,%d,%d)' % 
          (EEjun,EEsen,LVjun,LVsen,LTjun,LTsen,OOsen))

    cons_dict = {
        'Algorithm': [0,0,0,0,0,0,0],
        'Find.All': [0,0,0,0,0,0,0],
        'Find.Any.Only': [0,0,0,0,0,0,0],
        'Find.Count': [0,0,0,0,0,0,0],
        'Find.Min.Max': [0,0,0,0,0,0,0],
        'Prove.Exists': [0,0,0,0,0,0,0],
        'Prove.ForAll.NotExists': [0,0,0,0,0,0,0],
        'ProveDisprove.Exists': [0,0,0,0,0,0,0],
        'ProveDisprove.ForAll': [0,0,0,0,0,0,0],
        'The.Other.Proofs': [0,0,0,0,0,0,0]
    }
    consolidation_table = {
        'Algorithm': 'Algorithm',
        'Find.All': 'Find.All',
        'Find.Any': 'Find.Any.Only',
        'Find.Count': 'Find.Count',
        'Find.Max': 'Find.Min.Max',
        'Find.Min': 'Find.Min.Max',
        'Find.Only': 'Find.Any.Only',
        'Prove.Exists': 'Prove.Exists',
        'Prove.ForAll': 'Prove.ForAll.NotExists',
        'Prove.NotExists': 'Prove.ForAll.NotExists',
        'Prove.Other': 'The.Other.Proofs',
        'ProveDisprove.Exists': 'ProveDisprove.Exists',
        'ProveDisprove.ForAll': 'ProveDisprove.ForAll',
        'ProveDisprove.Other': 'The.Other.Proofs'
    }
    for key in sorted(qtype_map):
        if key != 'NoteOnProof':
            item0 = sum(a == 'EEjun' for a in qtype_map[key])
            item1 = sum(a == 'EEsen' for a in qtype_map[key])
            item2 = sum(a == 'LVjun' for a in qtype_map[key])
            item3 = sum(a == 'LVsen' for a in qtype_map[key])
            item4 = sum(a == 'LTjun' for a in qtype_map[key])
            item5 = sum(a == 'LTsen' for a in qtype_map[key])            
            item6 = sum(a == 'OOsen' for a in qtype_map[key])
            #print('%s: %s' % (key, item1+item2+item3+item4+item5))
            
            cons_dict[consolidation_table[key]][0] += item0
            cons_dict[consolidation_table[key]][1] += item1
            cons_dict[consolidation_table[key]][2] += item2
            cons_dict[consolidation_table[key]][3] += item3
            cons_dict[consolidation_table[key]][4] += item4
            cons_dict[consolidation_table[key]][5] += item5
            cons_dict[consolidation_table[key]][6] += item6
            
    json_summary = []
    count = 0
    for key in sorted(cons_dict):
        val = cons_dict[key]
        item = {
            'count':count,
            'qtype_id':key,
            'EEjun':val[0],
            'EEsen':val[1],
            'LVjun':val[2],
            'LVsen':val[3],
            'LTjun':val[4],
            'LTsen':val[5],
            'OOsen':val[6]
        }
        json_summary.append(item)
        count += 1
    fname = '../../workspace-new/linen-tracer-682/data-js/summary_qtypes.json'
    with io.open(fname, 'w', encoding='utf8') as json_file:
        json_file.write('data = ')
        json.dump(json_summary, json_file, ensure_ascii=False, sort_keys=True, indent=4)
        json_file.write(';')


if __name__ == '__main__':
    main()
