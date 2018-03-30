# IntelliMind Assignments

## Assignment 1

### Part1 : Pre-process text data

- In Pre-Processing of text data, Pre-Processing of Data is necessary since it may contain various noises and unwanted data(Ex: Spelling Mistakes)
- So for removing such noises I used some basic python libraries and performed following processing:-

		Split into Sentences
		Split into Words
		Remove all the words that are not alphabetic
		Remove all the Stop Words
		Stemming of words

- The above mentioned processing techniques were possible by using the nltk python library 
- After executing the documents in this code all the documents will become noise free.
- The code for this assignment is attached in the repository named assign_1_1.py


### Part2 : Generate sentiment score for each document [ +ve, -ve, neutral ] 
- For generating the sentiment of the data, I used Navie Bayes Classifier
- For Identifying the positive and negative sentiments of the documents, I trained the Bayes Classifier by creating classes :- 

		positive vocabulary 
		negative vocabulary

- After training the classes of Bayes Classifier I took input of documents one after another and calculated the sentiment score of each document
- The result might not be very much accurate since very less dataset was used for training the classes  
- The code for this assignment is attached in the repository named assign_1_2.py

### Part3 : Perform Named Entity Recognition within text data

- To Perform Named Entity Extraction from the given text document, I used Spacy Library
- Details about this Library can be obtained from the below link

`<link>` : <https://spacy.io/>

- Using this Named Extraction of all the text data can be obtained by the program
- The code for this assignment is attached in the repository named assign_1_3.py


