'''
Created on Jun 17, 2019

@author: kalvis
'''

def prod_all(lst):
    result = 1
    for i in range(0,len(lst)): 
        result = result*lst[i]
    return result

