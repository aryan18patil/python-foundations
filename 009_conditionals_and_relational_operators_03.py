"""
The result of dividing a number by zero is undefined. Write a program that asks the user to enter a numerator (the value at the top of a fraction) and the denominator (the value at the
bottom of a fraction). The program should produce a decimal number that is equal to the fraction (numerator / denominator), displayed with a precision of 2 decimal places, or "Undefined"
if the denominator is 0.

The input format is:

Enter the numerator: 
Enter the denominator: 
And the output format is: 

Result: [result]
"""

numerator = int(input("Enter the numerator: "))
denominator = int(input("Enter the denominator: "))

if denominator == 0:
    print("Result: Undefined")
    
else:
    result = numerator / denominator
    print(f"Result: {result:.2f}")
