"""
Define a function called create_word_pair_dictionary(sentence) that takes a sentence as a parameter and returns a dictionary. The function creates a dictionary by looping through each
word in the sentence and creating a corresponding key : value item. The key of each item in the dictionary is a word and the value is the list of words in the parameter sentence that
immediately follow the word used as the key. For example, the following code fragment:

sentence = 'life is beautiful'
print(create_word_pair_dictionary(sentence))

produces:

{'life':['is'], 'is':['beautiful']}


Notes:

You can assume that the parameter string is not empty and contains lowercase string elements only.
The last word in the sentence will not be used as a key as it is not followed by another word.
The list of words in each dictionary item is to contain unique elements only (i.e. no duplicates) and should be sorted into alphabetical order.
"""

def create_word_pair_dictionary(sentence):
    word_pair_dict = {}
    words_list = sentence.split()
    
    for i in range(len(words_list) - 1):
        if words_list[i] in word_pair_dict:
            if words_list[i + 1] not in word_pair_dict[words_list[i]]:
                word_pair_dict[words_list[i]].append(words_list[i + 1])
            
        else:
            word_pair_dict[words_list[i]] = [words_list[i + 1]]
            
    for value in word_pair_dict.values():
        value.sort()
        
    return word_pair_dict

sentence = 'programming is fun'
data = create_word_pair_dictionary(sentence)
for key in sorted(data):
    print(key, data[key])

print()

sentence = 'we made it together'
print(create_word_pair_dictionary(sentence))
print()
