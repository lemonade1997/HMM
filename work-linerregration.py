#-*- coding:utf-8 -*- 
 
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from pandas import DataFrame,Series
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
 
#读取文件
#datafile='E:\\xhyxx\\work2\\good-t.xlsx'#优
#datafile='E:\\xhyxx\\work2\\soso-t.xlsx'#良
datafile='E:\\xhyxx\\work2\\bad-t.xlsx'#差
data = pd.read_excel(datafile)#datafile是excel文件，所以用read_excel,如果是csv文件则用read_csv
examDf = DataFrame(data)
 
#数据清洗,要哪些列取哪些列
#new_examDf = examDf.ix[:,[2,4,5,6,7,8,9]]
new_examDf = examDf.ix[:,[4,6,7,8,9,10]]
''' 
#检验数据
print(new_examDf.describe())#数据描述，会显示最值，平均数等信息，可以简单判断数据中是否有异常值
print(new_examDf[new_examDf.isnull()==True].count())#检验缺失值，若输出为0，说明该列没有缺失值 
''' 
#输出相关系数，判断是否值得做线性回归模型
print(new_examDf.corr())#0-0.3弱相关；0.3-0.6中相关；0.6-1强相关；
