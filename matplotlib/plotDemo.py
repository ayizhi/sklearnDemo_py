#coding:utf-8
import matplotlib.pyplot as plt
from numpy.random import randn
import numpy as np

#弹出窗口（个人理解为建立画布）
fig = plt.figure()

#不能通过空figure绘图，必须用add_subplot创建一个或多个subplot才行
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)

#这时发出绘图命令，如plt.plot，matplotlib就会在最后一个用过的subplot上进行绘制
plt.plot(randn(50).cumsum(),'k--')
_ = ax1.hist(randn(100),bins=20,color='k',alpha=0.3)
ax2.scatter(np.arange(30),np.arange(30) + 3*randn(30))

#调整图跟图之间的距离
plt.subplots_adjust(wspace=0.2,hspace=0.25)
plt.show()
