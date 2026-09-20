"""
Complete the get_palindrome() function that prompts the user to enter a palindrome. A palindrome is a word that reads the same both backward and forward. For example, "madam" is a
palindrome. The function should ignore case.

Note: You must implement at least one helper function as part of your solution.
"""

def get_palindrome():
    program_intro()
    determine_palindrome()
    
def program_intro():
    print("This program requires you to enter a palindrome.")
    print()
    
def determine_palindrome():
    word = input("Enter a palindrome: ")
    is_palindrome = False
    
    while not is_palindrome:
        if word.upper().split() == word[::-1].upper().split():
            is_palindrome = True
            print(f"Cool! {word} is a palindrome.")
            
        else:
            print(f"{word} is not a palindrome! Try again!")
            word = input("Enter a palindrome: ")

get_palindrome()
