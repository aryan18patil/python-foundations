"""
Write a program that repeatedly asks the user to enter numbers (or blank to exit). After the user enters a blank line, the numbers will be sorted into ascending order and displayed  as a
sorted list. The program will also calculate and display the median value.


Notes:

You can assume all the input numbers will be integer values.
"""

number = input("Enter a number (blank to exit): ")

numbers_list = []
while number != "":
    numbers_list.append(int(number))
    number = input("Enter a number (blank to exit): ")
    
sorted_numbers_list = sorted(numbers_list)

if len(sorted_numbers_list) % 2 != 0:
    median = sorted_numbers_list[(len(sorted_numbers_list) // 2)]
    
else:
    median = (
        ((sorted_numbers_list[(len(sorted_numbers_list) // 2) - 1]) +
        (sorted_numbers_list[len(sorted_numbers_list) // 2])) /
        2
    )
    
print(f"Data: {sorted_numbers_list}")
print(f"Median: {median}")
