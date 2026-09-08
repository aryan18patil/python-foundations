"""
Consider the following series:

1 + x + x^2 + ... + x^n


For small values of 'x', this series converges to the function f = 1 / (1 − x)
.

Write a program which asks the user to enter 2 float values corresponding to 'x' and to the precision of the approximation. The program calculates the number of terms needed for the series
to approximate the function 'f' with the precision required by the user.


Note:

The user will always enter an 'x' value lower than 1.
"""

import math

x = float(input("Enter x: "))
precision = float(input("Enter the precision required: "))

series_result = 1
terms = 1

while not math.isclose((series_result), (1 / (1 - x)), abs_tol=precision):
    series_result += x ** terms
    terms += 1
    
print(
    f"{terms} term(s) is/are needed to approximate "
    f"the function with a precision of {precision}"
)
