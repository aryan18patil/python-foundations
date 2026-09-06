"""
Assume the laws about schooling in a given country include the following:

Below the age of 5 you may not enrol in school.
At the age of 5, you may enrol in a school.
At the age of 6 (and over), you must have started school.


Write a program that asks the user to enter their age. For every age, your program should display one of the following messages, based on the rules described above:

You may not attend school.
You may start school, but you do not have to.
You must have started school.


Note:

The input age may be a floating point value.
"""

age = float(input("Enter your age: "))

if age < 5:
    print("You may not attend school.")
    
elif 5 <= age < 6:
    print("You may start school, but you do not have to.")
    
else:
    print("You must have started school.")
