#Physics 100A Lab 3.2

import numpy as np

#For part 1, measuring g from ball drop
drop_height=[0.5,1,1.5,2]
time_trial1=[1,1.1,1.2,1.3]
time_trial2=[1,1.1,1.2,1.3]
time_trial3=[1,1.1,1.2,1.3]

avg_t=[]
g=[]

#Using a for loop to calculate average time and g for each drop
for i in range(len(time_trial1)):
    t=[time_trial1[i],time_trial2[i],time_trial3[i]]
    t=np.mean(t)
    avg_t.append(t)
    print('Average time for trial',i,avg_t[i])

    g.append(2*drop_height[i]/(avg_t[i]))
    print('Measured g for trial',i,g[i])
    

