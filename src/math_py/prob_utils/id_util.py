import re

def get_country_by_id(prob_id):
    if re.match('^LV.*', prob_id):
        return 'LV'
    elif re.match('^EE.*', prob_id):
        return 'EE'
    elif re.match('^LT.*', prob_id):
        return 'LT'
    else:
        #print('Unidentified %s' % prob_id)
        return 'other'

def get_problem_dir_list():
    prob_dir_lst = ['numtheory-ee-pk' ,'numtheory-ee-lo', 
                    'numtheory-ee-lvs', 'numtheory-ee-lvt', 'numtheory-ee-tst',
                    'numtheory-lv-no', 'numtheory-lv-vo', 'numtheory-lv-ao', 'numtheory-lv-tst', 'numtheory-lv-other',
                    'numtheory-lt-lkmmo', 'numtheory-lt-ldk',
                    'numtheory-lt-raj', 'numtheory-lt-vilnius',  'numtheory-lt-lmmo', 'numtheory-lt-vumif','numtheory-lt-tst',
                    'numtheory-bbk-p1','numtheory-bbk-p2','numtheory-bbk-p3','numtheory-bbk-p4',
                    'numtheory-bbk-p5','numtheory-bbk-p6','numtheory-bbk-p7','numtheory-bbk-p8','numtheory-bbk-p9'
                    ]
    return prob_dir_lst


def get_gradegroup_by_id(prob_id):
    if re.match('^(LV|EE)\.[^\.]+\.[0-9]+\.[7-9].*',prob_id):
        return '9'
    elif re.match('^(LV|EE)\.[^\.]+\.[0-9]+\.(1|noorem|vanem).*',prob_id):
        return '12'
    else:
        return 'other'

def get_category(prob_id):
    co = get_country_by_id(prob_id)
    gr = get_gradegroup_by_id(prob_id)

    if co == 'EE':
        if gr == '9':
            return 'EEjun'
        elif gr == '12':
            return 'EEsen'
    elif co == 'LV':
        if gr == '9':
            return 'LVjun'
        elif gr == '12':
            return 'LVsen'
    else:
        return 'OOsen'
    
    
    
def get_html_links(lst_problems):
    file_dict = {
        'EE.PK':'numtheory-ee-pk',
        'EE.LO':'numtheory-ee-lo',
        'EE.LVS':'numtheory-ee-lvs',
        'EE.LVT':'numtheory-ee-lvt',
        'EE.TST':'numtheory-ee-tst',
        'LV.NO':'numtheory-lv-no',
        'LV.VO':'numtheory-lv-vo',
        'LV.AO':'numtheory-lv-ao',
        'LV.TST':'numtheory-lv-tst',
        'LV.OTHER':'numtheory-lv-other',
        'LT.LKMMO':'numtheory-lt-lkmmo',
        'LT.LDK':'numtheory-lt-ldk',
        'LT.RAJ':'numtheory-lt-raj',
        'LT.VILNIUS':'numtheory-lt-vilnius',
        'LT.LMMO':'numtheory-lt-lmmo',
        'LT.VUMIF':'numtheory-lt-vumif',
        'LT.TST':'numtheory-lt-tst',
        'BBK2012.P1':'numtheory-bbk-p1',
        'BBK2012.P2':'numtheory-bbk-p2',
        'BBK2012.P3':'numtheory-bbk-p3',
        'BBK2012.P4':'numtheory-bbk-p4',
        'BBK2012.P5':'numtheory-bbk-p5',
        'BBK2012.P6':'numtheory-bbk-p6',
        'BBK2012.P7':'numtheory-bbk-p7',
        'BBK2012.P8':'numtheory-bbk-p8',
        'BBK2012.P9':'numtheory-bbk-p9'
    }
    result = list()
    for pp in lst_problems:
        pp_pref=re.sub(r'(LV|EE|LT|BBK2012)\.([^\.]+)\..*',r'\1.\2',pp)
        file_id = file_dict[pp_pref]
        lower_id = pp.lower()
        result.append('<a href="../../problems/%s/content.html#/%s">%s</a>' % (file_id,lower_id,pp))
    return result
