"""
Complete the get_list_of_words_start_with() function which takes a single string parameter - filename - representing the name of a text file the function will read. The first line of the
text file will contain a single lowercase alphabetical character - the target letter. The rest of the text file will consist of one or more lines of text. The function will analyse the
text and print out the list of unique words that start with the target letter (either lowercase or uppercase).


Note:

Remember to close the input file.
The words from the file are to be converted into lowercase.
The list of unique words should be printed out in alphabetical order.
"""

def print_unique_words_starting_with(filename):
    with open(filename, "r") as input_stream:
        target_letter = input_stream.read(1).strip()
        words = input_stream.read().strip().split()
        words_list = []
        
        for word in words:
            if (
                (word[0].lower() == target_letter)
                and (word.lower() not in words_list)
            ):
                words_list.append(word.lower())
                
    words_list.sort()
        
    print(f"Unique words starting with '{target_letter}': {words_list}")

filename = "081_file_reading_04_sentences.txt"
print_unique_words_starting_with(filename)
