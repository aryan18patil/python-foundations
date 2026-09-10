"""
Write a program that repeatedly asks the user to enter an amount of money that includes both dollars and cents until they enter valid input. The input must:

include at least one digit before the decimal point
include a decimal point
include exactly 2 digits after the decimal point


Any other characters are considered invalid input. You cannot assume the input is valid, so your program must handle any character used as input.


Note:

Negative values will not be entered.
"""

amount = input("Enter an amount: ")

valid = False
while not valid:
    parts = amount.split(".")
    
    if len(parts) == 2:
        dollars = parts[0]
        cents = parts[1]
        
        if (
            (len(dollars) >= 1) and dollars.isdigit() and
            (len(cents) == 2) and cents.isdigit()
        ):
            valid = True

    if not valid:
        amount = input("Enter an amount: ")

print(f"{amount} is a valid amount.")
