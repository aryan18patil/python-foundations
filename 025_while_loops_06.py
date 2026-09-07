"""
A prime number is a number greater than 1 that is only divisible by 2 numbers: itself and 1.  Write a program that asks the user to enter a number and determines if the number is prime or
not.

If the number is prime, then display a message stating the same.
Otherwise, display a message stating that the number is not prime, and a message on the next line stating the value of it's first divisor after 1.
"""

number = int(input("Enter a number: "))

divisor = 2
prime = True
while (divisor < number) and (prime):
    if number % divisor == 0:
        factor = divisor
        prime = False
    
    divisor += 1
    
if number == 1:
    prime = False
    
if (prime):
    print(f"{number} is prime.")
    
elif (not prime) and (number != 1):
    print(f"{number} is not prime.")
    print(f"{number} is divisible by {factor}.")
        
else:
    print("1 is not prime.")
    print("1 is divisible by 1.")
