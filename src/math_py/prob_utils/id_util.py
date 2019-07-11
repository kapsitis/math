import re

def get_country_by_id(prob_id):
    if re.match('^LV.*', prob_id):
        return 'LV'
    elif re.match('^EE.*', prob_id):
        return 'EE'
    else:
        #print('Unidentified %s' % prob_id)
        return 'other'

def get_problem_dir_list():
    prob_dir_lst = ['numtheory-ee-pk' ,'numtheory-ee-lo', 'numtheory-ee-lvs-lvt', 
            'numtheory-lv-no', 'numtheory-lv-vo', 'numtheory-lv-ao', 
            'numtheory-lt-lkmmo', 'numtheory-lt-ldk',
            'numtheory-lt-raj',  'numtheory-lt-lmmo', 'numtheory-lt-vumif',
            'numtheory-bbk-p1','numtheory-bbk-p2','numtheory-bbk-p3','numtheory-bbk-p4'
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
        'EE.LVS/LVT':'numtheory-ee-lvs-lvt',
        'EE.LVS':'numtheory-ee-lvs-lvt',
        'EE.LVT':'numtheory-ee-lvs-lvt',
        'LV.NO':'numtheory-lv-no',
        'LV.VO':'numtheory-lv-vo',
        'LV.AO':'numtheory-lv-ao',
        'LT.LKMMO':'numtheory-lt-lkmmo',
        'LT.LDK':'numtheory-lt-ldk',
        'LT.RAJ':'numtheory-lt-raj',
        'LT.LMMO':'numtheory-lt-lmmo',
        'LT.VUMIF':'numtheory-lt-vumif',
        'BBK2012.P1':'numtheory-bbk-p1',
        'BBK2012.P2':'numtheory-bbk-p2',
        'BBK2012.P3':'numtheory-bbk-p3',
        'BBK2012.P4':'numtheory-bbk-p4'
    }
    result = list()
    for pp in lst_problems:
        pp_pref=re.sub(r'(LV|EE|LT|BBK2012)\.([^\.]+)\..*',r'\1.\2',pp)
        file_id = file_dict[pp_pref]
        lower_id = pp.lower()
        result.append('<a href="../../problems/%s/content.html#/%s">%s</a>' % (file_id,lower_id,pp))
    return result
