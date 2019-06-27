'''
Created on Jun 17, 2019

@author: kalvis
'''


def main():
    c = 2
    a = [0,c]
    for i in range(1,20):
        aa = a[i]**3 - 4*c*a[i]**2 + 5*(c**2)*a[i] + c
    
    

if __name__ == '__main__':
    main()