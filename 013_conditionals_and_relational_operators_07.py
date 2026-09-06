"""
Most years have 365 days. However, the time required for the Earth to orbit the Sun is actually slightly more than that. As a result, an extra day, February 29, is included in some years
to correct for this difference. Such years are referred to as leap years. The rules for determining whether or not a year is a leap year follow:

Any year that is divisible by 400 is a leap year.
Of the remaining years, any year that is divisible by 100 is not a leap year.
Of the remaining years, any year that is divisible by 4 is a leap year.
All other years are not leap years.


Write a program that reads a year from the user and displays a message indicating whether or not it is a leap year.  The format for the input prompt is:
Enter the year:

Your program should produce output in the form:
year] is a leap year
or
[year] is not a leap year


You can assume the user will enter a valid year.
"""

year = int(input("Enter the year: "))
is_year_leap = False

if year % 400 == 0:
    is_year_leap = True
    
elif year % 100 == 0:
    is_year_leap = False
    
elif year % 4 == 0:
    is_year_leap = True
    
if is_year_leap:
    print(f"{year} is a leap year")
    
else:
    print(f"{year} is not a leap year")
