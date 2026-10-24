"""
The digital root of a number is the single digit value obtained by an interative process of summing digits. On each iteration, the digit sum from the previous iteration is used to compute
the digit sum for the current iteration, with the process continuing until a single digit number is reached.

For example, given the number 12345, the digital root is 6.

12345 = 1 + 2 + 3 + 4 + 5
      = 15
      = 1 + 5
      = 6
      
Complete the digital_root() function that takes a single non-negative integer (that has at least two digits), number, as its parameter. The function calculates and returns the digital
root of this number.
"""

def digital_root(number):
    number_str = str(number)
    
    while len(number_str) != 1:
        digital_root = 0
        
        for char in number_str:
            n = int(char)
            digital_root += n
            
        number_str = str(digital_root)
        
    return digital_root

number = 9054
print(f"Digital Root of {number} = {digital_root(number)}")
