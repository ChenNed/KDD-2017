#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 17:19:04 2017

@author: carrey
"""

import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from feature_format import feature_format
from sklearn.model_selection import cross_val_score
from sklearn.metrics.scorer import make_scorer

x_train, x_test, y_train, y_test = feature_format(task = 2)

def MAPE(y_true, y_pred):
    return np.mean(np.abs((y_true - y_pred) / y_true))

score = make_scorer(MAPE, greater_is_better=False)

rng = np.random.RandomState(1)
regr = AdaBoostRegressor(DecisionTreeRegressor(max_depth = 5),
                         n_estimators=50, random_state = rng)

#regr.fit(x_train, y_train)
#
#y_pred = regr.predict(x_test)
#
#mape = np.mean(np.abs((y_pred - y_test)/y_test))
#
#print mape
#print x_test
#
#print y_pred,y_test


lr = LinearRegression()

test_score = cross_val_score(regr, x_train, y_train, cv=10, scoring=score)

print test_score
