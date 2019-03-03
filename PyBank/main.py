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
third_column = []
date_big_inc = str()
date_big_dec = str()
total = 0
average_chg = 0
greatest_increase = 0
greatest_decrease = 0
tot_months = str()
with open(budget_data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
  
    csv_header = next(csvreader)    
   
    
    for row in csvreader:
        full_ting.append(row)
        total_months = total_months + 1
        net_total = net_total + int(row[1])
        

#average = ((second_value - first_value)/(first_value)) * 100

#We are going into our list of lists, and getting third column values to figure out average change while skipping the first row
for i in range(len(full_ting)):
    if i == 0:
        i = 0
    else:
        first_value = int(full_ting[i - 1][1])
        second_value = int(full_ting[i][1])
        third_column.append([second_value - first_value])
        
        if (second_value-first_value)>greatest_increase:
            greatest_increase = (second_value-first_value)
            date_big_inc = full_ting[i][0]
        elif (second_value-first_value)<greatest_decrease:
            greatest_decrease = (second_value-first_value)
            date_big_dec = full_ting[i][0]
#print (third_column)
#print (date_big_dec)  
#print (greatest_increase)          
for row in third_column:
    total = total + int(row[0])
    average_chg = total/len(third_column)
    rounded_avg_chg = round(average_chg,2)

print ("Financial Analysis")
print ("----------------------------")
print (f"Total Months: {total_months}")
print (f"Average Change: ${rounded_avg_chg}")
print (f"Greatest Increase in Profits: {date_big_inc} (${greatest_increase})")
print (f"Greatest Decrease in Profits: {date_big_dec} (${greatest_decrease})")

file = open("PyBank_Results.txt","w")

file.write("Financial Analysis\n")
file.write("----------------------------\n")
file.write(f"Total Months: {total_months}\n")
file.write(f"Average Change: ${rounded_avg_chg}\n")
file.write(f"Greatest Increase in Profits: {date_big_inc} (${greatest_increase})\n")
file.write(f"Greatest Decrease in Profits: {date_big_dec} (${greatest_decrease})\n")

file.close()

#round(number[, ndigits])
#for n in range(len(full_ting)):
    #print(n)
    
    #print(len(csvreader[1]))
#print (total_months)
#print (net_total)
#I am trying to store the value as third column by havin the second column - from the first one 
    #so then to get the second column to loop you would have to do full_ting[1+1][1] - full_ting[2+1][1]
#if the second value is greater than the first value, store the second value as greatest_inc