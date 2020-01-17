#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 12:41:33 2019

@author: omicon
"""
#kernel SVM

# Importing the libraries
#import numpy as np
#import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('csv_result-Autism-Adult-Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 21].values

# ubah nilai yang belum numerik
from sklearn.preprocessing import LabelEncoder
encode = LabelEncoder()
for i in range (1, (X.shape[1])):
    X[:,i] = encode.fit_transform(X[:,i])
y = encode.fit_transform(y)

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)

# Gaussian Kernel
from sklearn.svm import SVC
classifier = SVC(kernel = 'rbf', random_state = 0, gamma='auto')
classifier.fit(X_train, y_train)

# Polynomial Kernel
# from sklearn.svm import SVC
# classifier = SVC(kernel = 'poly', degree=8)
# classifier.fit(X_train, y_train)

# # Sigmoid Kernel
# from sklearn.svm import SVC
# classifier = SVC(kernel = 'sigmoid')
# classifier.fit(X_train, y_train)

# Hasil Prediksi
y_pred = classifier.predict(X_test)
# presentasi performa
performa = classifier.score(X_test, y_test)

# Confusion Matrix dan Classification Report
from sklearn.metrics import confusion_matrix, classification_report
cm = confusion_matrix(y_test, y_pred)
cr = classification_report(y_test, y_pred)

# k-fold cross validation untuk menghindari overfitting
from sklearn.model_selection import cross_val_score, train_test_split
skor = cross_val_score(classifier, X, y, cv=10)
rata2_skor = skor.mean()
std_var = skor.std()

# improve model dengan grid search
from sklearn.model_selection import GridSearchCV
parameters = [
        {'C':[1,10,100,1000],'kernel':['linear']},
        {'C':[1,10,100,1000],'kernel':['rbf'], 'gamma':[0.5, 0.1, 0.01, 0.001]},
        ]
gridsearch = GridSearchCV(estimator = classifier, param_grid = parameters, scoring ='accuracy', 
                          cv = 10, n_jobs = -1)
gridsearch = gridsearch.fit(X_train, y_train)
akurasi_tertinggi = gridsearch.best_score_
parameter_terjoss = gridsearch.best_params_
