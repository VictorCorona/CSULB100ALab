import numpy as np
import matplotlib.pyplot as mp

#time for 10 cycles
t = np.array([1,2,3])

#length of string
l=np.array([4,5,6])

T = t/10
T = t**2

m = np.polyfit(l, T, 1)

#g=4*np.pi**2/m(1)
print(m)
