"""
In the previous problem, you calculated the month and day of Easter Sunday for a given year.  

Modify this previous program to calculate the day of Easter Sunday and display the name of the month instead of the number (i.e., convert the month number into a month name and display the
name).
"""

year = int(input("Enter the year: "))

a = year % 19
b = year // 100
c = year % 100
d = b // 4
e = b % 4
f = (b + 8) // 25
g = (b - f + 1) // (3)
h = ((19 * a) + b - d - g + 15) % 30
i = c // 4
k = c % 4
m = (32 + (2 * e) + (2 * i) - h - k) % 7
n = (a + (11 * h) + (22 * m)) // 451
month = (h + m - (7 * n) + 114) // 31
day = (1) + ((h + m - (7 * n) + 114) % 31)
    
if month == 3:
    month_name = "March"
    
elif month == 4:
    month_name = "April"

print(f"Easter will occur on {day} {month_name}, {year}.")
