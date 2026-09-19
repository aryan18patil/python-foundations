"""
Complete the word_puzzle(horizontal_str, vertical_str)function that takes two string parameters horizontal_str and vertical_str. The function checks whether these two strings have a
character in common and prints them out so that they intersect at this shared character.

If the two strings have more than a single character in common, the first shared character is used.

If the two strings do not have a character in common, the function should print the following message: "The two strings do not intersect".

You can assume that both parameter strings are at least one character long and consist only of lowercase alphabetical characters.


Example:

word_puzzle("hello","world") should result in:
  w
  o
  r
hello
  d
  
"""

def word_puzzle(horizontal_str, vertical_str):
    common_char = False
    count = 0
    
    while (count < (len(horizontal_str))) and (not common_char):
        if horizontal_str[count] in vertical_str:
            v_index = vertical_str.find(horizontal_str[count])
            h_index = count 
            common_char = True
        count += 1
            
    if not common_char:
        print("The two strings do not intersect")
        
    else:
        for i in range(len(vertical_str)):
            if i == v_index:
                print(f"{horizontal_str}")
                
            else:
                print(f"{h_index * " "}{vertical_str[i]}")

word_puzzle("hello","world")
word_puzzle("colony","yummy")
word_puzzle("zero","match")
