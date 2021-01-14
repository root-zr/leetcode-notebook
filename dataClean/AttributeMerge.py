# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 11:24:35 2020

@author: User
"""

import pandas as pd 
import re
import csv
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

df = pd.read_csv('合并列之后的数据.csv',encoding = 'utf-8')

'''
a = []
b = []
for i in range(0,3186):
    #print(df['简介'].loc[i])
    res2= re.sub('nan',"",str(df['门票'].loc[i]))
    a.append(res2)
    res3= re.sub('nan',"",str(df['地址'].loc[i]))
    b.append(res3)
df = pd.DataFrame(a)
df2 = pd.DataFrame(b)
df.to_csv('test.csv',encoding='utf-8-sig')
df2.to_csv('test2.csv',encoding='utf-8-sig')
'''

#除去重复的行
'''
a = []
a.append(df['名称'].duplicated())
dfs = pd.DataFrame(a)
df3 = pd.DataFrame(dfs.values.T, index=dfs.columns, columns=dfs.index)
df3.to_csv('test.csv',encoding='utf-8-sig')
'''

# 读入数据
path = '合并列之后的数据.csv'   #因为drop()函数不会在原数据上做修改，所以用元组的形式来做
with open(path, "r",encoding =  'utf-8') as f:
    reader = csv.reader(f)
    content = [row for row in reader]

# 转为numpy
#content_array = np.array(content)

#print(content)
for i in range(0,3185):
    if df['flag'].loc[i] == True:
        try:
            #print(content[i])
            #content.remove(content[i])
            df =  df.drop(index=[i])
        except:
            print('第{0}条数据处理失败'.format(i))
        
        #print(i)
        #df2 =  df2.drop(index=[i])
#df2 = df['名称'].drop_duplicates()
#df = pd.DataFrame(content)
df.to_csv('合并列之后的数据2.csv',encoding='utf-8-sig')
