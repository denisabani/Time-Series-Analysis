
import numpy as np
import matplotlib.pyplot as plt
from random import randint, randrange, seed, random
# %% Main program starts here ------------------------------------------------|

"""
Next steps: 
    3)Set boundries so that when we randomly choose the value of the next point, it remains in the grid 
    
"""
L = 5
Tmax = 10.0
Tmin = 1e-3
tau = 10

dimer = dict()
copydimer = dict()
count= 0 
counts_dict=dict()
dimer_count= dict()

r = np.empty([2, 2], float)

seed(10)
t = 0
T = Tmax
plt.figure()

while T > Tmin:
    t+=1
    T = Tmax*np.exp(-t/tau)
    #N is the number of dimers and am randomly picking spots on 50*50 grid. The
    #second point has to be in the near vicinity of the first 
    r[0,0]= randint(0,L)  #x, y coord of first point
    r[0,1]= randint(0,L)
    r[1,0], r[1,1] = r[0,0], r[0,1] # set the second coordinate equal to the first 
    a = randint(1,4) # picking second point in the vicinity of first; 1 = left 2=right 3=down 4=up NOTE: YOU NEED TO ADD BOUNDRIES SO IT STAYS IN THE 50* 50 MATRIX
    if a == 1:
        r[1,0] = r[0,0] - 1
    if a == 2:
        r[1,0] = r[0,0] + 1
    if a == 3:
        r[1,1] = r[0,1] - 1
    if a == 4:
        r[1,1] = r[0,1] + 1
    dim = [r[0,0], r[0,1]], [r[1,0], r[1,1]]  #contains the first and second point as separate lists  
    
    if t == 1:
        dimer[1] = dim
    
    else: 
        copydimer = dict(dimer)
        key = 1
        s_o = 0 #single overlap flag
        d_o = 0 #double overlap flag
        while s_o != 1 and d_o != 1 and key <= len(dimer):
            count = 0 
            for coord in dimer[key]:
                if coord == dim[0]:
                    count += 1
                if coord == dim[1]:
                    count += 1
#            counts_dict[t] = count
#            dimer_count[t] = len(dimer)
            if count == 2:
                d_o = 1
                if random() > np.exp(len(dimer)/T): 
                    del dimer[key]
            elif count == 1:
                s_o == 1
            elif count == 0:
                dimer[t] = dim[0], dim[1] #if the two points are not in the list, we want to add them 
            key += 1    
            
    for key in dimer.keys():
#        plt.clf()
        plt.plot([dimer[key][0][0],dimer[key][1][0]] ,[dimer[key][0][1],dimer[key][1][1]], 'o-', markersize=3 , linewidth=0.5, color='k')
        plt.show()
        plt.draw()
        plt.pause(10**-2)
    plt.axis('scaled')
    plt.show()

