
###############################################
#Q1: Monte Carlo simulation
###############################################
#Importing relevant modules
from random import random, randrange
from math import exp, pi
from numpy import ones, asarray
from pylab import plot, scatter, xlabel, ylabel, title, show, figure, clf, hist, bar

###############################################
#Defining constants
N = 1000 #number of particles
min_steps = 250000 #number of time steps defined in Q1a)
dE_thresh = 2000 #threshold value determined from results of Q1a), with T = 10 kbT

def mc(T, N, figs):
    #create a 2D array to store the quantum numbers
    n = ones([N, 3], int)
    
    ###############################################
    #Main loop
    eplot = []
    E = 3*N*(pi**2)/2 #each DOF of each particle contributes (pi**2)/2
    run = 0 #while loop condition
    count = 0 #for loop condition
    while run == 0:
        #Choose the particle and the move
        i = randrange(N)
        j = randrange(3)
        if random()<0.5: #50-50 chance of passing
            dn = 1 #change in quantum number
            dE = (2*n[i, j] + 1)*(pi**2)/2 #change in energy
        else:
            dn = -1 #change in quantum number
            dE = (-2*n[i, j] + 1)*(pi**2)/2 #change in energy
            
        #decide whether to accept the move
        if n[i, j]> 1 or dn == 1:
            if random()<exp(-dE/T):
                #update the quantum number and the energy
                n[i, j] += dn
                E += dE
        eplot.append(E)
        
        #Checking if equilibrium has been reached
        if count > min_steps:
            if (count%500) == 0: #checking only every 500 iterations
                e_min = min(eplot[-1000:])
                e_max = max(eplot[-1000:])
                if abs(e_max - e_min) < dE_thresh:
                    run = 1 #if plateau, then break while loop
        count += 1
    
    ###############################################
    #Plotting energy as a function of time
    if figs == 0:
        figure(1)
        clf()
        plot(eplot) 
        ylabel("Energy")
        xlabel("Time")
        title("Energy as a function of time")
        show()
    
    ###############################################
    #Calculating the energy of each particle, neglecting constant factors 
    energy_n = n[:, 0]**2 + n[:, 1]**2 + n[:, 2]**2 #total energy
    e_tot = sum(energy_n) #total energy of the system
    
    #Calculating the frequency distribution and creating a plot
    figure()
    clf()
    hist_output = hist(energy_n, 50)
    xlabel("Frequency")
    ylabel("Frequency Counts")
    title("Raw Frequency distribution for T=" + str(T))
    show()
    
    energy_frequency = hist_output[0] #frequency count output
    
    energy_vals = 0.5*(hist_output[1][:-1] + hist_output[1][1:]) #Defining central energy values
    n_vals = energy_vals**0.5 #Calculating the energy frequency distribution 
    
    ###############################################
    #Plotting frequency distribution as a function of n
    if figs == 0:
        figure(3)
        clf() 
        bar(n_vals, energy_frequency, width=0.1)
        xlabel("Particle Energy")
        ylabel("Frequency Counts")
        title("Frequency distribution as a function of energy")
        show()
    ###############################################
    return e_tot, energy_frequency, n_vals #total energy; energy counts; quantum numbers

###############################################
#Defining average value of n for a system
def n_avg(f, n): #f is frequency count for given n, where n is the quantum number
    w_sum = sum(f*n)
    return w_sum / sum(n)

#Calculating average energy 
n_avg_store = ones([6])
e_tot_store = ones([6])
T_store = [10.0, 40.0, 100.0, 400.0, 1200.0, 1600.0] # in KbT

e_tot_store[0], ef_T1, n_T1 = mc(T_store[0], N, 1)
n_avg_store[0] = n_avg(ef_T1, n_T1)

e_tot_store[1], ef_T2, n_T2 = mc(T_store[1], N, 1)
n_avg_store[1] = n_avg(ef_T2, n_T2)

e_tot_store[2], ef_T3, n_T3 = mc(T_store[2], N, 1)
n_avg_store[2] = n_avg(ef_T3, n_T3)

e_tot_store[3], ef_T4, n_T4 = mc(T_store[3], N, 1)
n_avg_store[3] = n_avg(ef_T4, n_T4)

e_tot_store[4], ef_T5, n_T5 = mc(T_store[4], N, 1)
n_avg_store[4] = n_avg(ef_T5, n_T5)

e_tot_store[5], ef_T6, n_T6 = mc(T_store[5], N, 1)
n_avg_store[5] = n_avg(ef_T6, n_T6)

#Plotting the final total energy for range of initial energy
figure()
clf()
scatter(asarray(T_store), e_tot_store)
title("Total energy of system for range of initial energy")
xlabel("Initial energy")
ylabel("Total energy of system")
show()

hc = (e_tot_store[-1] - e_tot_store[0])/(T_store[-1] - T_store[0])
print('Heat capacity is ' + str(hc) + 'Kb')

#Plotting the final average quantum number for range of initial energy
figure()
clf()
scatter(asarray(T_store), n_avg_store)
title("Final average n for range of initial energy")
xlabel("Initial energy")
ylabel("Final average n")
show()     