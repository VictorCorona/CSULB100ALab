#Physics 100A Lab 2
#Activity 6 calculation

import numpy as np

#input 10 velocity points values
v=np.array([1,2,3,4,5,6,7,8,9,10])
avg_v1=np.mean(v)
print('Average velocity from velocity reading:',avg_v1,'m/s')

#input your two points position (x) and time (t)
p1=np.array([1,1])
p2=np.array([2,2])

#Velocity from position vs time
dx=p2[0]-p1[0]    #change in position
dt=p2[1]-p1[1]    #change in time
avg_v2=dx/dt      #calculating avg velocity

print('Change in position',dx,'m')
print('Change in time',dt,'s')
print('Average velocity from position vs time',avg_v2,'m/s')