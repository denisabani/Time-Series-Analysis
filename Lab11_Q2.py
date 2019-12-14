
###############################################
#Q1: Ising model, based on Prof. Grisouard's code
###############################################
# import modules
from numpy import exp, sum, ones
from pylab import figure, subplot, plot, title, grid, xlabel, ylabel, show, tight_layout
from pylab import imshow, clf, draw, pause
from random import random, randrange
from statistics import median

###############################################
def energyfunction(dipoles, dim):
    energy = 0
    for i in range(dim):
        energy += sum(dipoles[i, :-1]*dipoles[i, 1:])
    for j in range(dim):
        energy += sum(dipoles[:-1, j]*dipoles[j, 1:])
    return energy

def acceptance(En, Eo, kT):
    p = exp(-(En - Eo)/kT)  # Boltzmann factor
    if En-Eo <= 0 or random() < p:
        accepted = True
    else:  # rejected
        accepted = False
    return accepted

def M(dipoles): 
    return sum(dipoles)  # total magnetization

###############################################
#Defining constants
kB = 1.0
J = 1.0
dim = 20
N = 10**5  # number of flips

#Defining ising model function
def ising(T, dim, N):
    ###############################################
    #Generate array of dipoles
    dipoles = ones([dim, dim], int)
    energy = []
    magnet = []
    
    #Randomly assign +/- 1 to dipole array values
    for i in range(dim):
        for j in range(dim):
            rand_val = random() #uniform distribution between [0, 1]
            if rand_val < 0.5:
                dipoles[i, j] *= -1 
    
    E = J*energyfunction(dipoles, dim)
    energy.append(E)
    magnet.append(M(dipoles))
    
    ###############################################
    #Algorithm for flipping the dipoles
    count = 0
    figure()
    for i in range(N):
        picked = randrange(dim)
        dipoles[picked] *= -1  #flip the dipole
        Enew = J*energyfunction(dipoles, dim)
    
        # calculate new energy depending on probability
        flipd = acceptance(Enew, E, kB*T)  # this is the next old value
        if flipd:
            E = Enew
        else:
            dipoles[picked] *= -1  # we de-flip
    
        #Storing energy and magnetization
        energy.append(E)
        magnet.append(M(dipoles))
        
        #Animation
        if count%1000 == 0:
            clf()
            imshow(dipoles, cmap = 'gray', origin = 'lower')
            title("Magnetization of system")
            show()
            draw()
            pause(10**-2)
        
        count += 1
    
    ###############################################
    #Plotting energy and magnetization
    figure()
    
    subplot(211)
    plot(energy)
    grid()
    xlabel("Number of flips")
    ylabel("Total energy")
    title("Total energy of system over time")
    
    subplot(212)
    plot(magnet)
    grid()
    xlabel("Number of flips")
    ylabel("Total magnetization")
    title("Total magnetization of system over time")
    
    tight_layout()
    show()
    
    print("Final magnetization for T=" +str(T) + " is " + str(int(median(magnet[-100:]))))
  
    ###############################################
#Running program for 3 different initial energy values    
T1 = 1.
T2 = 2.
T3 = 3.    

ising(T1, dim, N)
pause(2)

ising(T2, dim, N)
pause(2)

ising(T3, dim, N)