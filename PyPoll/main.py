import csv


pyPoll_input = "./Resources/election_data.csv"
pyPoll_output = "analysis/pyPoll_Output.txt"
totalVotes = 0
candidates_Dict = {}
the_winner =""
winner_votes = 0

with open(pyPoll_input, 'r') as csvfile:
    filereader = csv.reader(csvfile,delimiter=',')
    
    #Reading each CSV file row    
    for row in filereader:
        #Printing Results
        #If it's not the header line
        if filereader.line_num>1:
            totalVotes = totalVotes+1

            #If candidates' dictionary is empty, add candidate and first vote count
            if len(candidates_Dict) == 0:
                candidates_Dict[row[2]] = 1  #Candidate name : 1 (first vote)
            else:
            #Check if candidate name already exists in Dictionary, add a vote to the existing ones
                if row[2] in candidates_Dict:
                    candidates_Dict[row[2]] = candidates_Dict[row[2]] +1 
                else:
                    #Add candidate and first vote count
                    candidates_Dict[row[2]] = 1    #Candidate name : 1 (first vote)
    
    
#Writing output to text file
print("Election Results")
print("-------------------------")
print(f"Total Votes: {totalVotes}")
print("-------------------------")

#Writing output to text file 

txtWriter = open(pyPoll_output, 'w')
txtWriter.write("Election Results\n")
txtWriter.write("-------------------------\n")
txtWriter.write("Total Votes: "+str(totalVotes)+'\n')
txtWriter.write("-------------------------\n")

for candidateKey in candidates_Dict.keys():    #Iteration definition based in w3schools example - Only this lines
    votes = candidates_Dict[candidateKey]
    percentage = format(votes/totalVotes,'.3%')    #Line taken from Stackoverflow  
   
    #Determining who's the winner
    if the_winner == "":
        the_winner = candidateKey
        winner_votes = votes
    else:
        if votes > winner_votes:
            #Validating votes of this candidate
            the_winner = candidateKey
            winner_votes = votes


    print(f"{candidateKey}: {percentage} ({votes})")       
    txtWriter.write(candidateKey+": "+str(percentage)+" ("+str(votes)+")\n")

print("-------------------------")
print(f"Winner: {the_winner}")
print("-------------------------")

txtWriter.write("-------------------------\n")
txtWriter.write("Winner: "+the_winner+"\n")
txtWriter.write("-------------------------\n")

txtWriter.close()
