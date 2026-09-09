"""
Write a program that asks the user to enter a phrase. The program should print out an acronym consisting of the first letter of each word in the phrase. The acronym should be in capital
letters.

For example, if the phrase "personal identification number" is entered, then the program should print "PIN"
"""

phrase = input("Enter a phrase: ")

phrase_list = phrase.split()

index = 0
while index < len(phrase_list):
    print(f"{phrase_list[index][0].upper()}", end="")
    index += 1

print()
