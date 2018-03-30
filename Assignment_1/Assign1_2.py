# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 12:46:42 2018

@author: archan
"""


import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import names
 
def word_feats(words):
    return dict([(word, True) for word in words])
 
positive_vocab = [ 'awesome', 'outstanding', 'fantastic', 'terrific', 'good', 'nice', 'great', ':)' ]
negative_vocab = [ 'bad', 'terrible','useless', 'hate', ':(','sad','cry' ]
neutral_vocab = [ 'movie','the','sound','was','is','actors','did','know','words','not' ]
 
positive_features = [(word_feats(pos), 'pos') for pos in positive_vocab]
negative_features = [(word_feats(neg), 'neg') for neg in negative_vocab]
neutral_features = [(word_feats(neu), 'neu') for neu in neutral_vocab]
 
train_set = negative_features + positive_features + neutral_features
 
classifier = NaiveBayesClassifier.train(train_set) 

file=[]
text=[]

for i in range(10):
    
    text=[]
    file.append(input())
    # Predict
    neg = 0
    pos = 0
    filename = file[i] 
    file1 = open(filename, 'r')
    text = file1.read().split()
    file1.close()
    
    # split into words by white space
    #sentence = sentence.lower()
    
    for word in text:
        classResult = classifier.classify(word_feats(word))
        if classResult == 'neg':
            neg = neg + 1
        if classResult == 'pos':
            pos = pos + 1
            
    posfreq=str(float(pos)/len(text))
    
    negfreq=str(float(neg)/len(text))
    
    print('Positive: ' + posfreq)
    print('Negative: ' + negfreq)
     
    if posfreq>negfreq:
        print('Document is Positive with Score:'+posfreq)
    elif negfreq>posfreq:
            print('Document is Negative with Score:'+negfreq)
    else:
        print('Document is Neutral')
            
    print("\n")
    
