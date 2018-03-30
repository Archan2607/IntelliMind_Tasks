# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 00:00:48 2018

@author: archan
"""

from nltk import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
              
file=[]
text=[]

#taking input of given 10 txt documents

for i in range(10):
    
    text=[]
    file.append(input())
    
    filename = file[i] 
    file1 = open(filename, 'r')
    text = file1.read()
    file1.close()
    # split into sentences
    #from nltk import sent_tokenize
    
    sentences = sent_tokenize(text)
    print(sentences[5])
    
    # split into words
    #    from nltk.tokenize import word_tokenize
    tokens = word_tokenize(text)
    print(tokens[:1000])
    
    # split into words
       # from nltk.tokenize import word_tokenize
    tokens = word_tokenize(text)
    # remove all tokens that are not alphabetic
    words = [word for word in tokens if word.isalpha()]
    print(words[:1000])
    
    
    #    from nltk.corpus import stopwords
    stop_words = stopwords.words('english')
    print(stop_words)
    
    # split into words
    #from nltk.tokenize import word_tokenize
    tokens = word_tokenize(text)
    # stemming of words
     #   from nltk.stem.porter import PorterStemmer
    porter = PorterStemmer()
    stemmed = [porter.stem(word) for word in tokens]
    print(stemmed[:1000])
    
    print("\n")
