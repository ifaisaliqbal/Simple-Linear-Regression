# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 19:24:53 2019

@author: iqbal
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Salary_Data.csv");

X = data.iloc[:,:-1].values;
y = data.iloc[:,1].values;

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.2, random_state = 0 )

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,y_train)

y_pred = regressor.predict(X_test)