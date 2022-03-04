counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not in the list of counties.")

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso are in the list of counties.")
else:
    print("Arapahoe and El Paso is not in the list of counties.")

if "Arapahoe" in counties and "El Paso" not in counties:
   print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

for county in counties:
    print(county)
    
numbers = [0,1,2,3,4]
for num in numbers:
    print(num)

numbers = [0,1,2,3,4]
for num in range(5):
    print(num)

for i in range(len(counties)):
    print(counties[i])

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county in counties_dict.keys():
    print(county)

for voters in counties_dict.values():
    print(voters)

for county in counties_dict:
    print(counties_dict[county])

for county in counties_dict:
    print(counties_dict.get(county))

for county, voters in counties_dict.items():
    print(county, voters)

#print each county and registered voter from the counties dictionary in sentence output
for county, voters in counties_dict.items():
    print(county,f'county has', voters,f'registered voters')

#create three dictionaries with a county and number of voters
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

#print on the county name from each dictionary
for county_dict in voting_data:
    print(county_dict["county"])

#Print each county and registered voter form the counties dictionary so that the output looks like this:
    #Arapahoe county has 369237 registered voters.
    #Denver county has 413229 registered voters.
    #Jefferson county has 390222 registered voters.  
counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

#calculate the percentage of votes using f-string literals.
my_votes = int(input("How many votes did you get in the election?"))
total_votes = int(input("What is the total votes in the election? "))
percentage_votes = (my_votes / total_votes) * 100
print("I received" + str(percentage_votes)+"% of the total votes")

#calculate the percentage of votes using f-strings
my_votes = int(input("How many votes did you get in the election?"))
total_votes = int(input("What ws the total votes in the eelection?"))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")

#print each county and registered voter from the counties dictionary.
counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

#print each county and registered voter from the counties dictionary using f-string
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters")

#Multiline F-Strings
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the eelection "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidates_votes / total_votes * 100}% of the total votes.")

print(message_to_candidate)

#add a thousands seperator to the output for candidate and format % 2 decimal places
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total numbere of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes. ")

Print(message_to_candidate)

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#1. Initialize a total vote counter.
total_votes = 0

# Open the election results and read the file. 
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        #2. Add to the toal vote count.
        total_votes +=1

# 3. Print the total votes.
print(row)



