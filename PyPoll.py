#!/usr/bin/env python
# coding: utf-8

# In[41]:


import pandas as pd
election=pd.read_csv('~/OneDrive/desktop/bootcamp/election_data.csv')

#find the total number of votes 

total_votes = election["Ballot ID"].count()

#Find the votes for each candidate 

charles_votes = election["Candidate"].value_counts()['Charles Casper Stockham']
diana_votes = election["Candidate"].value_counts()['Diana DeGette']
raymon_votes = election["Candidate"].value_counts()['Raymon Anthony Doane']

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

#Print the results to a blank file in the same folder as election_data csv

f = open('OneDrive\Desktop\Bootcamp\Election_Output.txt', "w")
print("Election Results", file=f)
print("", file=f)
print("----------------------------------", file=f)
print("", file=f)
print(F"Total Votes: {total_votes}", file=f)
print("", file=f)
print("----------------------------------", file=f)
print("", file=f)
print(f"Charles Casper Stockham: {round(charles_per,3)}% ({charles_votes})", file=f)
print("", file=f)
print(f"Diana DeGette: {round(diana_per,3)}% ({diana_votes})", file=f)
print("", file=f)
print(f"Raymon Anthony Doane: {round(raymon_per,3)}% ({raymon_votes})", file=f)
print("", file=f)
print("----------------------------------", file=f)
print("", file=f)
print(f"Winner: {election_winner}", file=f)
print("", file=f)
print("----------------------------------", file=f)
f.close()


# In[ ]:




