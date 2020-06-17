# PyBank Challenge - Create a python script to analyze profit and loss data for a company.

import os
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join("Resources", "budget_data.csv")

totalMonths = []
totalMoney = 0
totalChange = 0
priorMoney = 0
currentMoney = 0
differenceChange = 0
averageChange = 0.0
currentChange = 0.0
priorChange = 0.0
greatestIncreaseValue = 0
greatestDecreaseValue = 0

# Read in the CSV file
with open(budget_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_reader = next(csvreader)

    for row in csvreader:
        
        totalMonths.append(row[0]) 
        totalMoney += int(row[1])
        priorMoney = currentMoney
        currentMoney = int(row[1])
        
        if priorMoney != 0:
            priorChange = differenceChange
            differenceChange = currentMoney - priorMoney
            currentChange = differenceChange
            totalChange = totalChange + differenceChange

            if currentChange > priorChange and currentChange > greatestIncreaseValue:
                greatestIncreaseMonth = row[0]
                greatestIncreaseValue = currentChange

            if currentChange < priorChange and currentChange < greatestDecreaseValue:
                greatestDecreaseMonth = row[0]
                greatestDecreaseValue = currentChange

totalMonthCount = len(totalMonths)
averageChange = totalChange / (totalMonthCount - 1)

print("Financial Analysis")
print("------------------------------")
print(f'Total Months: {totalMonthCount}')
print(f'Total: ${totalMoney}')
print('Average Change: $' + str(round(averageChange,2)))
print(f'Greatest Increase in Profits: {greatestIncreaseMonth} (${greatestIncreaseValue})')
print(f'Greatest Decrease in Profits: {greatestDecreaseMonth} (${greatestDecreaseValue})')

outputpath = os.path.join("analysis","financial_analysis.txt")

with open(outputpath,'w', newline='') as textfile:
    textfile.write("Financial Analysis" + '\n') 
    textfile.write("------------------------------" + '\n')
    textfile.write(f'Total Months: {totalMonthCount}' + '\n')
    textfile.write(f'Total: ${totalMoney}' + '\n')
    textfile.write('Average Change: $' + str(round(averageChange,2)) + '\n')
    textfile.write(f'Greatest Increase in Profits: {greatestIncreaseMonth} (${greatestIncreaseValue})' + '\n')
    textfile.write(f'Greatest Decrease in Profits: {greatestDecreaseMonth} (${greatestDecreaseValue})' + '\n')

    textfile.close()