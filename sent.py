#!/usr/bin/python
import sys
import os
import nltk
from collections import Counter
import csv


# Function to return the file contents as List
def returnList(fileName):
    ''' This function will convert the words in the corresponding file (positive.txt) to Python List of words'''
    wordsList = []
    if os.path.exists(fileName):
        try:
            f = open(fileName)
            lines = f.read()
            linesLower = lines.lower()
            wordsList = linesLower.split()
        except :
            print "Error in Handing File:", fileName
            sys.exit()
    return wordsList


#Counter Initialization

# Using Python Natural Language ToolKit to generate the Sentimental Analysis

#To Count the words in each sentiment 
def getCount(freqDist,sentList):
    '''It is counting the positive and other sentimental words in the given nltk freqdistribution dictionary'''
    count = 0
    for word in sentList:
        if freqDist.has_key(word):
            count += freqDist[word]
    return count


#To Count the words in each sentiment 
def getNegationCount(wordsArticle, freqDist, negationList):
    ''' To get the positive and negative negation counts for the given input after preprocessing'''
    positiveNegCount = 0
    negativeNegCount = 0
    for word in negationList:
        #print word
        if freqDist.has_key(word):
            positiveList = returnList('positive.txt')
            negativeList = returnList('negative.txt')  
            for position, item in enumerate(wordsArticle):
                try:
                    if item == word:
                        if wordsArticle[position+1]:
                            checkWord1 = wordsArticle[position+1]
                            if checkWord1 in positiveList:
                                positiveNegCount += 1
                            if checkWord1 in negativeList:
                                negativeNegCount += 1
                            
                        if wordsArticle[position+2]:
                            checkWord2 = wordsArticle[position+2]
                            if checkWord2 in positiveList:
                                positiveNegCount += 1
                            if checkWord2 in negativeList:
                                negativeNegCount += 1
                                
                        if wordsArticle[position+3]:
                            checkWord3 = wordsArticle[position+3]
                            if checkWord3 in positiveList:
                                positiveNegCount += 1
                            if checkWord3 in negativeList:
                                negativeNegCount += 1 
                except: 
                    pass
                
 
    #print positiveNegCount, negativeNegCount
    return (positiveNegCount, negativeNegCount)



def getArticleCount(split_paper):
    ''' It is converting the each article in to words in a python list and calling the corresponding count functions which will return the counts''' 
    countList = []
    lowerArticle = split_paper.lower() #Converting to lower chars
    wordsArticle = lowerArticle.split() #splitiing each and every word based on delimiters or space
    freqDist = nltk.FreqDist(wordsArticle) # Using nltk to calculate frequency distribution
    
    positiveCount = 0
    negativeCount = 0
    modalWeakCount = 0
    modalStrongCount = 0
    litigiousCount = 0
    uncertaintyCount = 0
    
    negationList = returnList('negation.txt')
    positiveList = returnList('positive.txt') #Callinn returnList fnction to create list of words
    negativeList = returnList('negative.txt')
    modalWeakList = returnList('modal_weak.txt')
    modalStringList = returnList('modal_strong.txt')
    litigiousList = returnList('litigious.txt')
    uncertaintyList =  returnList('uncertainty')

    positiveNegCount, negativeNegCount = getNegationCount(wordsArticle, freqDist, negationList)
    positiveCount = getCount(freqDist,positiveList) #Calling the getCount to get the positive count of a article or title. Below ones are same
    negativeCount = getCount(freqDist,negativeList)
    modalWeakCount = getCount(freqDist,modalWeakList)
    modalStrongCount = getCount(freqDist,modalStringList)
    litigiousCount = getCount(freqDist, litigiousList)
    uncertaintyCount = getCount(freqDist, uncertaintyList)
    
    #Getting the values for each sentiment
    #Printing the values
    #print 'Positive Count:', positiveCount
    #print 'Negative Count:', negativeCount
    #print 'Modal Weak Count:', modalWeakCount
    #print 'Modal Strong Count:', modalStrongCount
    #print 'Litigious Count:', litigiousCount
    #print 'Uncertainty Count:', uncertaintyCount


    countList.append(positiveCount)
    countList.append(negativeCount)
    countList.append(modalWeakCount)
    countList.append(modalStrongCount)
    countList.append(litigiousCount)
    countList.append(uncertaintyCount)
    countList.append(positiveNegCount)
    countList.append(negativeNegCount)
    
    return countList
