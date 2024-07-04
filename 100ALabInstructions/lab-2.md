This lab does not require much data analysis, it is mostly graphical analysis. You can still use python to do some calculations at the end.

```python.run

import numpy as np

#input 10 velocity points values
v=np.array([v1,v2,v3,v4,v5,v6,v7,v8,v9,v10])
avg_v1=np.mean(v)
print('Average velocity from velocity reading:',avg_v1,'m/s')

#input your two points position (x) and time (t)
p1=np.array([x1,t1])
p2=np.array([x2,t2])

#Velocity from position vs time
dx=p2[0]-p1[0]    #change in position
dt=p2[1]-p1[1]    #change in time
avg_v2=dx/dt      #calculating avg velocity

print('Change in position',dx,'m')
print('Change in time',dt,'s')
print('Average velocity from position vs time',avg_v2,'m/s')
```