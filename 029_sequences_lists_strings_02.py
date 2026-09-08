"""
When working with data, we often want to remove extreme values before analysing the data. These extreme values are known as outliers. Write a program that repeatedly asks the user to
enter numbers (or blank to exit). After the user enters a blank line, the two highest values, and the two lowest values should be removed from the data set. The program should analyse
the remaining numbers and display the minimum, maximum and mean, rounded to 2 decimal places.


Notes:

Treat all input values as floating point values.
If the list has fewer than 5 elements then treat each of the minimum, maximum and mean as "undefined"
"""

user_input = input("Enter a number (blank to exit): ")
numbers_list = []

while user_input != "":
    numbers_list.append(float(user_input))
    user_input = input("Enter a number (blank to exit): ")

if len(numbers_list) < 5:
    print("Minimum: undefined")
    print("Maximum: undefined")
    print("Mean: undefined")

else:
    new_numbers_list = sorted(numbers_list)[2:-2]

    minimum = min(new_numbers_list)
    maximum = max(new_numbers_list)
    average = sum(new_numbers_list) / len(new_numbers_list)

    print(f"Minimum: {round(minimum, 2)}")
    print(f"Maximum: {round(maximum, 2)}")
    print(f"Mean: {round(average, 2)}")
    
