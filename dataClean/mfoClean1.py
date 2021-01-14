# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 16:20:45 2020

@author: User
"""

import pandas as pd 

data = pd.read_json('马蜂窝全部数据(1).json',encoding = 'utf-8')
df = pd.DataFrame(data)
print(df)
df2 = df.dropna(axis=1, thresh= 5, inplace=False)
#print(df2)
#clean = df.dropna(thresh = 80)
#print(clean)
#fw = open("百科数据.csv","w")
'''
df2 = pd.DataFrame(df.values.T, index=df.columns, columns=df.index)
df2.to_csv('马蜂窝全部数据(未处理）.csv',encoding='utf-8-sig')
'''
df3 = pd.DataFrame(df2.values.T, index=df2.columns, columns=df2.index)
df3.to_csv('马蜂窝全部数据(1).csv',encoding='utf-8-sig')
#print(data)