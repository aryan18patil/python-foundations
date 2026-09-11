"""
Write a program which asks the user to enter text and then displays a table showing the number of times each vowel appears in the text. If no occurrences of a given vowel is present, then
the corresponding row in the table will not be displayed (i.e., only the vowels that are present are displayed). Additionally, the text should be displayed with all the vowels removed.
Your program should count the vowels regardless of whether they are in upper or lower case (i.e., 'A' and 'a' are both counted as an occurrence of the letter 'a').

The prompt should be:
Enter the text:

The output should be in the format:

'a' appears [occurrences_of_a] times.
'e' appears [occurrences_of_e] times.
'i' appears [occurrences_of_i] times.
'o' appears [occurrences_of_o] times.
'u' appears [occurrences_of_u] times.
Without vowels the text is: [text_with_vowels_removed]


Notes:

Any vowels that are not present in the text will not be reported in the output.
The word "times" is used even when there is a single occurrence of a vowel.
Both upper and lower case letters are counted as the same vowel and displayed as shown above with a lower case letter to represent the vowel.
The non-vowel letters remain in the same case as the original input (i.e., the case of the non-vowel letters is not changed).
Do not write your own functions for this program.
"""

text = input("Enter the text: ")

updated_text = ""
a_count = 0
e_count = 0
i_count = 0
o_count = 0
u_count = 0

for char in text:
    if char in "aA":
        a_count += 1
        
    elif char in "eE":
        e_count += 1
        
    elif char in "iI":
        i_count += 1
        
    elif char in "oO":
        o_count += 1
        
    elif char in "uU":
        u_count += 1
        
    else:
        updated_text += char
        
vowel_count_list = [a_count, e_count, i_count, o_count, u_count]
vowels_list = ["a", "e", "i", "o", "u"]
index = 0
while index < len(vowel_count_list):
    if vowel_count_list[index] > 0:
        print(
            f"'{vowels_list[index]}' "
            f"appears {vowel_count_list[index]} times."
        )
    
    index += 1
    
print(f"Without vowels the text is: {updated_text}")
