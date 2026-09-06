"""
Write a program that asks the user to enter the name of a month, and the year.  The program will print out the number of days in that month. If the input is not a recognized month name,
then the program should display the message "Invalid month." instead.
"""

month = input("Enter the month: ")
year = int(input("Enter the year: "))

if month == "February":
    leap = False
    
    if year % 400 == 0:
        leap = True
        
    elif (year % 4 == 0) and (year % 100 != 0):
        leap = True
        
    if leap:
        print(f"{month} has 29 days.")
        
    else:
        print(f"{month} has 28 days.")
        
elif (month == "April") or (month == "June") or (month == "September") or (month == "November"):
    print(f"{month} has 30 days.")
    
elif (
    (month == "January") or (month == "March") or (month == "May") or (month == "July") or
    (month == "August") or (month == "October") or (month == "December")
):
    print(f"{month} has 31 days.")
    
else:
    print("Invalid month.")
