"""
Complete the function multiply_by_previous_item(integer_list) that takes a single integer list parameter: integer_list. The function iterates through the elements in integer_list, from the
second element onwards (i.e., from the list element with the index of 1 onwards) and multiplies each element by the value of the previous element in the list. The list is changed in place.
"""

def multiply_by_previous_item(integer_list):
    for index in range(1, len(integer_list)):
        integer_list[index] *= integer_list[index - 1]
        
    return integer_list

integer_list = [1,2,3,4,5,6]
multiply_by_previous_item(integer_list)
print(integer_list)

integer_list = [-1,2,-3,4,-5,6]
multiply_by_previous_item(integer_list)
print(integer_list)

integer_list = [0,1,2,3,4,5]
multiply_by_previous_item(integer_list)
print(integer_list)
