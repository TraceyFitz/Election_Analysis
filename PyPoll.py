

# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = ("../Election_Analysis/Resources/election_results.csv")
#file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0
# Candidate options and candidate votes
candidate_options = []
candidate_votes = {}

# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#County names and County Votes 
county_names=[]
county_votes={}

#track winning county 
largest_county_turnout=""
largest_county_vote=0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes=total_votes+1
        # Get the candidate name from each row.
        candidate_name= row[2]
        county_name=row[1]
        # If the candidate does not match any existing candidate add it the
        # the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        if county_name not in county_names:
            # Add the clounty name to the county list.
            county_names.append(county_name)
            # And begin tracking that county's voter count.
            county_votes[county_name] = 0
        # Add a vote to that county's count
        county_votes[county_name] += 1
        
#Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)
    
    # Determine the percetnage of votes for each candidate by looping through the counts.
    # Iterate through the candidate list. 
    for county in county_votes:
        # Retrieve vote count of a county.
        county_vote = county_votes[county]
        # Calculate the percentage of votes.
        county_percentage = float(county_vote) / float(total_votes) * 100

        #  To do: print out each county's name, vote count, and percentage of
        # votes to the terminal.
        county_results=(f"{county}: {county_percentage:.1f}% ({county_vote:,})\n")
        print(county_results)
        txt_file.write(county_results)
        # Determine winning vote cound and candidate 
        # Determine if the votes is great than the winning count.
        if (county_vote > largest_county_vote):
            # If true then set winning_count = votes and winning percent =
            # vote_percentage.
            largest_county_vote = county_vote
            largest_county_turnout = county
            
            

    winning_county_summary = (
        f"-------------------------\n"
        f"Largest County Turnout:  {largest_county_turnout}\n"
        f"-------------------------\n")

    print(winning_county_summary)
    txt_file.write(winning_county_summary)



    # Determine the percetnage of votes for each candidate by looping through the counts.
    # Iterate through the candidate list. 
    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate.
        votes = candidate_votes.get(candidate_name)
        # Calculate the percentage of votes.
        votes_percentage = float(votes) / float(total_votes) * 100

        #  To do: print out each candidate's name, vote count, and percentage of
        # votes to the terminal.
        candidate_results=(f"{candidate_name}: {votes_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)
        # Determine winning vote cound and candidate 
        # Determine if the votes is great than the winning count.
        if (votes > winning_count) and (votes_percentage > winning_percentage):
            # If true then set winning_count = votes and winning percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = votes_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)

