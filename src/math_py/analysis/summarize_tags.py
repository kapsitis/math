import os
import re

questionTypes = {}


def summarize():
    result = {}
    prob_dir_lst = ['numtheory-ee-pk' ,'numtheory-ee-lo', 
                    'numtheory-ee-lvs', 'numtheory-ee-lvt', 'numtheory-ee-tst',
                'numtheory-lv-no', 'numtheory-lv-vo', 'numtheory-lv-ao', 'numtheory-lv-tst', 'numtheory-lv-other',
                'numtheory-lt-ljkmo', 'numtheory-lt-lkmmo', 'numtheory-lt-ldk',
                'numtheory-lt-raj', 'numtheory-lt-vilnius', 'numtheory-lt-lmmo', 'numtheory-lt-vumif', 'numtheory-lt-tst'
                ]
    
    qTypes = ''
    cur_probid = ''
    for prob_dir in prob_dir_lst:
        with open('src/site/prob/%s/content.md' % prob_dir) as prob_input:
            for prob_lin in prob_input:
                if re.match('# <lo-sample/> .*', prob_lin):
                    cur_probid = re.sub('# <lo-sample/> ([^\s]+)','\g<1>', prob_lin).strip()
                    gradeCat = 'E'
                    gg = cur_probid.split(".")[0]
                    if gg.startswith('L'): 
                        gradeCat = 'L'
                    print('probid = "%s/%s"' % (cur_probid, gradeCat))
                elif re.match('questionType=(.+)\s*', prob_lin):
                    qTypes = re.sub('questionType=(.+)\s*','\g<1>', prob_lin).strip()
                    #print('qTypes = "%s"' % qTypes)
                    for qType in qTypes.split(','):
                        if qType in result: 
                            result[qType].append(gradeCat)
                        else:
                            result[qType] = [gradeCat]
    
    #result['alg.equation'] = [('numtheory-lv-no', 'LV.NO.2010.10.2'),('numtheory-lv-no', 'LV.NO.2010.10.4')] 
    return result   


def main(): 
    # Change current directory, if invoked directly
    the_dir = os.getcwd()    
    if the_dir.endswith('/src/math_py/analysis'):
        os.chdir("../../..")        
    the_stuff = summarize()
    for kk in the_stuff.keys():
        vv = the_stuff[kk]
        count_j = 0
        count_s = 0
        for v in vv:
            if v == 'E':
                count_j = count_j + 1
            else:
                count_s = count_s + 1
        print("the_stuff[%s] = %d/%d" % (kk,count_j,count_s))
        
        
if __name__ == '__main__':
    main()