'''
Created on Sep 14, 2019

@author: kalvis
'''


def main():
    buckets = dict()
    sums = dict()
    for i in range(1,20000): 
        buckets[i] = list()
    for i in range(1,200):
        sums[i] = list()
    for i in range(1,30): 
        for j in range(i,30):
            #A = i + j
            B = i**2 + j**2
            buckets[B].append((i,j))
    #        sums[A].append((i,j))
    for k in range(1,20000): 
        if len(buckets[k]) > 1:             
            print("(%d,%s)" % (k,buckets[k]))
            for pair in buckets[k]:
                A = pair[0] + pair[1]
                sums[A].append(pair)
    for l in range(1,200):
        if len(sums[l]) > 1:
            print("[%d,%s]" % (l,sums[l]))
    

if __name__ == '__main__':
    main()