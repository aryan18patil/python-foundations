"""
Write a program that asks the user to enter two integer numbers, a factor and a maximum. The program should print all the multiples of the factor that are between 1 and the maximum
(inclusive).

Notes:


You can assume that both numbers entered by the user will be positive integer numbers.
The numbers that are multiples should be printed one per line (i.e., each number is on a line by itself).
"""

factor = int(input("Enter a factor: "))
maximum = int(input("Enter a maximum: "))

counter = 1
while counter <= maximum:
    if counter % factor == 0:
        print(counter)
        
    counter += 1
