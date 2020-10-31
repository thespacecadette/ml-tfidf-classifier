# Assignment One

## Feature Extraction
I used `sklearn.feature_extraction` on a subset of data (see: `/test` folder) to ensure I could satisfy the following criteria:
* `wordlist` -> distinct list of words of ALL words in all documents in set.
* `reviews` -> vector count of all reviews that correspond to `N` length to `wordlist`

## Task 1: Feature Extraction

### Requirement 1
I implemented and tested `mapreducer.py` to the WSU SCEM Hadoop server using Hadoop Stream and used `moviesmalldata` as my test set.

`feature-extraction.py` contains my test algorithm for deriving TF-IDF on each word for EACH review of length `N`.

Subset result dump saved in `hadoop_result.feat`

### Requirement 2
`TODO: training_data & training_targets matrices (N x R.length)`

`TODO: test_data test_targets matrices (N x R.length)`

`TODO: Figure out difference between target and data`

`TODO: Run MapReducer to collect target/training data/targets as DATA FRAMES`

## Task 2: Classification

### Requirement 1: Convert to class
Convert ratings to position/negative class variables <= 5 = negative and > 5 positive. 1/0.

### Requirement 2: Normalisation
Normalisation. Classifier result with and without normalisation.

### Requirement 3: Cross Validation
Cross validation on model.

### Requirement 4: Test/Validate model
