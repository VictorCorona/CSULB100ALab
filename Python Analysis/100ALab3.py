#Physics 100A Lab 3.1
#Tabel 3.7 Class Data Analysis

import numpy as np
#inputing measurements
A=[1]               #angle of ramp
m_cart=[2]         #mass of cart
a_slope=[2]         #acceleration from slope of graph (table 3.5A)
a_stats= [3]        #acceleration from stats (table 3.5B)
m_weight= [2]       #mass of cart with weight
g_slope=[9.8]       #acceleration from average slope (table 3.6D)

#Creaeting Dictionary for each group
group1={'angle':A[0],'mass of cart':m_cart[0],'a_slope':a_slope[0],'a_stats':a_stats[0],'mass of cart with weight':m_weight[0],'g_slope':g_slope[0]}

g=np.mean(group1['a_slope'],group1['a_stats'],group1['g_slope'])
print(g)