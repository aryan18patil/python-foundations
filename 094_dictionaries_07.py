"""
Complete the update_dictionary() function that takes two parameters:

a_dict - a dictionary object where the keys are single letters and the values are integers.
target_value - an integer value.

The function updates a dictionary by removing all key/value pairs where the value is equal to the target_value. Note that the function does not create a new dictionary object or return a
value. It simply updates the dictionary object passed to it.
"""

def update_dictionary(a_dict, target_value):
    dict_list = list(a_dict.keys())
    
    for key in dict_list:
        if a_dict[key] == target_value:
            del a_dict[key]
            
    return dict_list

a_dict = {'a': 24, 'b': 11, 'c': 12, 'd': 20, 'e': 9, 'f': 21,
          'g': 24, 'h': 26, 'i': 11, 'j': 14, 'k': 9, 'l': 11}
print("Before:", end=" ")
keys = list(a_dict.keys())
for key in keys:
    print(f"{key}:{a_dict[key]}", end=" ")
print()
update_dictionary(a_dict, 11)
print("After:", end=" ")
keys = list(a_dict.keys())
for key in keys:
    print(f"{key}:{a_dict[key]}", end=" ")
print()
