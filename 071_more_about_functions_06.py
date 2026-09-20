"""
Complete the word_puzzle(horizontal_str, vertical_str)function that takes two string parameters horizontal_str and vertical_str. The function checks whether these two strings have a
character in common and prints them out so that they intersect at this shared character.

If the two strings have more than a single character in common, the first shared character is used.

Notes:
You MUST use two helper functions.
You can assume that both parameter strings are at least one character long and consist only of lowercase alphabetical characters.
"""

def word_puzzle(horizontal_str, vertical_str):
    output(find_common_char(horizontal_str, vertical_str))
    
def find_common_char(horizontal_str, vertical_str):
    common_char = False
    count = 0
    h_index = len(horizontal_str)
    v_index = len(vertical_str)
    
    while (count < (len(horizontal_str))) and (not common_char):
        if horizontal_str[count] in vertical_str:
            v_index = vertical_str.find(horizontal_str[count])
            h_index = count 
            common_char = True
        count += 1
        
    info_list = [common_char, v_index, h_index, len(horizontal_str), len(vertical_str), horizontal_str, vertical_str]
    return info_list
        
def output(info_list):
    if not info_list[0]:
        print("The two strings do not intersect")
        
    else:
        for i in range(info_list[4]):
            if i == info_list[1]:
                print(f"{info_list[5]}")
                
            else:
                print(f"{info_list[2] * " "}{info_list[6][i]}")

    print()

word_puzzle("hello","world")
word_puzzle("colony","yummy")
word_puzzle("zero","match")
