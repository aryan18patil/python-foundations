"""
Write a program that asks the user to enter some text and then prints out the total number of letters in that text. Both upper and lower case characters should be counted. Any characters
that are not letters should be ignored.
"""

text = input("Enter some text: ")

alpha_count = 0
index = 0
while index < len(text):
    if text[index].isalpha():
        alpha_count += 1
        
    index += 1
    
print(f"Total letters: {alpha_count}")
