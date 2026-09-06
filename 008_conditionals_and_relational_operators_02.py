"""
Write a program that accepts an integer value representing a day, and prints out the name of the corresponding day, where Monday is day 1, Tuesday is day 2 and so on.  Numbers should be
between 1 and 7. Any number outside the range 1-7 should result in the message "Invalid day." being printed.


The input prompt should be:

Enter the day number:


The output should have the format:

Day [day_number] is [day_name].
"""

day_number = int(input("Enter the day number: "))

if day_number == 1:
    print(f"Day {day_number} is Monday.")
    
elif day_number == 2:
    print(f"Day {day_number} is Tuesday.")
    
elif day_number == 3:
    print(f"Day {day_number} is Wednesday.")
    
elif day_number == 4:
    print(f"Day {day_number} is Thursday.")
    
elif day_number == 5:
    print(f"Day {day_number} is Friday.")
    
elif day_number == 6:
    print(f"Day {day_number} is Saturday.")
    
elif day_number == 7:
    print(f"Day {day_number} is Sunday.")
    
else:
    print("Invalid day.")
