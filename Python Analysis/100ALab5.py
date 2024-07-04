#Physics 100A Lab 5

import numpy as np
import matplotlib.pyplot as plt

#Input Measurements
R=[1,2,3,4,5]
M=[10,20,30,40,50]
t_avg=[3,6,7,8,9]
m=[2,3,4,5,6]
g=9.81

T=[]
v=[]
Fc_th=[]
Fc_ex=[]
for i in range(len(R)):
    T.append(t_avg[i]/20)
    v.append(2*np.pi*R[i]/T[i])
    Fc_th.append(M[i]*(v[i]**2)/R[i])
    Fc_ex.append(m[i]*g)

#Printing Results
print('T',T)
print('v',v)
print('Fc theory',Fc_th)
print('Fc experimental',Fc_ex)

#Plotting Results
plt.plot(M,Fc_th,'bo-')    #Change the variables here to make different plots plt.plot(x,y,'bo-)
plt.legend(['Fc vs M'])    #Change the legend to label the graph
plt.show()