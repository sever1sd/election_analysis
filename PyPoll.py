#The data we need to retrieve
#1. Total number of votes cast
#2. A complete list of candidates who received votes
#3. % of votes each candidate won
#4. Total number of votes each candidate won
#5. Winner of the election based on popular vote

#assign a variable for the file to laod and the path

#imports modules
import csv
import os

#assigns variable to file path
file_to_load = os.path.join("Resources","election_results.csv")
#assigns variable to save the file to a path
file_to_save = os.path.join("analysis","election_analysis.txt")

#initialize vote counter
total_votes = 0
#initiliaze candidate options
candidate_options = []
#initiliazes dictionary for candidate votes
candidate_votes = {}

winning_candidate = ""
winning_count = 0
winning_percentage = 0

#open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #sets headers to remove
    headers = next(file_reader)
    print(headers)
    
    #iterates each row in the column
    for row in file_reader:
        #adds 1 to the vote counter for each row
        total_votes += 1

        #finds candidate name in list index 
        candidate_name = row[2]

        #adds candidate name to list if not already present
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            #initializes candidate votes to zero
            candidate_votes[candidate_name] = 0

        #adds 1 each time it's added to the dict
        candidate_votes[candidate_name] += 1

with open(file_to_save,"w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results,end="")
    txt_file.write(election_results)

#loops through candidate list
    for candidate_name in candidate_votes:
        #pulls vote count for candidate
        votes = candidate_votes[candidate_name]
        #calcs the vote percentage
        vote_percentage = float(votes)/float(total_votes)*100
        #saves results as variable
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        #prints results
        print(candidate_results)
        #saves results in txt file
        txt_file.write(candidate_results)

        #decision statement to determine winner
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    #prints winning summary
    winning_candidate_summary = (
        f"---------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Vote Percentage: {winning_percentage:.1f}%\n"
        f"---------------------------\n"
    )
    txt_file.write(winning_candidate_summary)
print(winning_candidate_summary)
#print(total_votes)
#print(candidate_options)
#print(candidate_votes)
#print(vote_percentage)





