#Physics 100A Lab 1 
#Spring 2024
#Victor Corona

#import the numpy function library
import numpy as np  

#input your measuremtns here (in meters)
length=np.array([1,2,3])
width=np.array([1,2,3])
height=np.array([1,2,3])

#Estimate your numerical error for length (in meters)
num_error_length=np.array([0.01])
num_error_width=np.array([0.01])
num_error_height=np.array([0.01])

#Find the average of each dimension
avg_length=np.mean(length)
avg_width=np.mean(width)
avg_height=np.mean(height)

#Calculate the volume of the room
V=avg_length*avg_width*avg_height
print('Volume of the room is ',V,'m^3')

#calculate mass of air in the room
d=1.28  #density of air (kg/m^3)
d_error=0.05
M=V*d   
print('Mass of air in the room is ',M,'kg')

#Calculating errors
length_percent_error=num_error_length/avg_length
width_percent_error=num_error_width/avg_width
height_percent_error=num_error_height/avg_height

volume_error=length_percent_error+width_percent_error+height_percent_error
volume_percent_error=volume_error*100
print('Volume error',volume_percent_error[0],'%')

mass_error=volume_error+d_error
mass_num_error=mass_error*M
print('Numerical mass error',mass_num_error[0],'kg')