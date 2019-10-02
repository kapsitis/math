import math 

def isPrime(n):
    result = True
    ROOT = int(math.sqrt(n))
    for d in range(2,ROOT+1):
        if n % d == 0:
            result = False
            break
    return result

print(isPrime(10000000019))
