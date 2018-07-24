

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
        print(d)
        for e in list(d.keys()):
            if d[e] > m:
                m = d[e]
                n = e
        #n is now the most repeated element
        print(n,m)
        return
                
                
                
