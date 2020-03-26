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

# Step 2. challenge - initalize variables for counties list
county_list = []
# Step 3. challenge initalize counties votes dictionary
county_votes ={}
# Step 4. challenge - initialize string for county with largest turnout
largest_county_turnout = ""
highest_county = 0


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
       
       #Print the candidate name 
       candidate_name = row[2]

       # print county name 
       county_name = row[1]

       # Add if candidate does not match existing
       if candidate_name not in candidate_options:
           # Add it to list of candidates
           candidate_options.append(candidate_name)

           # 2. Begin tracking candidate vote count.
           candidate_votes[candidate_name] = 0

        #3. add vote to candidate count
       candidate_votes[candidate_name] +=1

       #if statement for counties does not match existing
       if county_name not in county_list:
           # Add it to list of counties
           county_list.append(county_name)

           # 2. Begin tracking county vote count.
           county_votes[county_name] = 0

        #3. add vote to county vote count
       county_votes[county_name] +=1
        

# Open file to write results to
with open(file_to_save,"w") as txt_file:
    #Print the final vote count to terminal and county votes title
    election_results=(
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        f"\n"
        f"County Votes:\n")
    print(election_results,end="")
    # save final vote to text file
    txt_file.write(election_results)

    # Begin for Loop for writing county vote results
    for county in county_votes:
        #retrieve vote count of county
        votesc = county_votes[county]
        #calculate % of votes
        votec_percentage = float(votesc)/float(total_votes)*100
        #initialize county results
        county_results = (
            f"{county}:{votec_percentage:.1f}% ({votesc:,})\n")
        
        #print each county results
        print(county_results)
        # save county results to text file.
        txt_file.write(county_results)

        # determine highest county
        if(votesc>highest_county):
            # 2. If true ten set highest_county = voteC and largest county to voteC
            highest_county=votesc
            largest_county_turnout=county

    largest_county_summary = (
        "\n"
        "-----------------------------\n"
        f"Largest County Turnout: {largest_county_turnout}\n"
        "-----------------------------\n")
    #Print largest county summar
    print(largest_county_summary)
    #save largest county summary to txt file
    txt_file.write(largest_county_summary)

    # for loop to write candidate votes/results 
    for candidate in candidate_votes:
        # 2. retrieve vote count of a candidate.
        votes = candidate_votes[candidate]
        # 3. Calculate % of votes
        vote_percentage = float(votes)/float(total_votes)*100
        # initialize candidate results
        candidate_results = (
            f"{candidate}:{ vote_percentage:.1f}% ({votes:,})\n")
        
        #print each candidate results
        print(candidate_results)
        #save candidate results to text file.
        txt_file.write(candidate_results)
    
        # determine winning vote count and candidate
        if(votes>winning_count) and (vote_percentage>winning_percentage):
            # 2. If true ten set winning_count = votes and winning_percent = vote percentage
            winning_count=votes
            winning_percentage=vote_percentage
            winning_candidate=candidate
    

    #winning candidate summary
    winning_candidate_summary = (
        "-----------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-----------------------------\n")
    #Print winning candidate summary
    print(winning_candidate_summary)
    #save winning candidate summary to text file
    txt_file.write(winning_candidate_summary)







