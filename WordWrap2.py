

import math


def word_wrap(line,lengthLine):
    inserts = []
    for n in range(len(line)):
        if n%lengthLine == 0 and n!=0:
            #find the first white space behind n
            index = n
            if(not line[n].isspace()):
                for i in range(n-lengthLine,n,1):
                    if line[i].isspace():
                        index = i
            inserts.append(index)
            
    inserts.reverse()
    for index in inserts:
        line = line[:index] + "\n" + line[index:]

    lines = line.split("\n")
    newLine = ""
    for l in lines:
        if l[0].isspace():
            l = l[1:]
        newLine += l+"\n"
    return newLine



    
