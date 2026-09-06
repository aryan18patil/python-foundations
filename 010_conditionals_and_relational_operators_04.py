"""
Easter is celebrated on the Sunday immediately after the first full moon following the spring equinox. Because its date includes a lunar component, Easter does not have a fixed date in the
Gregorian calendar. Instead, it can occur on any date between March 22 and April 25. The month and day for Easter can be computed for a given year using the Anonymous Gregorian Computus
algorithm.

Use the algorithm to write a program that asks the user to enter a year, and displays the month and day for Easter Sunday on that year.
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

print(f"In {year}, Easter will occur on day {day} of month {month}")
