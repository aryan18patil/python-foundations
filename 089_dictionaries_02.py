"""
Define a function named convert_dictionary(scores_dictionary) which takes a dictionary as a parameter and returns a new dictionary. The key of each item in the parameter dictionary is a
word and the value is a numerical score assigned to the word. The function creates a new dictionary based on the parameter dictionary. The key of each item in the new dictionary is a word
score and the value is a sorted list of words that have the same scores. For example, the following code fragment:

a_dict = {'beat': 24, 'fish': 38, 'of': 19, 'beta':24 }
print(convert_dictionary(a_dict))

produces:

{24: ['beat', 'beta'], 38: ['fish'], 19: ['of']}


Note:

You can assume that the parameter dictionary is not empty and is valid.
The list of words of each dictionary item must be sorted in alphabetical order.
"""

def convert_dictionary(code_dictionary):
    new_dict = {}
    
    for word, code in code_dictionary.items():
        if code in new_dict:
            new_dict[code].append(word)
            
        else:
            new_dict[code] = [word]
            
    for words_list in new_dict.values():
        words_list.sort()
        
    return new_dict

a_dict = {'cars': 37, 'beat': 24, 'arcs': 37, 'beta':24 , 'out': 53, 'can': 15}
print(convert_dictionary(a_dict))
