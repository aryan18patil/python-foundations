"""
Complete the analyse_words() function that takes a single string parameter - text. The string text consists of one or more words, separated by white space. You can assume that there are
no duplicate words in the text. The function goes through these words creating a dictionary where each item is a key-value pair:

Key - An integer representing how many vowels a word has.
Value - A list containing the words in text that have this many vowels. Vowels are the letters 'a', 'e', 'i', 'o', and 'u'. This list should be sorted in alphabetical order.
Note that the function should be case insensitive and be able to handle uppercase and lowercase vowels.
"""

def analyse_words(text):
    words_list = text.split()
    words_list.sort()
    vowels_dict = {}
    vowels = "aeiouAEIOU"
    
    for word in words_list:
        word_vowels = 0
        for char in word:
            if char in vowels:
                word_vowels += 1
                
        if word_vowels in vowels_dict:
            vowels_dict[word_vowels].append(word)
            
        else:
            vowels_dict[word_vowels] = [word]
            
    return vowels_dict

text = "The quick brown fox jumps over a lazy dog"
word_analysis_dict = analyse_words(text)
for key in sorted(word_analysis_dict):
    print(key, word_analysis_dict[key])
print()

text = "PETER PIPER picked a PECK of pickled peppers"
word_analysis_dict = analyse_words(text)
for key in sorted(word_analysis_dict):
    print(key, word_analysis_dict[key])
print()
