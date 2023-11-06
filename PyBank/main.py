#Dependencies
import pandas as pd
from pathlib import Path

# Load in file
# Store filepath in a variable
budget_file = Path("Resources/budget_data.csv")

# Read the CSV and store the header row
budget_df = pd.read_csv(budget_file)

#store the header row

header = budget_df.columns

#find total profits using .sum 

total_profits = budget_df["Profit/Losses"].sum()

#calculations to find number of months using len of unique values, and min, max, and mean of monthly_budget

total_months = budget_df["Date"].unique()
largest_increase = monthly_change.max()
largest_decrease = monthly_change.min()
average_change = monthly_change.mean()

#to include the month with the print out of biggest increase and decrease in profits use indexing

#add the monthly_change variable to the table as a column first
budget_df['monthly_change'] = monthly_change

#index by the min and max of the Profit/Loss column

min_index = budget_df['monthly_change'].idxmin()
max_index = budget_df['monthly_change'].idxmax()

#get the month value from date column

min_date = budget_df.loc[min_index, 'Date']
max_date = budget_df.loc[max_index, 'Date']
#print out the results 

print("Financial Analysis")
print("")
print("----------------------------------")
print("")
print(f"Total Months: {len(total_months)}")
print("")
print(f"Total: ${round(total_profits)}")
print("")
print(f"Average Change: ${round(average_change,2)}")
print("")
print(f"Greatest Increase in Profits: {max_date} (${round(largest_increase)})")
print("")
print(f"Greatest Decrease in Profits: {min_date} (${round(largest_decrease)})")

#Print the results to a the analysis folder inside a file called PyBank Results
#creta a variable valled text_to_save of the results

text_to_save = f"""Financial Analysis

----------------------------------

Total Months: {len(total_months)}

Total: ${round(total_profits)}

Average Change: ${round(average_change,2)}

Greatest Increase in Profits: {max_date} (${round(largest_increase)})

Greatest Decrease in Profits: {min_date} (${round(largest_decrease)})
"""

# Define the file path

file_path = "analysis/PyBank_Results.txt"

# write the results in the .txt file called PyPoll_Results

with open(file_path, "w") as file:
    file.write(text_to_save)