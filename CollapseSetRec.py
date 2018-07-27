
import random_slice as randslice
    



def collapse_object(a,n):
    '''
    a is an array of sub arrays, which all have length n

    returns another 2d arrays of the same objects built
    by grouping together similar object sub arrays.

    Ex:
    >>> collapse_object([["A","B"],["A","C"]], 2)
    ["A",["B","C"]]

    This only does a single pass, so it does not group optimally

    Ex:
    #Pass one
    >>> collapse_object( [["A","B"], ["A","C"], ["D","B"], ["D","C"]], 2)
    [['A', ['B', 'C']], ['D', ['B', 'C']]] 
    #Pass two
    collapse_object( [['A', ['B', 'C']], ['D', ['B', 'C']]], 2)
    [ [['A', 'D'], ['B', 'C']] ]

    With two passes we went from 4 groups of objects down to 1
    There are other cases where better results can be achieved
    with even more passes.

    '''
    s = []
    if a == []:#if a is empty return an empty array
        return []
    if n == 0:# if n is 0 then there are no dimensions
        return []
    if n == 1: #if n == 1, then there is only a single dimension and so all elements of a can be collected
        L = []
        for row in a:
            L.append(row[0])#row[0] works because there is only one element per row according to n
        if len(L) > 1:
            #return[L]
            dim = L[0].dimension
            l = []
            for i in L:
                l.append(str(i))
            return [member(l,dim)]
        else:
            return L
    
    most = most_repeated(a)

    for row in a:
        if most in row:
            s.append(row)
    #s = (row for row in a if most in row)
    a[:] = (row for row in a if most not in row)
    for row in s:
        row.remove(most)
    #s now contains all entries with most
    #a now contains all entries withoud most
    final = []
    sub = collapse_object(s,n-1)
    rest = collapse_object(a,n)
    for row in sub:
        if n > 2:
                r = [most]
                for e in row:
                    r.append(e)
                final.append(r)
        else:
            final.append([most,row])
    for row in rest:
        final.append(row)
    return final







def most_repeated(a):
        '''
        a is a 2d array of objects (which must have a __str__ and __repr__ method that ensures uniquesnes)

        d maintains a dictionary of  { str: (object, int) }
        representing the objects name as a key and a tuple of
        the object and number of occurences as the value

        returns the most repeated object in a
        '''
        d = {}
        for e in a:
            for n in e:
                h = str(n)
                if h in d:
                    d[h] = (n,d[h][1] +1)
                else:
                    d[h] = (n,1)
        m = 0
        n = None
        for k in list(d.keys()):
            if d[k][1] > m:
                m = d[k][1]
                n = d[k][0]
        return n

class member:
    def __init__(self,name,d):
        self.name = name
        if type(self.name) == type([]):
            self.name.sort()
        self.dimension = d
    def __str__(self):
        return str(self.name)
    def __repr__(self):
        if type(self.name) != type([]):
            return "'"+ str(self.name) +"'"
        else:
            return str(self.name)
    def __eq__(self,other):
        if type(other.name) != type(self.name):
            return False
        if type(self.name) == type([]):
            if(len(self.name) != len(other.name)):
                return False
            if(self.dimension != other.dimension):
               return False
            return  self.name == other.name
        return (self.name == other.name) and (self.dimension == other.dimension)
        


def reorder_rows(s,n):
    '''
    s is a list of rows of members
    n is the number of members per row
    '''
    final = []
    if n == 1:
        s = [s]
    for row in s:
        final.append(reorder_row(row,n))
    return final


def reorder_row(r,n):
    '''
    r is a list of member objects
    n is the number of objects
    '''
    new_row = [None]*n
    for member in r:
        new_row[member.dimension] = member
    return new_row
    

def objectify(a,n):
    objects = [] 
    for i in range(len(a)):
        cslice = a[i]
        obj = []
        for m in range(n):
            mem = member(cslice[m],m)
            obj.append(mem)
        objects.append(obj)
    return objects



def collapse(a):
    n = len(a[0])
    objects = objectify(a,n)

    results = reorder_rows(collapse_object(objects,n),n)
    lastLen = len(results)
    count = 1
    while len(results) != lastLen or count == 1:#pass over the data again until it is minimal
        lastLen = len(results)
        results = reorder_rows(collapse_object(results,n),n)
        count += 1
    return (count-1, len(results),results)

def print_wide_array(a,w):

    s = ""
    i = 0
    while i < len(a):
        if i%w == 0:
            s+="\n"
        s+=str(a[i])+","
        i += 1
    print(s)
        


        

if __name__ == "__main__":

    d1 = ["Steffen","Alex","Robert","Micheal","Anna","Carah","Max","Janice"]
    d2 = ["Payable","Receivable","Actual","Forecast"]
    d3 = ["CS","MAT","PHY","ART","ENG","CCT"]
    d4 = ["2018","2017","2016","2015","2014","2013","2012","2011"]
    d5 = ["Star Wars","Star Trek","Star Gate"]
    d6 = ["Chrome","FF","IE","Safari","Edge"]
    d7 = ["Task","Review","Report"]
    d8 = ["Edit","View"]
    d9 = ["Online","MAC","C#"]
    d10 = ["Save","Choose","Refresh","Cascade","Drill Transaction","Drill Save","Lids- add","Lids-remove","Lids-select","Lids-move","Log out"]
    d11 = ["Central","Standalone","Hybrid","xlsx","xlsm","xlsb"]
    #a = [d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11]
    #a = [d2,d3,d5,d6,d7,d8,d9,d11]
    #a = [d1,d2,d3,d4]
    #a = [d10,d4]
    a = [d1,d2,d3,d4,d5,d6]
    n = len(a)
    s = 0
    sl = 0
    x = 1
    iterr = 10000
    maxslice = []
    minresults = [None] * (iterr + 1)
    
    for i in range(x):
        slices = randslice.random_slices(a,n,iterr)
        #print ("Zero passes")
        result = collapse(slices)
        s+=result[0]
        sl+=result[1]
        if(result[1] < len(minresults)):
            minresults = result[2]
            maxslice = slices
        print("LEN =:",len(slices),"REDUCED =:",result[1],"REQUIRED =:",result[0])
        
    print(s/x)
    print(sl/x)
    #print("Biggest Difference Original")
    #print_wide_array(maxslice,4)
    #print("Biggest Difference Reduced")
    #print_wide_array(minresults,1)
        





    
        
    


        
