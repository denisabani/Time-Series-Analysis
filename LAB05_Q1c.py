# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 15:29:18 2018

@author: Denisa
"""
#####################
#7.6
#####################
import numpy as np
from matplotlib import pyplot as plt

#1D DCT Type-II
def dct(y):
    N = len(y)
    y2 = np.empty(2*N,float)
    y2[:N] = y[:]
    y2[N:] = y[::-1]

    c = np.fft.rfft(y2)
    phi = np.exp(-1j*np.pi*np.arange(N)/(2*N))
    return np.real(phi*c[:N])

#Inverse 1D DCT Type II
def idct(a):
    N = len(a)
    c = np.empty(N+1,complex)

    phi = np.exp(1j*np.pi*np.arange(N)/(2*N))
    c[:N] = phi*a
    c[N] = 0.0
    return np.fft.irfft(c)[:N]

# Plot of original data
data = np.loadtxt("dow2.txt", float)
x2 = np.arange(0,len(data),1)
plt.ylabel("Daily Closing Value ($)")
plt.xlabel("Time (business days)")
plt.plot(x2, data, label = "Original Data")
plt.title("Plot of original data")

#Plot of fourier transform and inverse of fourier transform 
rfft = np.fft.rfft(data)
rfft[10:] = 0 
new_data = np.fft.irfft(rfft)
x = np.arange(0,len(rfft),1)


plt.plot(x2, new_data, label= "Smoothed using FFT")
plt.title("Plot of Closing Value of Dow Jones between 2004-2008")
plt.legend()
plt.show()

#Re-do with discrete cosine transform
cos_tran = dct(data)
cos_tran[10:] = 0 
new_data2 = idct(cos_tran)
x3 = np.arange(0,len(cos_tran),1)
x4 = np.arange(0,len(new_data2),1)

#Plot discrete cosine transform with orignial data
plt.plot(x2, data, label = "Original Data")  
plt.plot(x4, new_data2, label = "Smoothed using Cosine FFT")
plt.ylabel("Daily Closing Value ($)")
plt.xlabel("Time (business days)")
plt.title("Plot of Closing Value of Dow Jones between 2004-2008")
plt.legend()
plt.show()

