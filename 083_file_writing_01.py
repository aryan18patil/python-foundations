"""
Complete the write_ints_and_floats() function that takes 2 parameters:

number_list - a list of numerical values consisting of integers and floats. You can assume that this list will not be empty.
filename - a string representing the name of a text file.
The function should write two lines of text to the text file specified by the filename:

The first line should consist of the text "Integers: " followed by a list of integer values in the parameter list arranged in ascending order. Each integer is separated from the next by a
", " (comma space).

The second line should consist of the text "Floats: " followed by a list of the floats in the parameter list arranged in ascending order. Each float is separated from the next by a ", "
(comma space).


Note:

Remember to close the file.
"""

def write_ints_and_floats(number_list, filename):
    ints_list = []
    floats_list = []
    
    for n in number_list:
        if isinstance(n, int):
            ints_list.append(n)
        else:
            floats_list.append(n)
            
    ints_string = ""
    floats_string = ""
    
    ints_list.sort()
    for n in ints_list:
        ints_string += f"{n}, "
        
    floats_list.sort()
    for n in floats_list:
        floats_string += f"{n}, "
        
    with open(filename, "w") as output_stream:
        output_stream.write(f"Integers: {ints_string[:-2]}\n")
        output_stream.write(f"Floats: {floats_string[:-2]}")

def print_contents(filename):
    with open(filename, 'r') as input_file:
        content = input_file.read()
    print(content)

filename = '083_file_writing_01_file.txt'
number_list = [1, -1, 2, -2, 3, -3, 0.5, -1.5, 2.5, -3.75]
write_ints_and_floats(number_list, filename)
print("--- Output File Contents ---")
print_contents(filename)
