"""
Write a program that asks the user to enter a number. After entering the number, the program should ask the user which operator they want to apply to the number. The possible operators
supported are: exponential, natural logarithm, base-10 logarithm and square root. The program should print the result of applying the operator to the number entered. If the user does not
enter a valid operator then the program should print the message "Operator not supported."


Notes:

Before displaying the result, the operand and result should both be rounded to 2 decimal places.
Consider that the user will enter "exp" for exponential, "log" for natural logarithm, "log10" for base-10 logarithm and "sqrt" for square root.
"""

import math

number = float(input("Enter a number: "))
operator = input("Enter an operator: ")

flag = 1

if operator == "exp":
    result = math.exp(number)

elif operator == "log":
    result = math.log(number)
    
elif operator == "log10":
    result = math.log10(number)
    
elif operator == "sqrt":
    result = math.sqrt(number)
    
else:
    print("Operator not supported.")
    flag = 0
    
if flag == 1:
    print(f"{operator}({round(number, 2)}) = {round(result, 2)}")
