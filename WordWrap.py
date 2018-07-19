#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      322212739
#
# Created:     08/04/2015
# Copyright:   (c) 322212739 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import math
lengthLine=int(input("len"))
line=input("words")
line=line.split()
wordList=[]
for n in line:
    wordList.append(n)
carCount=0
wordCount=0
currentLine=''
for n in range(len(wordList)):
    if (len(wordList[wordCount])+carCount)<=lengthLine:
        currentLine+=wordList[wordCount]
        currentLine+=' '
        carCount+=len(wordList[wordCount])+1
        wordCount+=1
    elif (len(wordList[wordCount])+carCount)>lengthLine:
        if len(wordList[wordCount])>lengthLine:
            currentLine+='\n'
            wordSplit=wordList[wordCount]
            splitCount=0
            for n in range(int(math.ceil(float(len(wordSplit))/lengthLine))):
                currentLine+=wordSplit[splitCount:(splitCount+lengthLine)]
                currentLine+='\n'
                splitCount+=lengthLine
            wordCount+=1
        else:
            currentLine+='\n'
            currentLine+=wordList[wordCount]
            currentLine+=' '
            carCount=len(wordList[wordCount])+1
            wordCount+=1
print(currentLine)
