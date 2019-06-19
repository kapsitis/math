'''
Created on Jun 17, 2019

@author: kalvis
'''

from imo_shl import list_utils



def main():
    a = [5,6]
#    a = [5,7]
    prod = list_utils.prod_all(a)
    startX = 0
    sqsum = 0
    for j in range(0,prod+1):
        for k in range(0,len(a)):
            if j % a[k] == 0:
                bb = j - startX
                print('adding %d^2' % bb)
                sqsum = sqsum + bb*bb
                startX = j
                break
    print('sqsum = %d' % sqsum)            
    
    





if __name__ == '__main__':
    main()


