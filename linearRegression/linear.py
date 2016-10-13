#coding:utf-8
import numpy as np
import pandas as pd
from pandas import DataFrame,Series
from sklearn import linear_model,datasets
import matplotlib.pyplot as plt

#读取数据
data = DataFrame(pd.read_csv('/Users/zhangyizhi/GitHub/sklearnDemo_py/data/data.csv'))
data = data.dropna(how='all').fillna(0)
data = data[data['getInMoney'] != 0]

#选择feature
data_x = data['a']
data_y = data['getInMoney']

#将数据集分割成training set和test set
data_x_train = np.array(data_x[:-200])
data_x_test = np.array(data_x[-200:])

data_x_train = data_x_train.reshape((data_x_train.shape[0],1))
data_x_test = data_x_test.reshape((data_x_test.shape[0],1))

data_y_train = np.array(data_y[:-200])
data_y_test = np.array(data_y[-200:])






#使用线性回归
regr = linear_model.LinearRegression()

#进行training set 和test set的fit ，即是训练的过程
regr.fit(data_x_train,data_y_train)

print regr.coef_

plt.scatter(data_x_test,data_x_test,color='blue')
plt.plot(data_x_test,regr.predict(data_x_test),color='red',linewidth=3)

plt.xticks(())
plt.yticks(())
plt.show()


