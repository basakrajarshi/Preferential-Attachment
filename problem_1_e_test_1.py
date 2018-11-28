# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 01:52:51 2018

@author: rajar
"""

import random
import matplotlib.pyplot as plt
import time

start_time = time.time()

# Initialize all the parameters for the network
n = 10**6 # Total number of nodes
attach_cont = [i for i in range(1,5)] # Uniform attachment contribution
c = 3 # k_out

ccdfs = []
indegrees = []
for r in attach_cont:
    p = c/(c+r) # Attachment probability
    x = [0] * (c*n) # Store the complete network
    x[0:11] = [2, 3, 4, 1, 3, 4, 1, 2, 4, 1, 2, 3] # Initial clique seed
    x.pop()
    
    # Iterate through all the vertices
    for t in range(5,n+1):
        # Iterate through each out-edge
        for j in range(0,c):
            # choose a vertex uniformly at random 
            # from the set of all vertices
            d = random.randint(1, t-1)
            x[c*(t-1) + j] = d
     
    # Initialize dictionary for counting the number of times
    # a node appears in the target list
    target_count = {}
    for i in x:
        if (i not in target_count):
            target_count[i] = 1
        else:
            target_count[i] += 1
            
    
    # Calculate the in-degree of nodes and store them in a dictionary
    ct = list(target_count.values())
    ct_dict = {}
    for c in ct:
        if (c not in ct_dict):
            ct_dict[c] = 1
        else:
            ct_dict[c] += 1
            
    
    # Calculate the cumulative complementary distribution function
    ccdf_dict = {}
    for key, value in ct_dict.items():
        #larger = [i for i in list(ct_dict.keys()) if key <= i]
        larger = []
        lt = list(ct_dict.keys())
        for i in lt:
            if (key <= i):
                larger.append(i)
        su = 0
        for x in larger:
            su += ct_dict[x]
        ccdf_dict[key] = su
    
    # Store the x and y values for plotting the ccdf
    x = []
    y = []
    for key, value in ccdf_dict.items():
        x.append(key)
        y.append(value/(n))
    
    # Store the graphs for different values of r 
    indegrees.append(x)
    ccdfs.append(y)
    

# Plot the ccdf
plt.figure()
ax = plt.gca()
ax.set_xscale('log')
ax.set_yscale('log')
for x,y in zip(indegrees, ccdfs):
    ax.scatter(x,y, alpha = 0.8)
plt.legend(('r = 1', 'r = 2', 'r = 3', 'r = 4'))
ax.set_xlabel('In-degree q')
ax.set_ylabel('Fraction of vertices with in-degree q or greater')
plt.savefig('ccdf_vs_indegree_all-r_no-pref-attach-2', dpi = 300)
plt.show()

elapsed_time = time.time() - start_time

print(elapsed_time, 'seconds' )