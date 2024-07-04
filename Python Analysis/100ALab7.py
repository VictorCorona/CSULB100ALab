#100A Lab 7.1

import numpy as np
import matplotlib.pyplot as plt

T_avg=[2,3,4]
L=[4,5,6]
m=[]
a=[]

T2=[i**2 for i in T_avg]
m=np.polyfit(L,T2,1)

print(m)
plt.plot(L,T_avg,'bo-')    #Change the variables here to make different plots plt.plot(x,y,'bo-)
plt.legend(['T_avg vs L'])    #Change the legend to label the graph
plt.show()
