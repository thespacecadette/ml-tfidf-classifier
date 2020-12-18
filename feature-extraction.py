#! /usr/bin/env python
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import matplotlib.pyplot as plt

import re
import os

# Global variables
wordlist = list()
reviews = list()
tfidf = list()
features = list()
labels = list()

def setRating(fileName):
    fileNameArray = fileName.split("_")
    rating = fileNameArray[1][:1]
    
    return rating
    
def getTFIDFFromWord(word, reviews, BoW):
    tfidfIndex = 0
    for w in BoW:
        if(w == word):
            return reviews[tfidfIndex]

# Generic export to file
def save(nameOfFile, path, array):
    fullPath = path + nameOfFile
    f = open(fullPath, "a")

    for tf in array:
        print("saving ... ", tf)
        f.write(str(tf) + "\n")
    f.close()

def convertToClassLabel(fileName):
   	rating = setRating(fileName)

   	if int(rating) > 5:
           return 1
    
   	return 0

def getWordList(path, files): 
    # Get vocabulary of words
    for f in files:
    	file = open((path + f), "r", errors='ignore')
    	Review = file.readlines()
        
    	for line in Review:
    		tokenise = re.split("[^a-zA-Z0-9']", line)
    		#print(tokenise)
    		reviews.append(line)
            	
    		for word in tokenise:
    			if word.lower() not in wordlist:
    				wordlist.append(word.lower())
                
    				convertedLabel = convertToClassLabel(file.name)
    				labels.append(convertedLabel)

    return wordlist

def performTFIDF(vectorizer):
    reviewsCount = vectorizer.fit_transform(reviews).toarray()
       
    transformer = TfidfTransformer(smooth_idf=False)
    return transformer.fit_transform(reviewsCount).toarray()

def summary(feature_names):
    print("____________________________________________________")
    print("SUMMARY: TF-IDF")
    print("words length N = ", feature_names.__len__(),"\n\n")
    print("TF-IDF of BoW \n", tfidf, "\n \n")
    print("Features = ", feature_names, "\n \n")
    print("____________________________________________________")


def mergeFiles(mergeFileOne, mergeFileTwo, fileToMergeTo):
    data = data2 = "" 
  
    # Reading data from file1     
    with open(mergeFileOne) as fp: 
        data = fp.read() 
      
    # Reading data from file2 
    with open(mergeFileTwo) as fp: 
        data2 = fp.read() 
      
    # Merging 2 files 
    # To add the data of file2 
    # from next line 
    data += "\n"
    data += data2 
      
    with open (fileToMergeTo, 'w') as fp: 
        fp.write(data) 

    
def generateData(pathToData, fileToSaveTo, directoryToSaveTo, type):    
    # Subset test data
    files = os.listdir(pathToData)
    
    vocabulary = getWordList(pathToData, files)
    
    vectorizer = CountVectorizer(vocabulary=vocabulary, stop_words="english", encoding="windows-1252", analyzer="word", lowercase=True)
    tfidf = performTFIDF(vectorizer)
    features = vectorizer.get_feature_names();

    # Write tfidf matrix to file
    save(fileToSaveTo, directoryToSaveTo, tfidf)
    
    # Write BoW
    save(type + "-words.vocab", directoryToSaveTo, features)
    
    # Save labels
    save(type + "-labels.txt", directoryToSaveTo, labels)

    print("Lengths: ", labels.__len__(), features.__len__())

    summary(vectorizer.get_feature_names())


# Preprocessing
#generateData("aclImdb/train/pos/", "train-positive.feat", "train/", "pos")
#generateData("aclImdb/train/neg/", "train-negative.feat", "train/", "neg")
#generateData("aclImdb/test/pos/", "test-positive.feat", "test/", "pos")
#generateData("aclImdb/test/neg/", "test-negative.feat", "test/", "neg")
mergeFiles("train/train-negative.feat", "train/train-positive.feat", "train/train.feat")
mergeFiles("train/neg-words.vocab", "train/pos-words.vocab", "train/words.vocab")
mergeFiles("test/test-negative.feat", "test/test-positive.feat", "test/test.feat")
mergeFiles("test/neg-words.vocab", "test/pos-words.vocab", "test/words.vocab")
mergeFiles("train/neg-labels.txt", "train/pos-labels.txt", "train/labels.txt")
mergeFiles("test/neg-labels.txt", "test/pos-labels.txt", "test/labels.txt")

