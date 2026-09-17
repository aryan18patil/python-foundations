"""
Write a program that prompts the user to enter a line of data. You can assume that each item of data is separated by a space character. Your program should convert this line of data into
a corresponding list of data. If a data item in this list is a valid string representation of an integer, it needs to be converted into an integer value. You can assume that you will only
be dealing with non-negative integers. Finally, your program should print out the data list.


Note:

You must use a for...in loop and the range() function.
The output of the program must be in the format shown in the examples below, including the format of the prompt, and all spaces and punctuation.
You may find the isdigit function helpful
"""

line_of_data = input("Enter your data: ")

list_of_data = line_of_data.split()

for index in range(len(list_of_data)):
    if list_of_data[index].isdigit():
        list_of_data[index] = int(list_of_data[index])
        
print(f"List of data: {list_of_data}")
