"""
Complete the print_ox_xo_pattern() function that takes two integer parameters:

number_of_rows - specifying the number of rows the pattern will have.
number_of_columns - specifying the number of characters in a row of the pattern.

Using these parameters, the function prints a pattern consisting of of alternating ‘o’ and ‘x’ characters. Even rows will start with an ‘o’ and odd rows will start with an ‘x’.

You can assume that both integer parameters are positive.
"""

def print_ox_xo_pattern(number_of_rows, number_of_columns):
    for y in range(number_of_rows):
        for x in range(number_of_columns):
            if y % 2 == 0:
                if x % 2 != 0:
                    print("x", end="")
                    
                else:
                    print("o", end="")
                    
            else:
                if x % 2 != 0:
                    print("o", end="")
                    
                else:
                    print("x", end="")
                    
        print()

print_ox_xo_pattern(5, 4)
