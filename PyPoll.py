# The data we need to retrieve
# 1. The total number of votes cast
# 2. A Complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

import csv
import os
# Assign a variable for the file to load and the path
file_to_load = "Resources/election_results.csv"

# Create a filename variable to a direct or indirect path to the file
file_to_save="Analysis/election_analysis.txt"

# 1. Initalize a total vote counter
total_votes = 0

# Candidate Options
candidate_options=[]

# 1. DEclare the empty dictionary for candidate votes
candidate_votes ={}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the eelction results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with reader function
    file_reader=csv.reader(election_data)

    #Read and print the header row.
    headers=next(file_reader)
   
   #print each row in the CSV file
    for row in file_reader:
       # 2. Add to the total vote count
       total_votes +=1
       
       #Print the candidate name from each row
       candidate_name = row[2]

       # Add if candidate does not match existing
       if candidate_name not in candidate_options:
           # Add it to list of candidates
           candidate_options.append(candidate_name)

           # 2. Begin tracking candidate vote count.
           candidate_votes[candidate_name] = 0

        #3. add vote to candidate count
       candidate_votes[candidate_name] +=1
for candidate in candidate_votes:
    # 2. retrieve vote count of a candidate.
    votes = candidate_votes[candidate]
    # 3. Calculate % of votes
    vote_percentage = int(votes)/int(total_votes)*100
    
    # determine winning vote count and candidate
    if(votes>winning_count) and (vote_percentage>winning_percentage):
        # 2. If true ten set winning_count = votes and winning_percent = vote percentage
        winning_count=votes
        winning_percentage=vote_percentage
        winning_candidate=candidate
    print(f"{candidate}:{ vote_percentage:.1f}% ({votes:,})\n")
winning_candidate_summary = (
    f"-----------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-----------------------------\n")
print(winning_candidate_summary)







