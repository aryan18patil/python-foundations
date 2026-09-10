"""
Write a program that asks the user to enter a line of integers. You can assume that the line will contain at least 1 integer value, and that the integer values will be separated by a
comma (","). The program then prints out the even integers in this line. The even integers are printed out on a single line, with a comma and a space (", ") separating each even integer.
"""

line_of_integers = input("Enter a line of integer values: ")

integers_list = line_of_integers.split(",")

even_int_list = []
for integer in integers_list:
    if int(integer) % 2 == 0:
        even_int_list.append(integer)
        
even_int_string = ", ".join(even_int_list)

print(f"The even integers are: {even_int_string}")
