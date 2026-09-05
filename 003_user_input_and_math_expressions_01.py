"""
Write a program that asks the user to enter a total number of minutes, and displays the equivalent in number of days, hours, and remaining minutes.

Use exactly the following prompt:

Enter the total number of minutes: 1886
1886 minutes is equal to XXX days, YYY hours, and ZZZ minutes.
Standard conversions:

1 year = 365 days
1 week = 7 days
1 day = 24 hours
1 hour = 60 minutes
1 minute = 60 seconds
"""

total_minutes = int(input("Enter the total number of minutes: "))

days = (total_minutes) // (60 * 24)
hours = ((total_minutes) % (60 * 24)) // (60)
remaining_minutes = (total_minutes) - ((days * 24 * 60) + (hours * 60))

print(f"{total_minutes} minutes is equal to {days} days, {hours} hours, and {remaining_minutes} minutes.")
