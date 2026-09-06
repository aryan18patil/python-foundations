"""
A quadratic equation is given by the formula y = ax^2 + bx + c. Write a program that asks the user to enter the coefficients a, b and c, then calculates and displays the roots for the
equation.


Notes:

The results for the roots must be displayed with a precision of 2 decimal places.
You may assume the input coefficients will be integer values.
"""

import math

a = int(input("Enter the value for a: "))
b = int(input("Enter the value for b: "))
c = int(input("Enter the value for c: "))

discriminant = (b ** 2) - (4 * a * c)

if discriminant > 0:
    root_1 = (-b - (math.sqrt(discriminant))) / (2 * a)
    root_2 = (-b + (math.sqrt(discriminant))) / (2 * a)
    print(f"There are two roots: {root_1:.2f} and {root_2:.2f}")

elif discriminant == 0:
    root = (-b) / (2 * a)
    print(f"There is a single root: {root:.2f}")

else:
    print("There is no root in the space of real numbers.")
