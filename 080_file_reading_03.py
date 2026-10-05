"""
Complete the process_transactions() function that takes a single string parameter, filename. This parameter specifies the name of the file the function will open and read its contents
from.

The files opened by the function are text files formatted as follows: The first line of the text file consists of a name. The second and subsequent lines of the text file consist of
transactions, one per line. A transaction consists of a name, followed by a ":", followed by an integer amount (can be positive or negative).

The function will loop through all transactions, and calculate the total value of all transactions for the person whose name is in the first line of the file.

The function will return a tuple consisting of the name and the total value of all transactions for the person with that name.
"""

def process_transactions(filename):
    with open(filename, "r") as input_stream:
        line = input_stream.readline().strip()
        name = line
        total_value = 0
        
        line = input_stream.readline().strip()
        while line != "":
            line_list = line.split(":")
            if line_list[0] == name:
                total_value += int(line_list[1])
                
            line = input_stream.readline().strip()
            
    return (name, total_value)

filename = "080_file_reading_03_Transactions1.txt"
transaction_data = process_transactions(filename)
if transaction_data[1] < 0:
    print(f"The sum of transactions for {transaction_data[0]} = -${transaction_data[1] * -1}")
else:
    print(f"The sum of transactions for {transaction_data[0]} = ${transaction_data[1]}")

filename = "080_file_reading_03_Transactions1.txt"
print(f"Function return type: {type(process_transactions(filename))}")
