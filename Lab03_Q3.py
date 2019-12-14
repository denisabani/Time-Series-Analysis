# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 20:06:14 2018

@author: Denisa & Brian
"""
############################################################################
#Question 3: Using numerical derivation to create topographical maps
#In this code, 2 plots are outputted:
# - a density plot of the altitude of various long/lat points of Hawaii
# - a density plot of the intensity at various long/lat points
############################################################################

#Import relevant modules
import numpy as np
from matplotlib import pyplot as plt 
import struct
from Lab03_combined_functions import *

#Import data file
filename = 'N19W156.hgt'
f = open(filename, 'rb')
N = 1201

matrix = np.empty([N, N]) #storage variable

#Reading the data file
for j in range(N): #rows
    for i in range(N): #columns
        buf = f.read(2) # reads the first 1201 bytes of data (topmost row)
        x_tuple = struct.unpack('>h', buf) #specifies format type
        x = x_tuple[0]
        matrix[j, i] = x #update matrix 

###########################################################################
scale = 60 #used a scaling factor to improve constrast in topo. image

#Defining the gradient function, using the central difference method
deltax = 420
gradx = np.empty([N, N]) #derivatve with respect to x
for i in range(N):
    for j in range(1, N-1): #need to account for iterative issues at initial and final points
        dx_temp = (matrix[i, j+1] - matrix[i, j-1]) / (2*deltax)
        gradx[i, j] = dx_temp * scale

deltay = 420
grady = np.empty([N, N]) #derivative with respect to y
for i in range(N):
    for j in range(1, N-1): #need to account for iterative issues at initial and final points
        dy_temp = (matrix[j+1, i] - matrix[j-1, i]) / (2*deltay)
        grady[j, i] = dy_temp * scale

#Creating an intensity storage matrix
intensity_matrix = np.empty([N, N])

for i in range(N):
    for j in range(N):
        intensity_matrix[i,j] = intensity(gradx[i,j], grady[i,j], np.pi) #updating the intensity matrix
 
#Plotting the altitude for each long/lat point
plt.imshow(matrix, cmap = 'gray', vmin = -0.25*10**4, vmax = 0.5*10**4, origin = 'upper')
plt.xlabel("longitudinal position")
plt.ylabel("latitudinal position")
plt.title("Height at various longitudinal and latitudinal positions")
plt.show()

#Plotting the illumination intensity for each long/lat point
plt.imshow(intensity_matrix, cmap = 'gray', origin = 'upper')
plt.xlabel("longitudinal position")
plt.ylabel("latitudinal position")
plt.title("Intensity at various longitudinal and latitudinal positions")
plt.show()

#Zooming in on Mauna Loa
plt.imshow(intensity_matrix, cmap = 'gray', origin = 'upper')
plt.xlabel("longitudinal position")
plt.ylabel("latitudinal position")
plt.xlim(200, 800)
plt.ylim(400, 800)
plt.title("Illimuation intensity of Mauna Loa")
plt.show()

#Zooming in on Mauna Kea
plt.imshow(intensity_matrix, cmap = 'gray', origin = 'upper')
plt.xlabel("longitudinal position")
plt.ylabel("latitudinal position")
plt.xlim(400, 900)
plt.ylim(0, 400)
plt.title("Illumination intensity of Mauna Kea")
plt.show()

#Zooming in on Hualalai
plt.imshow(intensity_matrix, cmap = 'gray', origin = 'upper')
plt.xlabel("longitudinal position")
plt.ylabel("latitudinal position")
plt.xlim(0, 400)
plt.ylim(200, 600)
plt.title("Illumination intensity of Hualalai")
plt.show()