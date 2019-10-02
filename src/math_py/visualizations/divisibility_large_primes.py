'''
Created on Oct 1, 2019

@author: kalvis
'''

import math
import numpy as np
from itertools import count, islice


def is_prime(n):
    return n > 1 and all(n % i for i in islice(count(2), int(math.sqrt(n)) - 1 ))
    

def main():
    lower = (int(math.exp(20)) // 1000)*100
    # 485165195.4097903
    for i in range(lower+400, lower + 500):
        if is_prime(i):
            print('prime is %d' % i)
    
    
if __name__ == '__main__':
    main()