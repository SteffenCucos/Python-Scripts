

def collapse(a,n=0):

    if n == 0:
        return []
    
    s = []
    most = most_repeated(a)
    for row in a:
        if most in row:
            row.remove(most)
            s.append(row)
    for row in s:
        print(row,s)
        row.remove(most)
    #s now contains all entries with most removed
    l = [most,collapse(s,n-1)]
    print(l)








def most_repeated(a):
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
        return n
