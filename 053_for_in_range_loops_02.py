"""
Write a Python program that asks the user to enter:

positive integer as the maximum limit.
A positive integer as a factor.


The program should then print all the numbers from 0 up to the maximum limit (both inclusive) that are exactly divisible by the factor. All numbers should be printed on one line, separated
by a single space, including a space after the last number.
"""

maximum = int(input("Enter the maximum limit: "))
factor = int(input("Enter the factor: "))

for number in range(0, (maximum + 1), factor):
    print(number, end=" ")
    
print()
