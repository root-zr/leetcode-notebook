# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 08:44:07 2020

@author: User
"""
import pandas as pd 
import re

def my_test(a, b): #用来合并两列字符串数据
   string = ""
   if str(a)== 'nan' and str(b) !='nan':
       string = str(a)
   if str(a)!= 'nan' and str(b) =='nan':
       string = str(b)    
   string = str(a) + str(b)
   if string == 'nannan':
       string = ""
   return string
def test(a,b): #只合并一个有一个没有的情况
    string = ""
    if(pd.isnull(a)==True and pd.isnull(b)==False):
        string = str(b)
        return string
    if(pd.isnull(b)==True and pd.isnull(a)==False):
        string = str(a)
        return string
    if pd.isnull(a)==False and pd.isnull(b)== False:
        return a  #如果两个数据都是非空，默认以去哪儿网为主
    return string
dfGoWhere = pd.read_csv('gowhere.csv',encoding = 'utf-8')
dfBaiKe = pd.read_csv('百科数据.csv',encoding = 'utf-8')
dfMaFenWo = pd.read_csv('马蜂窝数据.csv',encoding = 'utf-8')

print(dfGoWhere )
print(dfBaiKe )
print(dfMaFenWo)

df3 =pd.merge(dfGoWhere , dfBaiKe,on = '名称',how = 'outer')
df2 =pd.merge(df3 , dfMaFenWo,on = '名称',how = 'outer')
df = df2.dropna(axis=1, thresh= 10, inplace=False) #保留10个属性以上的列
print(df)
#df.to_csv('整合后的数据.csv',encoding='utf-8-sig')

'''
df3 = dfGoWhere.combine_first(dfBaiKe)
df = df3.combine_first(dfMaFenWo)
df.to_csv('整合后的数据2.csv',encoding='utf-8-sig')
'''
df['简介'] = df.apply(lambda row: my_test(row['简介_x'], row['简介_y']), axis=1)
df['官网地址网址'] = df.apply(lambda row: test(row['网址_x'], row['网址_y']), axis=1)
df['电话'] = df.apply(lambda row: test(row['电话_x'], row['电话_y']), axis=1)
df['交通'] = df.apply(lambda row: test(row['交通_x'], row['交通_y']), axis=1)
df['门票'] = df.apply(lambda row: my_test(row['门票_x'], row['门票_y']), axis=1)
df['地址'] = df.apply(lambda row: my_test(row['地址_x'], row['地址_y']), axis=1)
df['英文名称'] = df.apply(lambda row: my_test(row['英文名称_x'], row['英文名称_y']), axis=1)
df.to_csv('合并列之后的数据.csv',encoding='utf-8-sig')