"""
Write a program that asks the user to enter a string, and then asks the user to enter a letter. The program should display the index of the first occurrence of that letter, and the index
of the last occurrence of that letter.  If the letter appears only once then the first and last index will be the same. If the letter does not appear in the string, then the program should
print the message:

The letter [letter] does not appear in [string].


The input prompt should be:

Enter the string:
Enter the letter:


The output should have the format:

The index of the first occurrence of [letter] in [string] is [index].
The index of the last occurrence of [letter] in [string] is [index].


Notes:

Keep the original capitalization.
Letters with different capitalization (e.g., "A" and "a") are treated as different letters.
Any string can be entered.  It does not need to be a single word.
"""

text = input("Enter the string: ")
letter = input("Enter the letter: ")

if letter not in text:
    print(f"The letter {letter} does not appear in {text}.")
    
else:
    first_position = len(text)
    index = 0
    while (index < len(text)) and (first_position == len(text)):
        if text[index] == letter:
            first_position = index
            
        index += 1
            
    reversed_text = text[::-1]
    
    last_position = len(text)
    index_2 = 0
    while (index_2 < len(reversed_text)) and (last_position == len(text)):
        if reversed_text[index_2] == letter:
            last_position = index_2
            
        index_2 += 1
        
    print(
        f"The index of the first occurrence of {letter} in {text} is "
        f"{first_position}."
    )
    
    print(
        f"The index of the last occurrence of {letter} in {text} is "
        f"{len(text) - 1 - last_position}."
    )
