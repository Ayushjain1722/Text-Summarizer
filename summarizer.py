import nltk 
from nltk.corpus import stopwords
import csv
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize, sent_tokenize
import pandas as pd
from nltk.stem import PorterStemmer
import math


def cuePhrasesCalc(sent_tokens, word_tokens):
    QPhrases = ['examples', 'anyway', 'furthermore', 'first', 'second', 'then', 'now', 'therefore', 'hence', 'lastly', 'finally', 'summary']
    cuePhrases = {}
    for sentence in sent_tokens:
        cuePhrases[sentence] = 0
        word_tokens = nltk.word_tokenize(sentence)
        for word in word_tokens:
            if word.lower() in QPhrases:
                cuePhrases[sentence] += 1
    maximumFreq = max(cuePhrases.values())
    for k in cuePhrases.keys():
        try:
            cuePhrases[k] = maximumFreq/cuePhrases[k]
            cuePhrases[k] = round(cuePhrases[k], 3)
        except ZeroDivisionError:
            x = 0
    return cuePhrases

def numericDataCalc(sent_tokens, word_tokens):
    numericData = {}
    for sentence in sent_tokens:
        numericData[sentence] = 0
        word_tokens = nltk.word_tokenize(sentence)
        for word in word_tokens:
            if word.isdigit():
                numericData[sentence] += 1
    maximumFreq = max(numericData.values())
    for k in numericData.keys():
        try:
            numericData[k] = numericData[k]/maximumFreq
            numericData[k] = round(numericData[k],3)
        except ZeroDivisionError:
            x = 0
    return numericData

def sentLenCalc(sent_tokens, word_tokens):
    # if sentence is less than 10 words, reduce 5% value of that sentence
    # if sentence is 10 to 20 words, keep maimum weight i.e. 1
    # if sentence is greater than 20 words, reduce 5% value of that sentence
    sentLenScore = {}
    for sentence in sent_tokens:
        sentLenScore[sentence] = 0
        word_tokens = nltk.word_tokenize(sentence)
        if len(word_tokens) < 10:
            sentLenScore[sentence] = 1 - 0.05*(10-len(word_tokens))
            sentLenScore[sentence] = round(sentLenScore[sentence],4)
        elif len(word_tokens) > 20:
            sentLenScore[sentence] = 1 - 0.05*(len(word_tokens)-20)
            sentLenScore[sentence] = round(sentLenScore[sentence],4)
        else:
            sentLenScore[sentence] = 1 
    return sentLenScore

def sentencePositionCalc(sent_tokens):  
    sentencePosition = {}
    d = 1 #Sentence number
    no_of_sentences = len(sent_tokens)
    for i in range(no_of_sentences):
        a = 1/d
        b = 1/(no_of_sentences-d+1)
        sentencePosition[sent_tokens[d-1]] = max(a,b)
        sentencePosition[sent_tokens[d-1]] = round(sentencePosition[sent_tokens[d-1]],3)
        d = d+1
    return sentencePosition

def freqTableCalc(word_tokens_refined, sent_tokens, ps):
    freqTable = {}
    for word in word_tokens_refined:
        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1
    for word in freqTable.keys():
        freqTable[word] = math.log10(freqTable[word]+1)
        freqTable[word] = round(freqTable[word],3)
    
    #Calculate sentence score according to word frequency
    wordFreq = {}
    for sentence in sent_tokens:
        wordFreq[sentence] = 0
        word_tokens = nltk.word_tokenize(sentence)
        f = []
        for word in word_tokens:
            f.append(ps.stem(word))
        for word,freq in freqTable.items():
            if word in f:
                wordFreq[sentence] += freq
    return wordFreq

def upperCaseCalc(sent_tokens, word_tokens):
    upperCase = {}
    for sentence in sent_tokens:
        upperCase[sentence] = 0
        word_tokens = nltk.word_tokenize(sentence)
        for word in word_tokens:
            if word.isupper():
                upperCase[sentence] += 1
    maxFreq = max(upperCase.values())
    for k in upperCase.keys():
        try:
            upperCase[k] = upperCase[k]/maxFreq
            upperCase[k] = round(upperCase[k],3)
        except ZeroDivisionError:
            x = 0
    return upperCase

def properNounCalc(sent_tokens):
    nltk.download('averaged_perceptron_tagger')
    properNoun = {}
    for sentence in sent_tokens:
        tagged_sent = pos_tag(sentence.split())
        propernouns = [word for word,pos in tagged_sent if pos=='NNP']
        properNoun[sentence] = len(propernouns)
    maxFreq = max(properNoun.values())
    for k in properNoun.keys():
        try:
            properNoun[k] = properNoun[k]/maxFreq
            properNoun[k] = round(properNoun[k],3)
        except ZeroDivisionError:
            x = 0
    return properNoun

def headMatchCalc(sent_tokens, stopWords, ps):
    headMatch = {}
    heading = sent_tokens[0]
    for sentence in sent_tokens:
        headMatch[sentence] = 0
        word_tokens = nltk.word_tokenize(sentence)
        for k in word_tokens:
            if k not in stopWords:
                k = ps.stem(k)
                if k in ps.stem(heading):
                    headMatch[sentence] += 1
    maxFreq = max(headMatch.values())
    for k in headMatch.keys():
        try:
            headMatch[k] = headMatch[k]/maxFreq
            headMatch[k] = round(headMatch[k],3)
        except ZeroDivisionError:
            x = 0
    return headMatch

def getSummary(cuePhrases, numericData, sentLenScore, sentencePosition, wordFreq, upperCase, properNoun, headMatch, sent_tokens):
    totalScore = {}
    for k in cuePhrases.keys():
        totalScore[k] = cuePhrases[k] + numericData[k] + sentLenScore[k] + sentencePosition[k] + wordFreq[k] + upperCase[k] + properNoun[k] + headMatch[k]
    sumValues = 0
    for sentence in totalScore:
        sumValues += totalScore[sentence]
    average = sumValues/len(totalScore)
    
    # Storing sentences into summary
    summary = ''
    for sentence in sent_tokens:
        if sentence in totalScore and totalScore[sentence] > (1.5*average):
            summary += ""+sentence
    
    return summary


def summarize(text):

    sent_tokens = nltk.sent_tokenize(text)
    word_tokens = nltk.word_tokenize(text)
    word_tokens_lower = [word.lower() for word in word_tokens]
    stopWords = list(set(stopwords.words('english')))
    word_tokens_refined = [x for x in word_tokens_lower if x not in stopWords]

    stem = []
    ps = PorterStemmer()
    for word in word_tokens_refined:
        stem.append(ps.stem(word))
    word_tokens_refined = stem

    #Feature extraction
    cuePhrases = cuePhrasesCalc(sent_tokens, word_tokens)
    numericData = numericDataCalc(sent_tokens, word_tokens)
    sentLenScore = sentLenCalc(sent_tokens, word_tokens)
    sentencePosition = sentencePositionCalc(sent_tokens)
    wordFreq = freqTableCalc(word_tokens_refined, sent_tokens, ps)
    upperCase = upperCaseCalc(sent_tokens, word_tokens)
    properNoun = properNounCalc(sent_tokens)
    headMatch = headMatchCalc(sent_tokens, stopWords, ps)

    # Compiling all features to get the final summary
    summary = getSummary(cuePhrases, numericData, sentLenScore, sentencePosition, wordFreq, upperCase, properNoun, headMatch, sent_tokens)
    return summary

## Program to check direct run of the program.
if __name__ == "__main__":
    text = '''Success from two leading coronavirus vaccine programs likely means other frontrunners will also show strong protection against COVID-19, Bill Gates said Tuesday.

The fact that two coronavirus vaccines recently showed strong protection against COVID-19 bodes well for other leading programs led by AstraZeneca, Novavax, and Johnson & Johnson, Bill Gates said Tuesday.The billionaire Microsoft founder and philanthropist said it will be easier to boost manufacturing and distribute these other shots to the entire world, particularly developing nations.The vaccine space has seen a flurry of good news in recent days, marked by overwhelming success in late-stage trials by both Pfizer and Moderna. The studies showed both vaccines provided strong protection against the virus compared to a placebo. "With the very good news from Pfizer and Moderna, we think it's now likely that AstraZeneca, Novavax, and Johnson & Johnson will also likely show very strong efficacy," Gates told journalist Andrew Ross Sorkin. 
While Gates didn't delve into the scientific rationale behind that prediction, many scientists hold the same hope. All the leading vaccine candidates target the same part of the coronavirus in the spike protein. Early-stage clinical trials showed all the shots elicited varying levels of neutralizing antibodies, virus-fighting proteins that play a critical role in the body's immune response. But the only way to know if that translates to protection is by running late-stage trials that enroll tens of thousands for volunteers who receive either the experimental shot or placebo injections. The scientific success has turned the top challenges surrounding a COVID-19 vaccine to the manufacturing and distribution front. Gates noted that the world will be supply constrained for 2021, but these additional vaccines will prove valuable on that front.'''
    print(summarize(text))