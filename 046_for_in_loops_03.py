"""
Write a program which asks the user to enter a message. The program converts this message into Morse code, and prints the result. Two lists are provided to help convert the message. The
first list contains all the letters of the alphabet and also a space character, and the second list contains the corresponding Morse codes. An alphabet character is equivalent to the
Morse code which has the same index in the Morse code list.

char_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
             'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
             'S', 'T', 'U', 'V', 'W', 'X','Y', 'Z', ' ']
             
morse_list = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.',
              '....','..', '.---', '-.-', '.-..', '--', '-.',
              '---', '.--.', '--.-', '.-.', '...', '-', '..-',
              '...-', '.--', '-..-','-.--', '--..', ' ']


Notes:

The input message can be lower or upper case, and only contains alphabetical characters and spaces.
Each Morse code in the output is followed by a space.
It does not matter if your output includes a trailing space (i.e., spaces at the end of a line will be ignored).
"""

char_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
             'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
             'S', 'T', 'U', 'V', 'W', 'X','Y', 'Z', ' ']
morse_list = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.',
              '....','..', '.---', '-.-', '.-..', '--', '-.',
              '---', '.--.', '--.-', '.-.', '...', '-', '..-',
              '...-', '.--', '-..-','-.--', '--..', ' ']

message = input("Enter a text: ")

print("The translation in Morse code is: ", end="")              
for char in message:
    print(morse_list[char_list.index(char.upper())], end=" ")
