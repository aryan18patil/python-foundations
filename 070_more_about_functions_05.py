"""
Complete the following code:

The get_consonant_counts() function takes a single string parameter - text. This string consists of words, each separated by a single space. Each word only consists of alphabetical
characters. The function analyses the text and returns a list of the consonant counts for each word in text. Vowels are the letters "A", "E", "I", "O" and "U". All the other letters are
consonants. The function is case insensitive. It calls two helper functions described below.

The get_words() function takes a single string parameter - text. The function returns a list of the words in text.

The count_consonants() function takes a single string parameter - word. The function returns an integer value representing the number of consonants in word.
"""

def get_consonant_counts(text):
    words = get_words(text)
    consonant_counts = []
    for word in words:
        consonant_counts.append(count_consonants(word))
    return consonant_counts

def get_words(text):
    words = text.split()
    return words

def count_consonants(word):
    consonant_count = 0
    for char in word:
        if char not in "aeiouAEIOU":
            consonant_count += 1
    return consonant_count

text = "The QuicK BRown fOx jUMPs OVEr thE lAZy Dog"
print(get_consonant_counts(text))

text = "On whAT winGS Dare hE aSPire What the HAND daRe sEiZe THe FIre"
print(get_consonant_counts(text))
