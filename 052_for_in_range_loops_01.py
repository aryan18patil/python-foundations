"""
Write a Python program which asks the user to enter a number n, and then loops through the integers from 1 to n (inclusive) printing the following.

When the integer is a multiple of 3, the program prints "Fizz".
When the integer is a multiple of 5, the program prints "Buzz".
When the integer is a multiple of 3 and 5, the the program prints "FizzBuzz".
In all other cases, the program prints the integer.
For this exercise, you must use a for...in loop and the range() function.

Note:
You can assume that the user will always enter an integer value.
"""

number = int(input("Enter a number: "))

for n in range(1, (number + 1)):
    if (n % 3 == 0) and (n % 5 != 0):
        print("Fizz")
        
    elif (n % 3 != 0) and (n % 5 == 0):
        print("Buzz")
        
    elif (n % 3 == 0) and (n % 5 == 0):
        print("FizzBuzz")
        
    else:
        print(n)
