# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 00:26:58 2018

@author: prateek
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

# Importing the dataset
dataset = pd.read_csv('iris.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values.reshape(150,1)

labelencoder_y = LabelEncoder()
y[:, 0] = labelencoder_y.fit_transform(y[:, 0])


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

X_train, X_test, y_train, y_test = X_train.astype(np.float64),X_test.astype(np.float64), y_train.astype(np.float64), y_test.astype(np.float64)


from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=2)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)


accuracy_score(y_test, y_pred)