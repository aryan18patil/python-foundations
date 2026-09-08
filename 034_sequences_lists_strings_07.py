"""
Write a program that asks the user to enter an integer number and displays the number as a Binary number.
"""

decimal = int(input("Enter the decimal number: "))

if decimal == 0:
    print("0 in decimal is 0 in binary.")
    
else:
    dividend = decimal
    binary_list = []
    while dividend != 0:
        binary_list.append(dividend % 2)
        dividend //= 2
    
    print(f"{decimal} in decimal is ", end="")
    
    index = len(binary_list) - 1
    while index >= 0:
        print(f"{binary_list[index]}", end="")
        index -= 1
        
    print(" in binary.")
