#import libraries
import os
import csv

#declare bankData as object
bankData = os.path.join("budget_data.csv")

#initiate the two lists
date = [] 
profit = []

#initiate listed variables to zero 
values = 0
final_Change = 0
total_profitLose = 0
total_monthAmount = 0


#read and open csv file
with open(bankData, newline = "") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ",")
    #read the first row
    csv_header = next(csv_reader)
    #initiate the header value to zero
    Header_value = 0
    #return the next function using 'next'
    rowOne = next(csv_reader)
    #self append the total months
    total_monthAmount += 1
    #self append the next row
    total_profitLose += int(rowOne[1])
    #set the value to the appended function
    values = int(rowOne[1])
    #this is added to reset initially place values in row One
    csv_Init = 0
    
    #cycles through each row of the file after header & initial row 
    for initial_row in csv_reader:
        # Keeping track of the dates
        date.append(initial_row[0])
        # calculate the final change, then add it to list of changes
        # converts the numbers into objects 
        final_Change = int(initial_row[1]) - values
        # append the profit to the changed value
        profit.append(final_Change)
        # sets new objects equal to values
        values = int(initial_row[1])
        #total number of months
        total_monthAmount += 1
        #total net amount of "Profit/Losses over entire period"
        total_profitLose = total_profitLose + int(initial_row[1])

    #highest increase in profits
    highest_increase = max(profit)
    #highest index of profits
    highest_index = profit.index(highest_increase)
    #highest date set equal to highest date index
    highest_date = date[highest_index]
    #largest decrease (lowest increase) in profits 
    highest_decrease = min(profit)
    #worst profit
    worstIndex = profit.index(highest_decrease)
    #worst date value in date index
    worstDate = date[worstIndex]
    #average change in "Profit/Losses between months over entire period"
    average_change = sum(profit) / len(profit)
    

#display output to user
print("Financial Analysis")
print("---------------------")
#Print total for months,total profit/lose, and average change in price
print(f"Total Months: {str(total_monthAmount)}")
print(f"Total: ${str(total_profitLose)}")
print(f"Average Change: ${str(round(average_change,2))}")
#print the larges increase and decrease in profits
print(f"Greatest Increase in Profits: {highest_date} (${str(highest_increase)})")
print(f"Greatest Decrease in Profits: {worstDate} (${str(highest_decrease)})")

#exporing the data into a text file
#exporting method: https://programminghistorian.org/en/lessons/working-with-text-files
bankOutput = open("Banking_Output.txt", "w")
outputRow1 = "Financial Analysis"
outputRow2 = "---------------------"
outputRow3 = str(f"Total Months: {str(total_monthAmount)}")
outputRow4 = str(f"Total: ${str(total_profitLose)}")
outputRow5 = str(f"Average Change: ${str(round(average_change,2))}")
outputRow6 = str(f"Greatest Increase in Profits: {highest_date} (${str(highest_increase)})")
outputRow7 = str(f"Greatest Decrease in Profits: {worstDate} (${str(highest_decrease)})")
bankOutput.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(outputRow1,
	outputRow2,
	outputRow3,
	outputRow4,
	outputRow5,
	outputRow6,
	outputRow7))

# Bank Output:
# Financial Analysis
# ---------------------
# Total Months: 86
# Total: $38382578
# Average Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($1926159)
# Greatest Decrease in Profits: Sep-2013 ($-2196167)

