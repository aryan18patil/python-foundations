"""
Complete the append_content_summary() function that takes a single string parameter filename that specifies the name of the text file the function will append content to.


The function should:

1) Read the contents of the specified text file. You can assume that the text file will always contain a paragraph of text.

2) Analyze the contents to determine the following information:
   The total number of characters in the text file.
   The number of alphabetical letters in the text file.
   The number of words in the text file. You can assume that the words in a paragraph are separated by space characters.

3) Append to the text file, the following content:
   A blank line.
   The line 'Number of characters: ' followed by the total number of characters in the text file.
   The line 'Number of letters: ' followed by the total number of alphabetical letters in the text file.
   The line 'Number of words: ' followed by the total number of words in the text file.


Note:

Remember to close any file you open.
"""

def append_content_summary(filename):
    with open(filename, "r") as input_stream:
        full_text = input_stream.read()
        total_chars = len(full_text)
        
        total_letters = 0
        for char in full_text:
            if char.isalpha():
                total_letters += 1
                
        words_list = full_text.split()
        total_words = len(words_list)
        
    with open(filename, "a") as output_stream:
        output_stream.write(f"\n\nNumber of characters: {total_chars}\n")
        output_stream.write(f"Number of letters: {total_letters}\n")
        output_stream.write(f"Number of words: {total_words}")

def print_contents(filename):
    with open(filename, 'r') as input_file:
        content = input_file.read()
    print(content)

content = (
    "The Lamborghini Countach is a rear mid-engine, rear-wheel-drive sports car produced by the Italian automobile manufacturer Lamborghini from 1974 until 1990. It is one of the many "
    "exotic designs developed by Italian design house Bertone, which pioneered and popularized the sharply angled 'Italian Wedge' shape. The first showing of the Countach prototype was at "
    "the 1971 Geneva Motor Show, as the Lamborghini LP500 concept."
)
filename = '086_file_writing_04_file.txt'
with open(filename, 'w') as input_stream:
    input_stream.write(content)
append_content_summary(filename)
print_contents(filename)
