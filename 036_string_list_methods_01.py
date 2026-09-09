"""
Write a function called is_palindrome(sentence) that returns True if the sentence is a palindrome and False otherwise. A palindrome is a sentence that has letters in the same order when
reversed, ignoring all spaces and punctuation. For example, the sentence "Madam, I'm Adam" is a palindrome.
"""

def is_palindrome(sentence):
    index = 0
    alpha_sentence = ""
    while index < len(sentence):
        if sentence[index].isalpha():
            alpha_sentence += sentence[index].lower()

        index += 1

    if alpha_sentence == alpha_sentence[::-1]:
        output = True

    else:
        output = False

    return output

print(is_palindrome("Madam, I'm Adam"))
print(is_palindrome("Andrew Andrew"))
print(is_palindrome("Kayak"))
