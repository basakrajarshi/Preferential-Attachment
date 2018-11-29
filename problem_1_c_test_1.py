# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 18:46:37 2018

@author: rajar
"""

import pandas as pd

# Read the papers with dates data and store it in a pandas dataframe
data = pd.read_csv('cit-HepPh-dates.txt', skiprows = [0], 
                   sep='\t', header=None)
# Name the columns
data.columns = ['Paper', 'Date']
#n1 = data.shape[0]
#print('Before', n1)

# Remove duplicate entries
data.drop_duplicates(subset = 'Paper', keep = False, inplace = True)
n = data.shape[0]
#print('After', n)

first_ten = int(n/10)

# Store the first 10 % of published papers in a new dataframe,
# name the columns and make a new list for counting the citations
data_first = data[:first_ten]
data_first.columns = ['Col-1', 'Col-2']
average_first = []

# Store the last 10 % of published papers in a new dataframe,
# name the columns and make a new list for counting the citations
data_last = data[-first_ten:]
data_last.columns = ['Col-1', 'Col-2']
average_last = []

# Read and store the edge-list dataset (containing the 
# citation information) into a new pandas dataframe
edge_data = pd.read_csv('cit-HepPh.txt', skiprows = [0,1,2,3],
                        sep = '\t', header = None)
edge_data.columns = ['Tail', 'Head']
n_edges = edge_data.shape[0]
cit_count = {}

for index, rows in edge_data.iterrows():
    if (rows['Head'] not in cit_count):
        cit_count[rows['Head']] = 1
    else:
        cit_count[rows['Head']] += 1
    
# Make a pandas series for citation counts from edge-list dataset
citations = edge_data['Head'].value_counts()

# Fetch and store the number of citations for the first 10%
count = 0
for index, rows in data_first.iterrows():
    ids = rows['Col-1']
    if (ids in citations.keys()):
        count = citations[ids]
        average_first.append(count)

# Fetch and store the number of citations for the last 10%
count = 0        
for index, rows in data_last.iterrows():
    ids = rows['Col-1']
    if (ids in citations.keys()):
        count = citations[ids]
        average_last.append(count)
        
print('Average in first ten :', sum(average_first)/len(average_first))
print('Average in last ten :', sum(average_last)/len(average_last))