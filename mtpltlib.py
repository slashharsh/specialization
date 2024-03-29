# -*- coding: utf-8 -*-
"""datavisual1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tpSMFBLtNHbel1SRZTO9OqNdXDarebyr
"""

import matplotlib as mtpl

dir(mtpl)

[i for i in dir(mtpl) if 'ver' in i print(i)]

del mtpl

import matplotlib.pyplot as plt   #only loading particular class

plt.plot()       #to plot cordinates in graph  IN A LINE

plt.show()

x=[2,3]
y=[4,5]
x1=[1,2,3]
y1=[4,5,6]

plt.xlabel("time")   #xlabel to label of X-AXIS
plt.ylabel("speed")   #ylabel to label of Y-AXIS
plt.plot(x,y,label='sand')    #to show label of particular plot
plt.plot(x1,y1,label='water')   
plt.grid(color='green')   #TO FORM GRIDS IN GRAPH ALSO COLOR CAN BE ASSIGNED
plt.legend()    #to show label of plot that we assigned for a particular plot
plt.xlim(0,15)    # TO ASSIGN THE LIMIT OF X -AXIS  (RANGE)
plt.ylim(0,15)     #TO ASSIGN THE LIMIT OF Y-AXIS  (RANGE)

plt.show

plt.bar(x1,y1,label="wtr")   #TO PLOT BAR GRAPHS

#CRICKET VISUALIZATIONS
player=['dhoni','kohli','pandya']
runs=[101,202,100]
plt.plot(player,runs)
