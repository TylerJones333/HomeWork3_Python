#import libraries
import os
import csv

#look in the election data csv file
Polls = os.path.join("election_data.csv")

# these will be the declared lists
# grab the amount of votes for each candidate
totalVotes = []
#grab the candidate names in a list
candidates_list = []
#grab the percentage of the total candidate collection
percentVote_list = []
#moves through each vote and totals it
totalVote_list = 0

#read and open csv file
with open(Polls, newline = "") as csvfile:
    poll_reader = csv.reader(csvfile, delimiter = ",")
    #read the first row
    poll_header = next(poll_reader)

    #loop through each value in each row
    for rows in poll_reader:
        #this append function loops through to help 
        #find the total ballet
        totalVote_list += 1 

        #if the candidate is absent or nonexistent, 
        #add the candidate
        if rows[2] not in candidates_list:
            #this loop is extracting candidate as it goes
            candidates_list.append(rows[2])
            #Adds votes to Candidates who lack votes
            index_value = candidates_list.index(rows[2])
            #sets it equal to that index
            totalVotes.append(1)
            #Row aligment: 
            #https://stackoverflow.com/questions/25630127/if-row0-in-row1-print-row
             #else the candidate already get a vote counted  
        else:
            index_value = candidates_list.index(rows[2])
            #append the new value to the total votes
            totalVotes[index_value] += 1
            #each voter get put intoa loop to find the percentage

    # Add to percent_votes list 
    for ballets in totalVotes:
        #divide the ballets with the voting total
        newPercentage_value = (ballets/totalVote_list) * 100
        #Format string for percentage error 
        '''
        Formating source:
        https://stackoverflow.com/questions/49540932/
        use-the-percentage-error-in-a-figure-title/49540967#49540967
        '''
        newPercentage_value = round(newPercentage_value)
        #Round the percent value through formatting '%.3f%%'
        newPercentage_value = "%.3f%%" % newPercentage_value
        #append the value you to voter percent list
        percentVote_list.append(newPercentage_value)
    
    #pull the max value from the total votes    
    winningCanadate = max(totalVotes)
    #This method returns index of the max votes for the winning person
    index_value = totalVotes.index(winningCanadate)
    #sets it to the right cndidates' index
    winningCandidate = candidates_list[index_value]

#Welcome the user
print("Election Results")
print("--------------------------")
#Revealt the total amount of votes for the candidates
print(f"Total Votes: {str(totalVote_list)}")
print("--------------------------")
#loop each candidate, percentage, vote total
for i in range(len(candidates_list)):
    print(f"{candidates_list[i]}: {str(percentVote_list[i])} ({str(totalVotes[i])})")

print("--------------------------")
#print the winner after for looping
print(f"Winner: {winningCandidate}")
print("--------------------------")

#exporing the data into a text file
#exporting method: https://programminghistorian.org/en/lessons/working-with-text-files
pollOutput = open("Poll_Output.txt", "w")
outputRow1 = "Election Results"
outputRow2 = "--------------------------"
outputRow3 = str(f"Total Votes: {str(totalVote_list)}")
outputRow4 = str("--------------------------")
pollOutput.write('{}\n{}\n{}\n{}\n'.format(outputRow1, outputRow2, outputRow3, outputRow4))

for i in range(len(candidates_list)):
    output = str(f"{candidates_list[i]}: {str(percentVote_list[i])} ({str(totalVotes[i])})")
    pollOutput.write('{}\n'.format(output))
outputRow5 = "--------------------------"
outputRow6 = str(f"Winner: {winningCandidate}")
outputRow7 = "--------------------------"
pollOutput.write('{}\n{}\n{}\n'.format(outputRow5, outputRow6, outputRow7))

# Poll Output
# Election Results
# --------------------------
# Total Votes: 3521001
# --------------------------
# Khan: 63.000% (2218231)
# Correy: 20.000% (704200)
# Li: 14.000% (492940)
# O'Tooley: 3.000% (105630)
# --------------------------
# Winner: Khan
# --------------------------

