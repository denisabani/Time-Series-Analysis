# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 15:34:06 2018

@author: Denisa
"""
import numpy as np
from matplotlib import pyplot as plt

################
#7.2
################
def DFT(a_array): 
    '''
    This function takes an array and performs a discrete fourier transform
    
    '''
    N = len(a_array)    # length of input array
    a_dft_array = np.zeros(N//2+1,complex)
    for k in range(N//2+1):
        for n in range(N):
            a_dft_array[k] += a_array[n]*np.exp(-2j*np.pi*k*n/N)
    return a_dft_array

#Plot Original Data
data = np.loadtxt("sunspots.txt", float)
plt.plot(data[:, 0], data[:, 1])
plt.xlabel("time (months since 1749)")
plt.ylabel("number of sunspots")
plt.title("Number of Sunspots Over Time")
plt.show()

#Plot of FFT of original data
fft = DFT(data[:,1])
x = np.arange(0,len(fft),1)

plt.plot(x, abs(fft)**2) #wut is the spectral density
plt.xlim(0,50)
plt.title("FFT of Sunspots over Time")
plt.xlabel("Power Spectrum")
plt.ylabel("FFT")
