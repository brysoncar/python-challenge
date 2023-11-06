#Dependencies
import pandas as pd
from pathlib import Path

# Load in file
# Store filepath in a variable
election_file = Path("Resources/election_data.csv")

# Read the CSV and store the header row
election_df = pd.read_csv(election_file)

#store the header row

header = election_df.columns

#find the total number of votes 

total_votes = election_df["Ballot ID"].count()

#Find the votes for each candidate 

charles_votes = election_df["Candidate"].value_counts()['Charles Casper Stockham']
diana_votes = election_df["Candidate"].value_counts()['Diana DeGette']
raymon_votes = election_df["Candidate"].value_counts()['Raymon Anthony Doane']

#find the percentage of votes

charles_per = charles_votes / total_votes * 100
diana_per = diana_votes / total_votes * 100
raymon_per = raymon_votes / total_votes *100

#Find the winner with an if statement

if charles_votes > diana_votes and charles_votes > raymon_votes:
    election_winner = "Charles Casper Stockham"
elif  diana_votes > charles_votes and diana_votes > raymon_votes:
    election_winner = "Diana DeGette"
elif raymon_votes > diana_votes and raymon_votes > charles_votes:
    election_winner = "Raymon Anthony Doane"

#Print the results to terminal
           
print("Election Results")
print("")
print("----------------------------------")
print("")
print(F"Total Votes: {total_votes}")
print("")
print("----------------------------------")
print("")
print(f"Charles Casper Stockham: {round(charles_per,3)}% ({charles_votes})")
print("")
print(f"Diana DeGette: {round(diana_per,3)}% ({diana_votes})")
print("")
print(f"Raymon Anthony Doane: {round(raymon_per,3)}% ({raymon_votes})")
print("")
print("----------------------------------")
print("")
print(f"Winner: {election_winner}")
print("")
print("----------------------------------")

#Print the results to a the analysis folder inside a file called PyPoll Results
#creta a variable valled text_to_save of the results

text_to_save = f"""Election Results

----------------------------------

Total Votes: {total_votes}

----------------------------------

Charles Casper Stockham: {round(charles_per,3)}% ({charles_votes})

Diana DeGette: {round(diana_per,3)}% ({diana_votes})

Raymon Anthony Doane: {round(raymon_per,3)}% ({raymon_votes})

----------------------------------

Winner: {election_winner}

----------------------------------
"""

# Define the file path

file_path = "analysis/PyPoll_Results.txt"

# write the results in the .txt file called PyPoll_Results

with open(file_path, "w") as file:
    file.write(text_to_save)