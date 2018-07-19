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


def word_wrap(line,lengthLine):
    '''
    Line = text to be parsed
    lengthLine = max number of characters in any given line of the output

    returns Line with inserted "\n"

    inserts "\n" newline characters at or before lengthLine
    character intervals inorder to preserve whole words if possible
    '''
    
    wordList = line.split()
    carCount = 0
    wordCount = 0
    currentLine = ''
    for n in range(len(wordList)):
        
        word = wordList[wordCount]
        wordLen = len(word)
        
        if (wordLen+carCount) <= lengthLine:
            currentLine += word
            currentLine += ' '
            carCount += wordLen+1
            wordCount += 1
        elif (wordLen+carCount) > lengthLine:
            if wordLen > lengthLine:
                currentLine += '\n'
                wordSplit = word
                splitCount = 0
                for n in range(int(math.ceil(float(len(wordSplit))/lengthLine))):
                    currentLine += wordSplit[splitCount:(splitCount+lengthLine)]
                    currentLine += '\n'
                    splitCount += lengthLine
                wordCount += 1
            else:
                currentLine += '\n'
                currentLine += word
                currentLine += ' '
                carCount = wordLen+1
                wordCount += 1
    return currentLine
