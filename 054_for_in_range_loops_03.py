"""
Write a program that:

Asks the user to enter an integer.
Asks the user to enter a list of integers, separated by spaces.
Multiplies each item in the list by the integer entered.
Updates the list in-place and displays the updated list.
Notes:

You can assume that the user will enter valid input.
Use a for...in range() loop with indices to update the list.
"""

integer = int(input("Enter an integer: "))
integers_string = input("Enter a list of integers: ")

integers_list = integers_string.split()

for index in range(len(integers_list)):
    integers_list[index] = integer * int(integers_list[index])
    
print(integers_list)
