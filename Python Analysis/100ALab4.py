#Physics 100A Lab 4

import numpy as np

#List of Inputs
theta=45
v0=3.000
y0=-0.31

g=-9.81
theta=np.deg2rad(theta)

a=g/2
b=v0*np.sin(theta)
c=-y0

#Quadratic Formula
t=((-b)-np.sqrt((b**2)-(4*a*c)))/(2*a)
x=v0*np.cos(theta)*t

print('Time of flight',t,'s')
print('Distance',x,'m')



