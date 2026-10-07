"""
Complete the write_selected_items() function that takes 3 parameters:

input_filename - a string representing the name of the input text file.
output_filename - a string representing the name of the output text file.
max_price - a floating point value.
The function should:

Read the contents of the input text file. The input text file will contain one or more lines of text. Each line of text will contain the details of one item at a grocery store in the following format: name:price
Identify all of the items that cost up to and including the specified maximum price. The items should be sorted in ascending order based on their price.
Write the selected items to the output text file, one item per line in the following format: name: $price
Note:

Remember to close any file you open.
"""

def write_selected_items(input_filename, output_filename, max_price):
    with open(input_filename, "r") as input_stream:
        with open(output_filename, "w") as output_stream:
            line = input_stream.readline().strip()
            
            lines_list_to_sort = []
            while line != "":
                line_list = line.split(":")
                
                if float(line_list[1]) <= max_price:
                    lines_list_to_sort.append(
                        [(float(line_list[1]), line_list[0]),
                        (f"{line_list[0]}: ${line_list[1]}\n")]
                    )
                    
                line = input_stream.readline().strip()
                
            lines_list_to_sort.sort()
            for i in range(len(lines_list_to_sort)):
                output_stream.write(lines_list_to_sort[i][1])

def print_contents(filename):
    with open(filename, 'r') as input_file:
        content = input_file.read()
    print(content)

input_filename = "085_file_writing_03_read_file.txt"
output_filename = '085_file_writing_03_write_file.txt'
max_price = 3.79
write_selected_items(input_filename, output_filename, max_price)
print_contents(output_filename)
