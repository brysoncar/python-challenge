#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

#Read .csv document from machine

budget=pd.read_csv('~/OneDrive/desktop/bootcamp/budget_data.csv')

#find total profits using .sum 

total_profits = budget["Profit/Losses"].sum()

#to find monthly changes create a variable using the .diff function on the profits and losses series

monthly_change = budget["Profit/Losses"].diff()

#calculations to find number of months using len of unique values, and min, max, and mean of monthly_budget

total_months = budget["Date"].unique()
largest_increase = monthly_change.max()
largest_decrease = monthly_change.min()
average_change = monthly_change.mean()

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
print(f"Greatest Increase in Profits: (${round(largest_increase)})")
print("")
print(f"Greatest Decrease in Profits: (${round(largest_decrease)})")

#Print the results to a blank file in the same folder as budget_data csv

f = open('OneDrive\Desktop\Bootcamp\Budget_Output.txt', "w")
print("Financial Analysis", file=f)
print("", file=f)
print("----------------------------------", file=f)
print("", file=f)
print(f"Total Months: {len(total_months)}", file=f)
print("", file=f)
print(f"Total: ${round(total_profits)}", file=f)
print("", file=f)
print(f"Average Change: ${round(average_change,2)}", file=f)
print("", file=f)
print(f"Greatest Increase in Profits: (${round(largest_increase)})", file=f)
print("", file=f)
print(f"Greatest Decrease in Profits: (${round(largest_decrease)})", file=f)
f.close()


# In[ ]:




