"""
Write a program that repeatedly prompts the user to enter an integer until they enter an integer that is in the list provided in the variable, data. The integer will then be displayed
using the message:

[integer] is valid.
"""

data = [1, 4, 9, 16, 25]
print(f"The given list is: {data}")

user_input = int(input("Enter an integer from the given list: "))

while user_input not in data:
    user_input = int(input("Enter an integer from the given list: "))
    
print(f"{user_input} is valid.")
