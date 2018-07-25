

def collapse(a):
    '''
    a is an 2 dimensional array of n objects
    '''

    s = []

    while len(a) > 0:
    #find the most repeated element
        d = {}
        for e in a:
            for n in e:
                d[n] = d.get(n,0) + 1
        m = 0
        n = None
        for k in list(d.keys()):
            if d[k] > m:
                m = d[k]
                n = k
        #n is now the most repeated element
        #now group by n
        ap = []
        l = [n]
        i = []
        for e in a:
            if n in e:
                for p in e:
                    if p != n:
                       i.append(p)
            else:
                ap.append(e)
        l.append(i)
        s.append(l)
        a = ap

    print(s)
                
                
                
