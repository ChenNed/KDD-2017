#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 17:19:04 2017

@author: carrey
"""

import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import AdaBoostRegressor
import matplotlib.pyplot as plt
from feature_format import feature_format
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_regression

x_train, x_test, y_train, y_test = feature_format(task = 2)


#%%
rng = np.random.RandomState(1)
regr = AdaBoostRegressor(DecisionTreeRegressor(max_depth = 2),
                         n_estimators=10, random_state = rng)

regr.fit(x_train, y_train)

y_pred = regr.predict(x_test)

mape = np.mean(np.abs((y_pred - y_test)/y_test))

#print x_test
print mape

#print y_pred,y_test