'''
Created on Jun 14, 2019

@author: kalvis
'''

import math

def fact(n): 
    if n<=0:
        return 1
    else:
        return n*fact(n-1)

def is_prime(p): 
    if p <= 1:
        return False
    if p == 2 or p == 3:
        return True
    if p == 4:
        return False 
    result = True
    for k in range(2,math.floor(math.sqrt(p))+1):
        if p % k == 0:
            result = False
            break
    return result
 

# Return the largest power of p that divides n!
def lagrange(n,p):
    result = 0
    c = math.floor(n // p)
    while c > 0:
        result = result + c
        c = c // p
    return result


# Return list of tuples [(p1,k1),(p2,k2)...] 
def factorize(m): 
    result = list()
    c = m
    p = 2
    k = 0
    while c > 1:
        if c % p == 0:
            c = c // p
            k = k + 1
#            print('    c is %d' % c)
        else: 
            if k>0:
                result.append((p,k))
            p = p + 1
            k = 0
    if k > 0:
        result.append((p,k))
    return result

## Given list [(p1,k1),(p2,k2),...]
## find the value for the relevant pair (p,k) and return k
def lookup(lst, p):
#    print(' called lookup(%s,%s)' % (lst,p))
    result = 0
    for pp in lst:
        if p==pp[0]:
            result = pp[1]
            break
    return result
       

# Return smallest prime where l1 is not divisible by l2 (or 0, if they are divisible)
def smallest_witness(l1,l2):
    result = 0
    for pp in l2: 
        p = pp[0]
        k = pp[1]
        ll1 = lookup(l1,p)
        if ll1 < k:
            result = p
            break
    return result

