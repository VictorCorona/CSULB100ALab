#Physics 100A Lab 3.3
#Power Law Fitting
#Victor Corona

import numpy as np
import matplotlib.pyplot as plt

#Input your data here
t1=[1,2,3,4,5]
t2=[1,2,3,4,5]
t3=[1,2,3,4,5]
r_ball=[0.47625,0.3175,0.238125,0.1984375,0.15875]

#Calculating the average time for each drop with a for loop
t_avg=[]
for i in range(len(t1)):
    t_avg.append(np.mean([t1[i],t2[i],t3[i]]))

#Fitting a line to the log of r_ball and t_avg
m=np.polyfit(np.log(r_ball),np.log(t_avg),1)

#Plotting each result
plt.plot(t_avg,r_ball,'bo-')
plt.plot(np.log(t_avg),np.log(r_ball),'ro-')
print(m)
plt.show()



