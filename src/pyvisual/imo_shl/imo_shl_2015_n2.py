'''
Creative Commons, CC-BY 4.0
@author: kalvis
'''

import math
from imo_shl import numtheory_utils

# Return the product of all the numbers [m+1,n]
def prod_all(m,n):
    result = 1
    for k in list(range(m+1,n+1)):
        result = result*k
    return result


# Return factorial n! factorization as prime powers
def fact_factorial(n):
    if n == 2:
        return [(2,1)]
    plist = list()
    result = list()
    for p in range(2,n+1):
        if numtheory_utils.is_prime(p): 
            plist.append(p)
    for pp in plist:
        k = numtheory_utils.lagrange(n,pp)
        result.append((pp,k))
    return result

# Multiply/merge two lists of prime factors [(p1,k1),...]
def mul_merge(l1,l2):
    result = list()
    ll1 = list()
    for elt in l1:
        ll1.append(elt[0])
    ll2 = list()
    for elt in l2:
        ll2.append(elt[0])
    ll = list(set(ll1).union(set(ll2)))
    ll.sort()
    for elt in ll: 
        e1 = numtheory_utils.lookup(l1,elt)
        e2 = numtheory_utils.lookup(l2,elt)
        result.append((elt,e1+e2))
    return result   
    
# Return T, if list [(p1,k1),(p1,k2)...] is divisible by d
def is_divisible(lst, d):
    cur_d = d
    for pp in lst:
        p = pp[0]
        k = pp[1]
        while k > 0 and cur_d % p == 0:
            cur_d = cur_d // p
            k = k - 1
    if cur_d == 1: 
        return 'T'
    else:
        return 'F' 



def main():
    minA = 1
    maxA = 1000
    max_diff = 0
    vect = [0,0,0,0,0,0,0,0,0,0,0]
    for a in range(minA,maxA):
        found = False
        mylst = list()
        lower = a+6
        upper = a+7
        
        for b in range(lower,upper):
            d = prod_all(a,b)+1
            bb = fact_factorial(b)
            divisible = is_divisible(bb,d)
            mylst.append(divisible)
            if divisible == 'T':
                vect[b-a] = vect[b-a] + 1            
            if b-a > 1 and divisible == 'T':
                found = True
                if b - a > max_diff:
                    max_diff = b - a
        if found:
            for b in range(lower,upper):
                is_div = mylst[b-lower]
                print('(%3d,%3d)-%s ' % (a,b,is_div), end='')                
            print('')            
    print('max_diff = %d' % max_diff)
    print('vect is %s' % vect)
    
    # 7
    ddd = 7 * 79 * 1109 * 3119 * 3821 * 5381 * 9787
    ss = (1 + 13092*13093*13094*13095*13096) // ddd
    print('ss = %d' % ss)   
    b1 = numtheory_utils.is_prime(1109)
    b2 = numtheory_utils.is_prime(3119)
    b3 = numtheory_utils.is_prime(3821)
    b4 = numtheory_utils.is_prime(5381)
    b5 = numtheory_utils.is_prime(9787)
    
    print('(%s,%s,%s,%s,%s)' % (b1,b2,b3,b4,b5))   
    


if __name__ == '__main__':
    main()



