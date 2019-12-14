# -*- coding: utf-8 -*-

import random
import numpy as np
import matplotlib.pyplot as plt

#####################################################################
#Function in integrand
def f(x):
     return x**(-1/2)/(1+np.exp(x))
 
#####################################################################    
#mean value method
##################################################################### 
     
#Defining constants and storage variables
N = 10000
rep = 100
dim=1
N_array = np.ones(N)
rep_array = np.ones(rep)
count = 0
upper_lim = 1
lower_lim = 0
x_values = np.arange(0.01,1,0.01)

#Probability distribution
def fxn(x):
    return 1/(2*np.sqrt(x))

y_values = fxn(x_values)

#Mean value algortihm
for i in range(rep):
    for d in range(N):
        x = random.uniform(lower_lim,upper_lim)
        N_array[d] = f(x)
    total= sum(N_array)
    rep_array[i] = (upper_lim-lower_lim)**dim*(total/N)

#plotting histogram for mean value method
plt.figure()
plt.hist(rep_array, 10, range = [0.8, 0.88])
plt.title("Histogram of Integral Values for Mean Value Method")
plt.xlabel("Value of Integral")
plt.ylabel("Counts")
plt.show()

#####################################################################
#weighted avg method
#####################################################################

#Weight function, determined from the given probability distribution
def weight(x):
     return x**(-1/2)

#Defining constants and storage variables
N = 10000
rep = 100
dim=1
N_array = np.ones(N)
rep_array = np.ones(rep)
weight_array = np.ones(N)
count = 0
upper_lim = 1
lower_lim = 0.01

x_val= np.ones(N)

#Importing Python's simpson integration implementation
from scipy.integrate import simps #used to evaluate integral of weight(x)

#Weighted avg algorithm
for i in range(rep):                                                                                                                                       
    for d in range(N):
        x = random.uniform(lower_lim,upper_lim)**2   
        N_array[d] = f(x)/weight(x)
        weight_array[d]= weight(x)
    total= sum(N_array)
    wx_val = np.arange(0.0001, 1, 0.0001)
    w_val = weight(wx_val)
    total_weight = simps(w_val, wx_val)
    rep_array[i] = (total/N)*total_weight
    
#plotting histogram for weighted avg method    
plt.figure()
plt.hist(rep_array, 10, range = [0.8, 0.88])
plt.title("Histogram of Integral Values for Weighted Avg Method")
plt.xlabel("Value of Integral")
plt.ylabel("Counts")
plt.show()
