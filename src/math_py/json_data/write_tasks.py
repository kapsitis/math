import json
import io

def main():
    skill1 = {
        'levels': [1],
        'id': 'alg',
        'desc': u'Izmantot algebriskos apzīmējumus un metodes skaitļu teorijas uzdevumos',
        'problems': []
    }
    skill2 = {
        'levels': [1,1],
        'id': 'alg.equation',
        'desc': u'Ieviest mainīgo apzīmējumus, sastādīt vienādojumus, izmantojot šos apzīmējumus.',
        'problems': ['EE.PK.2018.10.3', 'NO.2000.9.4']        
    }
    
    fname = '../../../../../workspace-new/linen-tracer-682/data/tasks.json'
    with io.open(fname, 'w', encoding='utf8') as json_file:
        json.dump([skill1,skill2], json_file, ensure_ascii=False, sort_keys=True, indent=4)





if __name__ == '__main__':
    main()
    
    