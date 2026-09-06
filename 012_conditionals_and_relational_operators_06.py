"""
Write a program that asks the user to enter the name of a day.  The program should determine if the day is a working day (Monday, Tuesday, Wednesday, Thursday or Friday) or a weekend day
(Saturday or Sunday), and print a corresponding message "[day] is a weekend/working day."

You may assume the input name is a valid day.
"""

day = input("Enter the name of a day: ")

if (day == "Saturday") or (day == "Sunday"):
    print(f"{day} is a weekend day.")
    
else:
    print(f"{day} is a working day.")
