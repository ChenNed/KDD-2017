#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 15:14:02 2017

@author: carrey
"""
#%%
import pandas as pd


#%%
train = pd.read_csv("../../processed_data/by_weikai/processed_train_volume.csv")
test = pd.read_csv("../../processed_data/by_weikai/processed_test_volume.csv")
train_weather = pd.read_csv("../../processed_data/by_weikai/processed_train_weather.csv")
test_weather = pd.read_csv("../../processed_data/by_weikai/processed_test_weather.csv")
#%%
train.head()

#%%
new_train = train.groupby(['tollgate_id','direction','date','time_window',
                           'weekday','holiday','weather_hour']).size().\
                            reset_index().rename(columns = {0:'volume'})
                            
new_test = test.groupby(['tollgate_id','direction','date','time_window',
                           'weekday','holiday','weather_hour']).size().\
                            reset_index().rename(columns = {0:'volume'})

new_test.head()
#%%
big_train = pd.merge(new_train,train_weather,how = 'left', on = ['date','weather_hour'])
big_test = pd.merge(new_test,test_weather,how = 'left', on = ['date','weather_hour'])
del big_test['weather_hour']
del big_train['weather_hour']
big_train.head()

#%%
train_1_0 = big_train.query('tollgate_id == 1 and direction == 0')
train_1_1 = big_train.query('tollgate_id == 1 and direction == 1')
train_2_0 = big_train.query('tollgate_id == 2 and direction == 0')
train_3_0 = big_train.query('tollgate_id == 3 and direction == 0')
train_3_1 = big_train.query('tollgate_id == 3 and direction == 1')

test_1_0 = big_test.query('tollgate_id == 1 and direction == 0')
test_1_1 = big_test.query('tollgate_id == 1 and direction == 1')
test_2_0 = big_test.query('tollgate_id == 2 and direction == 0')
test_3_0 = big_test.query('tollgate_id == 3 and direction == 0')
test_3_1 = big_test.query('tollgate_id == 3 and direction == 1')

test_3_1.head()

#%%
train_1_0.to_csv('../../Processed_data/by_weikai/train_1_0_volume.csv', index = False)
train_1_1.to_csv('../../Processed_data/by_weikai/train_1_1_volume.csv', index = False)
train_2_0.to_csv('../../Processed_data/by_weikai/train_2_0_volume.csv', index = False)
train_3_0.to_csv('../../Processed_data/by_weikai/train_3_0_volume.csv', index = False)
train_3_1.to_csv('../../Processed_data/by_weikai/train_3_1_volume.csv', index = False)

test_1_0.to_csv('../../Processed_data/by_weikai/test_1_0_volume.csv', index = False)
test_1_1.to_csv('../../Processed_data/by_weikai/test_1_1_volume.csv', index = False)
test_2_0.to_csv('../../Processed_data/by_weikai/test_2_0_volume.csv', index = False)
test_3_0.to_csv('../../Processed_data/by_weikai/test_3_0_volume.csv', index = False)
test_3_1.to_csv('../../Processed_data/by_weikai/test_3_01volume.csv', index = False)



