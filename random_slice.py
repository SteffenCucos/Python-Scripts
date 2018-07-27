import random


def random_slices(a,n,i):
    '''
    a is a 2 dimensional array of n sub-arrays
    '''

    s = []
    for i in range(i):
        l = []
        for j in range(n):
            index = random.randint(0,len(a[j])-1)
            l.append(a[j][index])
        if l not in s:
            s.append(l)
    return s
        


    
