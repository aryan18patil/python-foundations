"""
CONCEPT (2): User Input and Math Expressions
Question: Before decimalisation in 1971, the British currency system used pounds, shillings, and pence. 

Write a program that asks the user to enter a total number of pence, and displays the equivalent in pounds, shillings, and remaining pence.

Currency conversions:
1 pound = 20 shillings
1 shilling = 12 pence

Use exactly the following prompt format for your input and output:

Enter the total number of pence: 854
854 pence is equal to 3 pounds, 11 shillings, and 2 pence.
"""

total_pence = int(input("Enter the total number of pence: "))

pounds = (total_pence) // (20 * 12)
shillings = (total_pence % (20 * 12)) // (12)
remaining_pence = total_pence % 12

print(f"{total_pence} pence is equal to {pounds} pounds, {shillings} shillings, and {remaining_pence} pence.")
