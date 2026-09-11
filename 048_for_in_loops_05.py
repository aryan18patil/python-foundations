"""
Complete the get_unique_3_letter_words(text) function which is passed a string of text as a parameter. The text consists of words separated by white space. The function returns a sorted
list of all the unique words in the parameter text which have a length of 3. All the words in the returned list should be in lowercase characters.
"""

def get_unique_3_letter_words(text):
    
    sentence_list = text.split()
    
    unique_words_list = []
    for word in sentence_list:
        if (len(word) == 3) and (word not in unique_words_list):
            unique_words_list.append(word.lower())
            
    unique_words_list.sort()
    return unique_words_list

sentence = "In the not too distant future technology may provide a solution to the problem"
words_list = get_unique_3_letter_words(sentence)
print(words_list)

words_list = get_unique_3_letter_words("I have nothing to declare except my genius")
print(words_list)
