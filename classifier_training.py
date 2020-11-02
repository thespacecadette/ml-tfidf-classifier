#! /usr/bin/env python
from sklearn.metrics import accuracy_score
from sklearn import svm, datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

import re
import os
import numpy as np

# Global variables
features = list()
labels = list()

# Generic export to file
def readLinesInFile(pathToFileName):
    array = list()
    f = open(pathToFileName, "r")

    for line in f:
        array.append(line)
    f.close()
    print(pathToFileName, array)
    return array
    
def classifier(): 
    # Get targets, labels
    #y_train= readLinesInFile("train/labels.txt")
    #X_train = readLinesInFile("train/words.vocab")
    #y_test = readLinesInFile("test/labels.txt")
    #X_test = readLinesInFile("test/words.vocab")
    features = readLinesInFile("train/words.vocab")
    labels = readLinesInFile("train/labels.txt")

    # Preprocess data
    # In this case it's already split.
    # So samping training data to further split our train/validation data
    X_train, X_test, y_train, y_test = train_test_split(features, features, test_size=0.33, random_state=42)
   
    
    # kNN Classifier
    knn = KNeighborsClassifier(n_neighbors = 3)
    knn.fit(X_train,y_train)
    knn.predict(X_test)
    knnAccuracy = knn.score(X_test, y_test)
    
    print("kNN Accuracy Rate: ", knnAccuracy)

    # K-fold cross validation - find best K
    neighbors = list(range(1, 50, 2))
    
    # empty list that will hold cv scores
    cv_scores = []
    
    # perform 10-fold cross validation
    for k in neighbors:
        knn = KNeighborsClassifier(n_neighbors=k)
        scores = cross_val_score(knn, X_train, y_train, cv=10, scoring='accuracy')
        cv_scores.append(scores.mean())
        
    # Mean Squared error
    mse = [1 - x for x in cv_scores]
    
    # Optimal K
    optimal_k = neighbors[mse.index(min(mse))]
    print("The optimal number of neighbors is {}".format(optimal_k))
    
    # plot misclassification error vs k
    plt.plot(neighbors, mse)
    plt.xlabel("Number of Neighbors K")
    plt.ylabel("Misclassification Error")
    plt.show()
    

    # SVC Model
    #svc = svm.SVC(kernel='linear', C=1.0) # Define SVM model
    #svc.fit(X_train, y_train) # Fit SVM model to the training data
    #Z = svc.predict(X_test) # Make prediciton using SVM model for test data
    #svc_Result = sum(Z==y_test)/float(len(Z))*100
    
    # Decision Tree Model
    #clf=DecisionTreeClassifier(max_depth=10)
    #clf.fit(X_train,y_train) # Train it on training set
    #clf_result = clf.score(X_test, y_test) # Test on test set
    
    #clf=RandomForestClassifier(n_estimators=10,max_depth=16)
    #clf.fit(X_train,y_train) # Train it on training set
    #score = clf.score(X_test, y_test) # Test on test set

    
    #print("SVC Kernal Model\n \n")
    #print("Prediction accuracy = ", svc_Result, "\n \n")
    print("____________________________________________________")
    #print("Decision Tree Model\n \n")
    #print("Prediction accuracy = ", clf_result, "% \n \n")
    print("____________________________________________________")
    #print("Random Forest Classifier Model\n \n")
    #print("Prediction accuracy = ", score, "% \n \n")
    print("____________________________________________________")
    print("____________________________________________________")

classifier()
