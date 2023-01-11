#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 19:47:56 2023

@author: tombui
"""

import pandas as pd
import os
path = os.getcwd() #get the current directory
file_name = os.path.join(path, r'Resources/election_data.csv') #create the file name to read
df = pd.read_csv (file_name)
num_vote = df.shape[0] #number of lines, or the
candidate_list = sorted(list(set(df.iloc[:,2])))
dicting = {} # key is candidate name, value is number vote
for candidate in candidate_list:
    dicting[candidate] = 0

for i in range(num_vote):
    candidate = df.iloc[i, 2]
    dicting[candidate] += 1
winner = ''
num = 0
for candidate in dicting.keys():
    if dicting[candidate] > num:
        num = dicting[candidate]
        winner = candidate
       

print('Election Results')
print('-------------------------')
print(r'Total Votes: %d'%num_vote)
print('-------------------------')
for candidate in candidate_list:
    print(candidate+": %.3f%% (%d)"%(100*dicting[candidate]/num_vote, dicting[candidate]))
print('-------------------------')
print('Winner: ' + winner)
print('-------------------------')

file_name = os.path.join(path, r'analysis/results.txt')
f = open(file_name, 'w')
f.write('Election Results\n')
f.write('-------------------------\n')
f.write('Total Votes: %d\n'%num_vote)
f.write('-------------------------\n')
for candidate in dicting.keys():
    f.write(candidate+": %.3f%% (%d)\n"%(100*dicting[candidate]/num_vote, dicting[candidate]))
f.write('-------------------------\n')
f.write('Winner: ' + winner +"\n")
f.write('-------------------------')
f.close()