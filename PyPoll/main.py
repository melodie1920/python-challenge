# PyPoll Challenge - Create a python script to analyze poll data

import os
import csv

# Path to collect data from the Resources folder
election_csv = os.path.join("Resources", "election_data.csv")

# Declare variables need in calculations
totalVotes = []
khanCount = 0
correyCount = 0
liCount = 0
otooleyCount = 0

# Read in the CSV file
with open(election_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # skip header row
    csv_reader = next(csvreader)

    # loop through the rows in the table to get the needed results
    for row in csvreader:

        totalVotes.append(row[0])
        
        if row[2] == 'Khan':
            khanCount += 1
        elif row[2] == "Correy":
            correyCount += 1
        elif row[2] == "Li":
            liCount += 1
        elif row[2] == "O'Tooley":
            otooleyCount += 1

totalVotesCount = len(totalVotes) 
khanPercent = "{:.3%}".format(khanCount / totalVotesCount)
correyPercent = "{:.3%}".format(correyCount / totalVotesCount)
liPercent = "{:.3%}".format(liCount / totalVotesCount)
otooleyPercent = "{:.3%}".format(otooleyCount / totalVotesCount)

# find a winner
candidateList = ["Khan", "Correy", "Li", "O'Tooley"]
candidateCountList = [khanCount, correyCount, liCount, otooleyCount]

maxvotesindex = candidateCountList.index(max(candidateCountList))

# print results to terminal
print("Election Results")
print("------------------------------")
print(f'Total Votes: {totalVotesCount}')
print("------------------------------")
print(f'Khan: {khanPercent} ({khanCount})') 
print(f'Correy: {correyPercent} ({correyCount})') 
print(f'Li: {liPercent} ({liCount})') 
print("O'Tooley: " + str(otooleyPercent) + " (" + str(otooleyCount) + ")")
print("------------------------------")
print("Winner: " + candidateList[int(maxvotesindex)])
print("------------------------------")

# create text file to append the results
outputpath = os.path.join("analysis","election_results.txt")

with open(outputpath,'w', newline='') as textfile:
    textfile.write("Election Results" + '\n') 
    textfile.write("------------------------------" + '\n')
    textfile.write(f'Total Votes: {totalVotesCount}'  + '\n')
    textfile.write("------------------------------"  + '\n')
    textfile.write(f'Khan: {khanPercent} ({khanCount})'  + '\n') 
    textfile.write(f'Correy: {correyPercent} ({correyCount})'  + '\n') 
    textfile.write(f'Li: {liPercent} ({liCount})'  + '\n') 
    textfile.write("O'Tooley: " + str(otooleyPercent) + " (" + str(otooleyCount) + ")"  + '\n')
    textfile.write("------------------------------"  + '\n')
    textfile.write("Winner: " + candidateList[int(maxvotesindex)]  + '\n')
    textfile.write("------------------------------")

    textfile.close()