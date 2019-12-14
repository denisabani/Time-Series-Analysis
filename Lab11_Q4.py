
import numpy as np
import matplotlib.pyplot as plt
from random import randint, randrange, seed, random
# %% Main program starts here ------------------------------------------------|
L = 50 #unit length of lattice 

Tmax = 10.0
Tmin = 1e-3
tau = 10000

dimer = dict()
dimer_count= dict()

r = np.empty([2, 2], float) 

seed(10)
t = 0
T = Tmax

while T > Tmin:
    t+=1
    T = Tmax*np.exp(-t/tau)
    r[0,0], r[0,1] = randint(0,L-1), randint(0,L-1)  #x, y coord of first point
    r[1,0], r[1,1] = r[0,0], r[0,1] # set the second coordinate equal to the first 
    a = randint(1,4) #randomly pick an x or y shift on scond point; 1 = left 2=right 3=down 4=up 
    if a == 1:
        r[1,0] = r[0,0] - 1
    if a == 2:
        r[1,0] = r[0,0] + 1
    if a == 3:
        r[1,1] = r[0,1] - 1
    if a == 4:
        r[1,1] = r[0,1] + 1
    dim =   [r[0,0], r[0,1]], [r[1,0], r[1,1]]  #contains the first and second point as separate lists  
    
    #Add the first dimer of the iteration directly to the dictionary 
    if t == 1:
        dimer[1] = dim
    #Every other incoming dimer needs to be compared to the dimers already in the lattice. counts_dict will keep count of the amount of times the current randomly chosen points are matched to a point for each dimer. The maximum count in the dictionary decides the fate of the dimer. 
    else: 
        copydimer = dict(dimer)
        counts_dict=dict()
        count = 0
        for key in copydimer.keys():
            for coord in dimer[key]:
                if coord == dim[0]:
                    count +=1
                if coord == dim[1]:
                    count += 1
            counts_dict[key] = count
        if max(list(counts_dict.values()))==2 and random() < np.exp(-len(dimer)/T):
            del dimer[key]
        if max(list(counts_dict.values())) == 0:
            dimer[t] = dim[0], dim[1]
            
#Plot all the dimers in the final dictionary      
for key in dimer.keys():
    plt.plot([dimer[key][0][0],dimer[key][1][0]], [dimer[key][0][1],dimer[key][1][1]], 'o-', markersize=3 , linewidth=0.5, color='k')
plt.axis('scaled')
plt.title("Simulated Annealing on 50*50 Lattice")
plt.show()
        
