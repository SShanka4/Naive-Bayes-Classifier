# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import numpy as np
import math
from scipy.sparse import *
from sklearn import datasets
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier
from pandas import DataFrame

#Reading the train and test data from the file and storing it in an object
trainData = pd.read_csv('train.data', sep=' ',header=None,names=['docId','wordId','count'])
trainLabels = pd.read_csv('train.label')

testData = pd.read_csv('test.data', sep=' ',header=None,names=['docId','wordId','count'])
testLabels = pd.read_csv('test.label')



df = pd.DataFrame(data=0, index = np.arange(11268), columns = np.arange(53976))


#Creating sparse matrix for training data
length=0
inner=0
index=0
Doclength = len(set(trainData.wordId))
for i in range (11267):
    df.set_value([trainData.docId[i]], [trainData.wordId[i]], 1)  
    
#Using Decision Tree classifier to model the data
model = DecisionTreeClassifier()
model.fit(df,trainLabels)
print("Model is -")
print("Prediction is - ")

#Trimming the test data contents and freeing the memory
testData = testData[(testData.wordId.isin(trainData.wordId))]
trainData=None
trainLabels=None
testLabels=None
df=None
del index
del length
del testLabels
ef=pd.DataFrame(data=0, index = np.arange(11268), columns = np.arange(53976))

#Using Naive Bayes classifier to predict
for j in range(11267):
    ef.set_value([j],[testData.wordId[j]],1)
from sklearn.naive_bayes import BernoulliNB
bernaulli = BernoulliNB()
bernaulli.fit(df, trainLabels)
BernoulliNB(alpha=0.0, binarize=0.0, class_prior=None, fit_prior=True)
print(clf.predict(ef))
