"""
Complete the get_digit_frequency() function that takes a single string parameter text. The function processes the text and returns a list of tuples where each tuple consists of a digit
and its corresponding frequency in the parameter text (i.e., how often it appears in the text). Things to note:

Only digits are considered by the function. Characters that are not digits are ignored.
Only digits that occur at least once in the text should appear in the list.
The tuples in the list should be sorted in ascending order, from smallest to largest, based on the digits being considered.
"""

def get_digit_frequency(text):
    f_list = []
    n_list = []
    
    for i in range(len(text)):
        if text[i].isdigit():
            if text[i] in n_list:
                position = n_list.index(text[i])
                f_list[position][1] += 1
                
            else:
                n_list.append(text[i])
                f_list.append([int(text[i]), 1])
                
    f_list.sort()
    
    for i in range(len(f_list)):
        f_list[i] = tuple(f_list[i])
        
    return f_list

text = "a1b2c3d4e5f6"
frequency_tuple = get_digit_frequency(text)
print(f"Type: {type(frequency_tuple)}")
print(f"Type: {type(frequency_tuple[0])}")
print(f"Frequency Tuple: {frequency_tuple}")

text = "AbCdEF11223344556670"
frequency_tuple = get_digit_frequency(text)
print(f"Frequency Tuple: {frequency_tuple}")

text = "asdhq3094asdjkl9qwe845134132j4qsd789asd890q34"
frequency_tuple = get_digit_frequency(text)
print(f"Frequency Tuple: {frequency_tuple}")
