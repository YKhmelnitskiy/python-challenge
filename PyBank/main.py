#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 17:30:10 2019

@author: yevgeniykhmelnitskiy
"""

import os 

import csv

budget_data_csv = os.path.join("..", "Resources", "budget_data.csv") 
total_months = 0
net_total = 0
average = 0
full_ting = []
with open(budget_data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
  
    csv_header = next(csvreader)    
    print(f"CSV Header: {csv_header}")
    
    for row in csvreader:
        full_ting.append(row)
        total_months = total_months + 1
        net_total = net_total + int(row[1])

final_value = int(full_ting[-1][1])
first_value = int(full_ting[0][1])
average = ((final_value - first_value)/(first_value)) * 100
print (full_ting)

-196785
#for n in range(len(full_ting)):
    #print(n)
    
    #print(len(csvreader[1]))
#print (total_months)
#print (net_total)
