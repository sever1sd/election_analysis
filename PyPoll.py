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

#open the election results and read the file
with open(file_to_load) as election_data:

    #to do: perform analysis
    file_reader = csv.reader(election_data)

    headers = next(file_reader)
    print(headers)


