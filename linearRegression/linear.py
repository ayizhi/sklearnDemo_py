#coding:utf-8
import numpy as np
import pandas as pd
from pandas import DataFrame,Series
from sklearn import linear_model

#读取数据
data = DataFrame(pd.read_csv('/Users/zhangyizhi/GitHub/sklearnDemo_py/data/data.csv'))
data = data.dropna(how='all').fillna(0)
data = data[data['getInMoney'] != 0]

print data.columns
print data
print '========='
print '========='
print '========='
print '========='
# print data2