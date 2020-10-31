#! /usr/bin/env python
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

import re
import os
import numpy as np

# Subset test data
path = 'test/'
files = os.listdir(path)

# Global variables
resultBow = list()
wordlist = list()
reviews = list()
ratings = list()

# Export BoW as .feat files
def formatReviewsMatrix(reviewsCount, BoW, reviews):
    matrix = list()
    reviewIndex = 0
    
    for reviewVector in reviewsCount:
        row = ""
        
        rowTail = ""
        colIndex = 0
        for tf in reviewVector:
            rowTail = rowTail + " " + str(colIndex) + ":" + str(tf) + " "
            colIndex = colIndex + 1
        
        row = row + ratings[reviewIndex] + " " + rowTail + ""
        reviewIndex = reviewIndex + 1
        matrix.append(row)
        
    return matrix

def addRating(fileName):
    fileNameArray = fileName.split("_")
    rating = fileNameArray[1][:1]
    ratings.append(rating)
    
def getTFIDFFromWord(word, reviews, BoW):
    tfidfIndex = 0
    for w in BoW:
        if(w == word):
            return reviews[tfidfIndex]

print("____________________________________________________")
print("______________   TF-IDF Reviews  ___________________")
print("____________________________________________________")

# Get vocabulary of words
for f in files:
	file = open((path + f), "r", encoding="windows-1252")
	Review = file.readlines()

	# Get rating from filename
	addRating(file.name)

	for line in Review:
		tokenise = re.split("[^a-zA-Z0-9']", line)
		#print(tokenise)
		reviews.append(line)
	
		for word in tokenise:
			if word.lower() not in wordlist:
				wordlist.append(word.lower())

vectorizer = CountVectorizer(vocabulary=wordlist, stop_words="english", encoding="windows-1252", analyzer="word")
reviewsCount = vectorizer.fit_transform(reviews).toarray()
BoW = vectorizer.get_feature_names();
   
transformer = TfidfTransformer(smooth_idf=False)
tfidf = transformer.fit_transform(reviewsCount).toarray()

outputMatrix = formatReviewsMatrix(tfidf, BoW, reviews)

reviewIdx = 0
for review in reviews:
   print("____________________________________________________")
   print("\n Review: \n" + outputMatrix[reviewIdx] + "\n")
   print("Review N length = ", vectorizer.get_feature_names().__len__())
   reviewIdx = reviewIdx + 1

print("____________________________________________________")
print("____________________________________________________")
print("SUMMARY: TF-IDF")
print("wordlist N length = ", wordlist.__len__(),"\n\n")
print("TF-IDF of BoW \n", tfidf, "\n \n")
print("BoW = ", BoW, "\n \n")
print("Output Matrix \n", outputMatrix)
print("____________________________________________________")
print("____________________________________________________")