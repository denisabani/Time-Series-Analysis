# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 14:06:07 2018

@author: Denisa
"""
#############################################
#Question 7.9: Image Deconvolution
#############################################
import numpy as np
from matplotlib import pyplot as plt

#Loading the blurry image
data = np.loadtxt("blur.txt", float)

#Plotting the blurry image
plot = plt.imshow(data, cmap='gray') 
plt.colorbar(plot)
plt.show()

rows = data.shape[0] #number of rows
cols = data.shape[1] #number of columns

#############################################
#Creating the point spread function
sigma = 25 #sigma of the Gaussian function, corresponds to its width
gauss= np.zeros([rows, cols])
for i in range(rows): #as given in the lab manual
    ip = i 
    if ip > rows/2:
        ip -= rows #ensures that rows is centered at the halfway point
    for j in range(cols):
        jp = j
        if jp > cols/2 :
            jp -= cols #ensures that cols is centered at the halfway point
        gauss[i,j] = np.exp(-(ip**2 + jp**2)/(2.*sigma**2)) #Gaussian function

#Plotting the spread function
plt.imshow(gauss, cmap='gray') 
plt.show()

#Applying FFT
data_ft = np.fft.rfft2(data) #FFT of the blurry image
gauss_ft = np.fft.rfft2(gauss) #FFT of the point spread function

#############################################
#Image deconvolution
delta = 10**(-3) #used in subsequent conditional statement
orig_ft= np.zeros([data_ft.shape[0], data_ft.shape[1]], dtype = np.complex)
for i in range(data_ft.shape[0]): #rows
    for j in range(data_ft.shape[1]): #columns
        if abs(gauss_ft[i,j]) < delta: #check if element of spread function is "too small"
            orig_ft[i,j] = (data_ft[i,j])/(rows * cols)
            
        else: #image deconvolution step, based on eqn 4 in the lab manual
            orig_ft[i,j] = (data_ft[i,j]) / ((gauss_ft[i,j])* rows * cols )
                  
#Plotting the pure image            
orig = np.fft.irfft2(orig_ft)
plt.imshow(orig, cmap='gray')
plt.colorbar(plot)
plt.show()
