# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 12:49:19 2018

@author: rajar
"""

import random
import time
import numpy as np

start_time = time.time()

# Initialize all the parameters for the network
n = 10**6 # Total number of nodes
simulations = [i for i in range(1,11)]
c = 12 # k_out
r = 5

p = c/(c+r) # Attachment probability
x = [0] * (c*n) # Store the complete network
x[0:11] = [2, 3, 4, 1, 3, 4, 1, 2, 4, 1, 2, 3] # Initial clique seed
x.pop()

all_first_ten = []
all_last_ten = []

for sim in simulations:
    

    x = [0] * (c*n) # Store the complete network
    x[0:11] = [2, 3, 4, 1, 3, 4, 1, 2, 4, 1, 2, 3] # Initial clique seed
    x.pop()
    # Iterate through all the vertices
    for t in range(5,n):
        # Iterate through each out-edge
        for j in range(0,c):
            # Generate a random number between 0 and 1
            # and check if it is less than p
            if (np.random.rand() < p):
                # choose an element uniformly at random 
                # from the list of targets
                d = x[random.randint(0, len(x)-1)]
                #print(d)
            else:
                # choose a vertex uniformly at random 
                # from the set of all vertices
                d = random.randint(1, t-1)
                #print(d)
            
            #x[c*(t-1) + j] = d
            x[c*(t-1) + j] = d
            
    # Initialize dictionary for counting the number of times
    # a node appears in the target list
    target_count = {}
    for i in x:
        if (i not in target_count):
            target_count[i] = 1
        else:
            target_count[i] += 1
    
    # Compute the average number of citations for the 
    # first ten percent of the publications
    sum_first_ten = 0
    for i in range(100000):
        if i in target_count:
            sum_first_ten += target_count[i]
    
    avg_first_ten = sum_first_ten/100000
    
    # Compute the average number of citations for the 
    # last ten percent of the publications
    sum_last_ten = 0
    for i in range(900000,1000000):
        if i in target_count:
            sum_last_ten += target_count[i]
            
    avg_last_ten = sum_last_ten/100000
            
    all_first_ten.append(avg_first_ten)
    all_last_ten.append(avg_last_ten)


print(sum(all_first_ten)/len(all_first_ten))
print(sum(all_last_ten)/len(all_last_ten))
print()

elapsed_time = time.time() - start_time

print(elapsed_time, 'seconds' )
