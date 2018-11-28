# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 13:21:58 2018

@author: rajar
"""

import numpy as np
import random
import matplotlib.pyplot as plt

n = 10**3
c = 3
r = 1
p = c/(c+r)
#x = np.zeros((1, c*n))
x = [0] * (c*n)
#x = [0] * 12
#x[0,0:11:1] = 2, 3, 4, 1, 3, 4, 1, 2, 4, 1, 2, 3
x[0:11] = [2, 3, 4, 1, 3, 4, 1, 2, 4, 1, 2, 3]
x.pop()

for t in range(4,n):
    for j in range(0,c):
        #print(random.uniform(0,1))
        if (random.uniform(0,1) < p):
            d = x[random.randint(0, c*(t-1))]
            #print(d)
        else:
            d = random.randint(0, t-1)
            #print(d)
        x[c*(t-1) + j] = d
        #x.append(d)

#print(x[234567])      
target_count = {}
for i in x:
    if (i not in target_count):
        target_count[i] = 1
    else:
        target_count[i] += 1
        

ct = list(target_count.values())
ct_dict = {}
for c in ct:
    if (c not in ct_dict):
        ct_dict[c] = 1
    else:
        ct_dict[c] += 1
        
#x = []
#y = []
#
#for key, value in ct_dict.items():
#    x.append(key)
#    y.append(value/(n))
#    
#plt.figure()
#ax = plt.gca()
#ax.set_yscale('log')
#ax.set_xscale('log')
#ax.set_xlabel('In-degree q')
#ax.set_ylabel('Fraction of vertices with in-degree q or greater')
#ax.scatter(x,y)


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

x = []
y = []
for key, value in ccdf_dict.items():
    x.append(key)
    y.append(value/(n))
    
plt.figure()
ax = plt.gca()
ax.set_yscale('log')
ax.set_xscale('log')
ax.set_xlabel('In-degree q')
ax.set_ylabel('Fraction of vertices with in-degree q or greater')
ax.scatter(x,y)
    