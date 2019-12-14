
import random
import numpy as np
import matplotlib.pyplot as plt

#####################################################################
#Function in integrand
def f(x):
     return np.exp(-2*np.abs(x-5))

#####################################################################    
#mean value method
##################################################################### 
     
#Defining constants and storage variables
N = 10000
rep = 100
dim = 1
N_array = np.ones(N)
rep_array = np.ones(rep)
weight_array = np.ones(N)
count = 0
upper_lim = 10.
lower_lim = 0.
x_values = np.arange(lower_lim, upper_lim, 0.01)

#Probability distribution
def fxn(x):
    return 1/np.sqrt(2*np.pi)* np.exp(-(x-5)**2/2)

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
plt.hist(rep_array)
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
plt.title("Histogram of Integral Values for Mean Value Method")
plt.xlabel("Value of Integral")
plt.ylabel("Counts")
plt.show()


#####################################################################
#weighted avg method
#####################################################################
#Weighting function, determined from given probability distribution
def weight(x):
     return 1/np.sqrt(2*np.pi)* np.exp(-(x-5)**2/2)

#Defining constants and storage variables
N = 10000
rep = 100
dim = 1
N_array = np.ones(N)
rep_array = np.ones(rep)
weight_array = np.ones(N)
count = 0
upper_lim = 10.
lower_lim = 0.
x_val= np.ones(N)
x_store = np.zeros(N)

#Weighted avg algorithm
from scipy.integrate import simps
for i in range(rep):                                                                                                                                       
    for d in range(N):
        x = np.random.normal(5,1)   
        x_store[d] = x
        N_array[d] = f(x)/weight(x)
        weight_array[d]= weight(x)
    total= sum(N_array)
    wx_val = np.arange(lower_lim, upper_lim, 0.01)
    w_val = weight(wx_val)
    total_weight = simps(w_val, wx_val)
    rep_array[i] = (total/N)*total_weight
    
#plotting histogram for weighted avg method
plt.figure()
plt.hist(rep_array)
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
plt.title("Histogram of Integral Values for Weighted Avg Method")
plt.xlabel("Value of Integral")
plt.ylabel("Counts")
plt.show()
