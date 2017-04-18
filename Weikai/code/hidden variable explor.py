#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 14:36:29 2017

@author: carrey
探查是否存在隐藏变量
"""
#%%
import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns


#%%
pf_v = pd.read_csv('../../Processed_data/by_weikai/big_train_volume.csv')
pf_v.head()

#%%
pf_v = pf_v[pf_v['precipitation'] == 0]
pf_v.sea_pressure.describe()

#%%
pf_volume = pf_v.groupby(['holiday','weekday','tollgate_id','direction','date','hour',
                          'time_window','weather_hour']).size()\
                            .reset_index().rename(columns = {0:'volume'})
pf_volume.head()

#%%
pf_volume_workday = pf_volume[pf_volume['holiday'] == False]
#pf_volume_workday['direction'] = pf_volume_workday['direction'].apply(str)

#%%
bp = sns.FacetGrid(data = pf_volume_workday,col = 'direction',row = 'weekday'
                   ,size = 8)
bp.map(sns.boxplot, 'hour', 'volume','tollgate_id').add_legend(title = 'tollgate_id')

#%%
dp = sns.FacetGrid(data = pf_volume_workday,col = 'tollgate_id', row = 'weekday', size = 4)
dp.map(sns.distplot, 'volume')

#%%
pf_p = pf_volume_workday.query('hour in [17,18]')

pf_m = pf_volume_workday.query('hour in [8,9]')


#%%
pf_describe = pf_m.groupby(['tollgate_id','direction','weekday']).mean()\
                            .rename(columns = {'volume':'volume_mean'})
                            
pf_describe['volume_std'] = pf_m.groupby(['tollgate_id','direction','weekday'])['volume'].std()\
                            .rename(columns = {'volume':'volume_std'})
                            
pf_describe['volume_median'] = pf_m.groupby(['tollgate_id','direction','weekday'])['volume'].median()\
                            .rename(columns = {'volume':'volume_median'})
                            
pf_describe[['volume_mean','volume_std','volume_median']]

#%%
g = sns.pairplot(pf_volume_workday)

