"""
Write a program that implements Newton’s method to compute and display the square root of a number entered by the user. The algorithm for Newton’s method is as follows:

Read a number (an integer) from the user
Initialize guess to number / 2
While guess is not good enough do
Update guess to be the average of guess and number / guess

When this algorithm completes, guess contains an approximation of the square root of the number entered by the user. The quality of the approximation depends on how you define “good
enough”. This is the tolerance for precision that we use when comparing floating-point values.

For your program, you must set the tolerance to be 0.01. Use the math.isclose() function to determine if the difference between guess * guess and the number entered by the user is less
than or equal to 0.01. The guess should be rounded to 2 decimal places when displayed.
"""

import math

number = int(input("Enter the number: "))

guess = number / 2

while not math.isclose((guess ** 2), (number), abs_tol=0.01):
    guess = ((guess) + (number / guess)) / (2)
    
print(f"Estimated square root of {number} is {round(guess, 2)}")
