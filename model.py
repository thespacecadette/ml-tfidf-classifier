from sklearn.svm import LinearSVC, SVC
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import seaborn as sns
from mlxtend.plotting import plot_decision_regions


train_features = []
train_labels = []

# Split training/test data
train_test_split()

classifier = SVC()
classifier.fit(train_features, train_labels)
