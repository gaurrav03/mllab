# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 00:08:40 2018

@author: prateek
"""
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris

iris_dataset=load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris_dataset["data"], iris_dataset["target"], random_state=0)

X_train, X_test, y_train, y_test = X_train.astype(np.float64),X_test.astype(np.float64), y_train.astype(np.float64), y_test.astype(np.float64)



from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
y_pred = gnb.fit(X_train, y_train).predict(X_test)


accuracy_score(y_test, y_pred)