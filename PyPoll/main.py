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
candidate1 = str()
candidate2 = str()
candidate3 = str()
candidate4 = str()
candidate1votes = 0
candidate2votes = 0
candidate3votes = 0
candidate4votes = 0
candidate1votesperc = 0
candidate2votesperc = 0
candidate3votesperc = 0
candidate4votesperc = 0
winner = str()
with open(election_data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
  
    csv_header = next(csvreader) 

   
    for row in csvreader:
        full_ting.append(row)
        total_votes = total_votes + 1
     
    
for i in range(len(full_ting)):
        duplicate_candidates.append(full_ting[i][2])
        
candidates = set(duplicate_candidates)
candidates = list(candidates)


candidate1 = candidates[0]
candidate2 = candidates[1]
candidate3 = candidates[2]
candidate4 = candidates[3]


for i in range(len(full_ting)):
    if (full_ting[i][2]) == candidate1:
        candidate1votes = candidate1votes + 1
    elif(full_ting[i][2]) == candidate2:
        candidate2votes = candidate2votes + 1
    elif(full_ting[i][2]) == candidate3:
        candidate3votes = candidate3votes + 1
    elif(full_ting[i][2]) == candidate4:
        candidate4votes = candidate4votes + 1
        
candidate1votesperc = round(((candidate1votes/total_votes)*100),3)
candidate2votesperc = round(((candidate2votes/total_votes)*100),3)
candidate3votesperc = round(((candidate3votes/total_votes)*100),3)
candidate4votesperc = round(((candidate4votes/total_votes)*100),3)

if candidate1votesperc > candidate2votesperc and candidate1votesperc > candidate3votesperc and candidate1votesperc > candidate4votesperc:
    winner = candidate1
elif candidate2votesperc > candidate1votesperc and candidate2votesperc > candidate3votesperc and candidate2votesperc > candidate4votesperc:
    winner = candidate2
elif candidate3votesperc > candidate1votesperc and candidate3votesperc > candidate2votesperc and candidate3votesperc > candidate4votesperc:
    winner = candidate3
elif candidate4votesperc > candidate1votesperc and candidate4votesperc > candidate2votesperc and candidate4votesperc > candidate3votesperc:
    winner = candidate4
 
print ("Election Results")
print ("-------------------------")
print (f"Total Votes: {total_votes}")
print ("-------------------------")
print (f"{candidate3}: {candidate3votesperc}00% ({candidate3votes})") 
print (f"{candidate1}: {candidate1votesperc}00% ({candidate1votes})") 
print (f"{candidate4}: {candidate4votesperc}00% ({candidate4votes})")
print (f"{candidate2}: {candidate2votesperc}00% ({candidate2votes})")
print ("-------------------------")
print (f"Winner: {winner}")
print ("-------------------------") 

file = open("PyPoll_Results.txt","w")

file.write("Election Results\n")
file.write("-------------------------\n")
file.write(f"Total Votes: {total_votes}\n")
file.write("-------------------------\n")
file.write(f"{candidate3}: {candidate3votesperc}00% ({candidate3votes})\n") 
file.write(f"{candidate1}: {candidate1votesperc}00% ({candidate1votes})\n") 
file.write(f"{candidate4}: {candidate4votesperc}00% ({candidate4votes})\n")
file.write(f"{candidate2}: {candidate2votesperc}00% ({candidate2votes})\n")
file.write("-------------------------\n")
file.write(f"Winner: {winner}\n")
file.write("-------------------------\n")

file.close()