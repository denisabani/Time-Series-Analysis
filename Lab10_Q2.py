
import random
import numpy as np

def f(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10):
    """fxn for hypersphere as given in Newmann"""
    if a1**2+a2**2+a3**2+a4**2+a5**2+a6**2+a7**2+a8**2+a9**2+a10**2 <= 1:
        return 1
    else:
        return 0

#Defining variables 
N = 1000000
dim=10
N_array = np.ones(N)
d_array = np.ones(dim)
upper_lim = 1
lower_lim = -1

#Generate random value between -1 and 1 for each dimension and store in d_array
#then calculate the value of the hypersphere and store into N_array for each value of r  
for i in range(N):
    for d in range(dim):
        d_array[d] = random.uniform(lower_lim,upper_lim)
    N_array[i] = f(d_array[0],d_array[1],d_array[2],d_array[3],d_array[4],d_array[5],d_array[6],d_array[7],d_array[8],d_array[9])

#Finding Integral Value
total= sum(N_array)
I = (upper_lim-lower_lim)**dim*(total/N)

#Finding error
f_avg = (total/N)**2
f2_avg = sum(N_array**2)/N
var_f = f2_avg - f_avg
err= (upper_lim-lower_lim)*np.sqrt(var_f)/ np.sqrt(N)

#Printing output 
print (I, '+/-',err)
