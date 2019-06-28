import os
import re

questionTypes = {}


def summarize():
    result = {}
    prob_dir_lst = ['numtheory-ee-pk' ,'numtheory-ee-lo', 'numtheory-ee-lvs-lvt', 
                'numtheory-lv-no-78', 'numtheory-lv-no', 'numtheory-lv-vo', 
                'numtheory-lv-ao', 'numtheory-lt-lkmmo', 'numtheory-lt-ldk',
                'numtheory-lt-raj',  'numtheory-lt-lmmo', 'numtheory-lt-vumif']
    
    cur_skill = ''
    cur_probid = ''
    for prob_dir in prob_dir_lst:
        with open('src/site/prob/%s/content.md' % prob_dir) as prob_input:
            for prob_lin in prob_input:
                if re.match('# <lo-sample/> .*', prob_lin):
                    cur_probid = re.sub('# <lo-sample/> ([^\s]+)','\g<1>', prob_lin).strip()
                    #print('probid = "%s"' % cur_probid)
                elif re.match('\* \[[^\[\]]+\]\(#\)\s*', prob_lin):
                    cur_skill = re.sub('\* \[([^\[\]]+)\]\(#\)\s*','\g<1>', prob_lin).strip()
                    #print('skillid = "%s"' % cur_skill)
                    if cur_skill in result: 
                        result[cur_skill].append((prob_dir, cur_probid))
                    else:
                        result[cur_skill] = [(prob_dir, cur_probid)]
    
    #result['alg.equation'] = [('numtheory-lv-no', 'LV.NO.2010.10.2'),('numtheory-lv-no', 'LV.NO.2010.10.4')] 
    return result   


def main(): 
    # Change current directory, if invoked directly
    the_dir = os.getcwd()    
    if the_dir.endswith('/src/math_py/analysis'):
        os.chdir("../../..")        
    summarize()
        
        
if __name__ == '__main__':
    main()