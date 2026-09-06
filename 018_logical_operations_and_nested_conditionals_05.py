"""
Write a program that asks the user to enter an hour of the day using the 24 hour clock.


The program should print a message that describes the time of day according to the following:

0:  It is midnight.
1 - 5:  It is night.
6 - 11:	 It is morning.
12:  It is midday.
13 - 17:  It is afternoon.
18 - 23:  It is evening.


Note: The input will be a valid integer value between 0 and 23 inclusive.
"""

hour = int(input("Enter the hour (0-23): "))

if hour == 0:
    print("It is midnight.")
    
elif 1 <= hour <= 5:
    print("It is night.")
    
elif 6 <= hour <= 11:
    print("It is morning.")
    
elif hour == 12:
    print("It is midday.")
    
elif 13 <= hour <= 17:
    print("It is afternoon.")
    
else:
    print("It is evening.")
