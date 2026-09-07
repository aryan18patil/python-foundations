"""
Prime factors of an integer 'n' are a set of prime numbers that can be multiplied together to obtain 'n'.

Write a program that asks the user to enter a number and displays the prime factors ordered from smallest to largest. If the number entered by the user is less than 2 then there are no
prime factors and the message "No prime factors" should be displayed.


Note:

You can assume that the number entered by the user will be an integer number.
"""

n = int(input("Enter a number: "))

factor = 2

if n < 2:
    print("No prime factors")

else:
    print(f"The prime factors of {n} are:")

    while factor <= n:
        if n % factor == 0:
            print(factor)
            n //= factor

        else:
            factor += 1
    
