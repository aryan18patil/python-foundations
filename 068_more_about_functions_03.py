"""
Complete the get_target_word() function that prompts the user to enter a target word. A target word is a word with at least 3 vowels. Vowels are the letters "A", "E", "I", "O" and "U".
The function needs to be able to handle both uppercase and lowercase vowels.

Note: You must implement at least one helper function as part of your solution.
"""

def get_target_word():
    display_intro()
    determine_target_word()
    
def display_intro():
    print("This program requires you to enter a target word.")
    print("Target words have at least 3 vowels.")
    print()
    
def determine_target_word():
    word = input("Enter a target word: ")
    target_word = False
    
    while not target_word:
        vowel_count = 0
        for char in word:
            if char in "aeiouAEIOU":
                vowel_count += 1
                
        if vowel_count < 3:
            print(f"{word} is not a target word! Try again!")
            word = input("Enter a target word: ")
            
        else:
            print(f"Cool! Your target word is {word}")
            target_word = True

get_target_word()
