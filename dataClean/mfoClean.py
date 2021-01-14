# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 19:41:10 2020

@author: User
"""

import re
import pandas as pd
import csv
'''
def readTable(fileObj):
    #补充代码
    a = []
    for line in fileObj.readlines():
        #line=line.replace('\n','')
        line=line.split(',')
        try: 
            #res = re.search(r'\D?(.*?)[(\]]' ,line[3]).group(1)
            #res1 = re.sub('（*）',"",line[0])
            '''
            #提取出中文地名
            #res1= re.search(r'.*?（' ,line[0]).group()
            res2=re.sub('（.*）',"",line[0])
            a.append(res2)
           
            #提取出英文地名
            
            res3 = re.search(r'.*?（(.*?)）' ,line[0]).group(1)
            if res3 !="":
                a.append(res3)    
            else:
                a.append(" ")
             
            
            #去掉简介前面的.
            res4 = re.sub('·',"",line[1])
            a.append(res4)
           
            #去掉地址前面的<i></i>
            res5 = re.sub('<i></i>',"",line[9]) 
            a.append(res5)
            '''
            res2=re.sub('nan',"",line[3])
            a.append(res2)
            
        except:
             line.append("")
        #a.append(line)          
    return a

fileHandle = open('合并列之后的数据.csv','r',encoding='utf-8')
periodicTable = readTable(fileHandle)

df = pd.DataFrame(periodicTable)
df.to_csv('马蜂窝全部数据(处理后).csv',encoding='utf-8-sig')
fileHandle.close()
'''
