"""
Write a program which prompts the user to enter two words and displays "Bingo!" if the two words end with the same character and only one (but not both) of the words begin with a vowel
letter, and displays "Oops!" otherwise.


Notes:

You can assume that the two words are in lower case.
"""

word_1 = input("Enter a first word: ")
word_2 = input("Enter a second word: ")

vowels = "aeiou"

if (
    (((word_1[0] in vowels) and (word_2[0] not in vowels)) or
    ((word_1[0] not in vowels) and (word_2[0] in vowels))) and
    word_1[-1] == word_2[-1]
):
    print("Bingo!")
            
else:
    print("Oops!")
