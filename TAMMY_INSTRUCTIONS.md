# Assignment One

## PLEASE NOTE: 

You will need to run the following first to preprocess data: 
1. `feature-extraction.py` and uncomment all the lines from `Line 125`. Current state is that not all test data has been preprocessed. Please also ensure `train` and `test` folders are present before you run. 

## Feature Extraction
I used `sklearn.feature_extraction` on a subset of data (see: `/test` folder) to ensure I could satisfy the following criteria:
* `wordlist` -> distinct list of words of ALL words in all documents in set.
* `reviews` -> vector count of all reviews that correspond to `N` length to `wordlist`

## Task 1: Feature Extraction

### Requirement 1
I implemented and tested `mapreducer.py` to the WSU SCEM Hadoop server using Hadoop Stream and used `moviesmalldata` as my test set.

`feature-extraction.py` contains my test algorithm for deriving TF-IDF on each word for EACH review of length `N`.

Subset result dump saved in `hadoop_result.feat`. Couldn't find a way to save files from Hadoop Server to my local machine (attempted setting up my own server, but ran into plenty of issues). Therefore, `feature-extraction.py` extracts all words, review vectors (with TFIDF values) in `[train/test]/[train/test]-[positive/negative].feat` files. 

### Requirement 2

In `feature-extraction.py` you will need to uncomment `generateData()` and `mergeFiles()` to generate the train/test data. 

Once this is done, open `traintest_set.py` and run to generate training data.

## Task 2: Classification

### Requirement 1: Convert to class
This was completed on `feature-extraction.py` and exported files were `train/labels.txt` and `test/labels.txt`. 
Convert ratings to position/negative class variables <= 5 = negative and > 5 positive. 1/0.

### Requirement 2: Normalisation
Normalisation. Classifier result with and without normalisation.

### Requirement 3: Cross Validation
This was completed in `classifier_training.py`.

### Requirement 4: Test/Validate model
This was completed in `classifier_training.py`.
