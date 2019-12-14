# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 20:06:14 2018

@author: Denisa
"""
############################################################################
#Question 1: Comparing Gaussian quadrature to Trapezoidal and Simpson integration methods
#In this code, 4 plots are outputted:
# - 3 plots for the relative error for Trapezoidal, Simpson and Gaussian integration (respectively) with respect to varying N
# - A model of the probability of snowfall for varying temperature ranges
############################################################################

#Importing relevant modules 
import numpy as np
from scipy import special as sp
from matplotlib import pyplot as plt
from Lab03_combined_functions import *

#Calling the erf function
a=0.0 #lower limit
b=3.0 #upper limt

#Reference value, used to calculate relative difference below
erf_fun = sp.erf(b) 

#########################################################################
#Creating plot of relative differences 
gauss_err= gauss_int(a,b,200) - gauss_int(a,b,100)
print(gauss_err)

#Calculating relative difference for Trapezoidal, Simpson, and Gaussian integration
trap_values =[]
simp_values =[]
gauss_values= []
num = np.arange(5, 1000, 1)
for i in num:
    trap_value = abs(trap_int(a, b, i)-erf_fun)/erf_fun
    simp_value = abs(simp_int(a, b, i)-erf_fun)/erf_fun
    gauss_value = abs(gauss_int(a, b, i)-erf_fun)/erf_fun
    trap_values.append(trap_value)
    simp_values.append(simp_value)
    gauss_values.append(gauss_value)

#Plotting the calculated relative differences
num_trap, trap_val = del_zero(num, trap_values) #need to remove y = 0 (and corresponding x), since log not defined here
plt.loglog(num_trap, trap_val, color = "red")
plt.title("Relative Error using Trapezoidal Integration Method")
plt.xlabel("log(N)")
plt.ylabel("log(Relative Error)")
plt.show()

num_simp, simp_val = del_zero(num, simp_values) #need to remove y = 0 (and corresponding x), since log not defined there
plt.loglog(num_simp, simp_val, color= "blue")
plt.title("Relative Error using Simpson Integration Method")
plt.xlabel("log(N)")
plt.ylabel("log(Relative Error)")
plt.show()

num_gauss, gauss_val = del_zero(num, gauss_values) #need to remove y = 0 (and corresponding x), since log not defined there
plt.loglog(num_gauss, gauss_val, color = "black")
plt.title("Relative Error using Gaussian Integration Method")
plt.xlabel("log(N)")
plt.ylabel("log(Relative Error)")
plt.show()

############################################################################
#Modelling the probability of blowing snow 
#for given values of u_10 and t_h, and for a range of T_a values

u_10 = [6,8,10] #given in the manual
t_h= [24, 48, 72] #given in the manual
t_a = np.arange(-20, 30, 0.1) #range of T_a values
N=100
y_values=[]
all_y_values=[]

#Evaluating the probability function over range of (u_10, T_a, t_h) values
#Probability formula has been recast in the form of erf()
for i in range(len(u_10)):
    for r in range(len(t_h)):   
        for ele in t_a:
            u_bar = 11.2 + 0.365*ele + 0.00706*ele**2 + 0.9*np.log(t_h[r])
            delta = 4.3 + 0.145*ele + 0.00196*ele**2
            
            #Defining integration limits 
            upper_x_limit = (u_bar - u_10[i])/(np.sqrt(2)*delta)
            lower_x_limit = (u_bar)/(np.sqrt(2)*delta)
            
            #Evaluating integral
            y_value= gauss_int(lower_x_limit,upper_x_limit, N) /(-2)                
            y_values.append(y_value)
            
        plt.plot(t_a, y_values, label = str("u_10 =  " + str(u_10[i])+ "; t_h = " + str(t_h[r])))
        all_y_values.append(y_values) #this store will be used to check all outputted values, for troubleshoot purpose
        y_values = [] #need to reset the store

plt.xlabel("T_a value (◦C)")
plt.ylabel("P(u_10, T_a, t_h)")
plt.legend()
plt.title("Probability of blowing snow for varying T_a")
plt.show()
 

    
    








