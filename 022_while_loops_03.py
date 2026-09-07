"""
Write a program that simulates a countdown. The program should ask the user to enter a positive integer number between 1 and 9 inclusive. The sequence of integer numbers should be
displayed in descending order from 10 to the positive integer entered by the user, both included. Each number should be on a new line. After the last integer is printed, the program should
display "Countdown aborted!"


Note:
You may assume the user will always enter a positive integer between 1 and 9 inclusive.
"""

number = int(input("Enter a positive integer between 1 and 9: "))

count = 10
while count >= number:
    print(count)
    count -= 1
    
print("Countdown aborted!")
