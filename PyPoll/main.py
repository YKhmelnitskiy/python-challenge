#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 17:30:48 2019

@author: yevgeniykhmelnitskiy
"""

import os 

import csv

election_data_csv = os.path.join("..", "Resources", "election_data.csv")
full_ting = []
total_votes = 0
candidates = []
duplicate_candidates = []
with open(election_data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
  
    csv_header = next(csvreader) 


    for row in csvreader:
        full_ting.append(row)
        total_votes = total_votes + 1
        
    for i in range(len(full_ting)):
        duplicate_candidates.append([full_ting[i][2]])
        
candidates = set([duplicate_candidates])
      
print (total_votes)
print (duplicate_candidates)