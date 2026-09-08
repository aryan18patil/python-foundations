"""
The Fibonacci sequence is a sequence of integer values such that each number is the sum of the two preceding ones, starting with 0 and 1. As such, the beginning of the sequence is:

0, 1, 1, 2, 3, 5, 8, 13, 21, ...


Write a program that asks the user to enter a number n, and displays the first n values of the Fibonacci sequence (i.e., if the number entered is 3 then we would expect 3 values to be
displayed).
"""

n = int(input("Enter a number: "))

previous = 0
current = 1
count = 0

while count < n:
    if count == (n - 1):
        print(previous)
    else:
        print(previous, end=", ")
        
    value = previous + current
    previous = current
    current = value
    
    count += 1
