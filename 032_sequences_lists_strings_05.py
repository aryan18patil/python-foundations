"""
Write a function called remove_vowels(sentence) that accepts a sentence as a parameter and returns the sentence with all the vowels removed. Note that both uppercase and lowercase vowels
should be removed.
"""

def remove_vowels(sentence):
    vowels = "aeiouAEIOU"
    
    new_sentence = ""
    index = 0
    while index < len(sentence):
        if sentence[index] not in vowels:
            new_sentence += sentence[index]
            
        index += 1
        
    return new_sentence
