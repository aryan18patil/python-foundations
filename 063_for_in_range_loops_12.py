"""
Complete the function descending_remove_multiples(integer_list, factor) that takes two parameters: an integer list parameter, integer_list, and an integer, factor. The function sorts the
items in integer_list in descending order and removes all multiples of factor. The list is changed in place.
"""

def descending_remove_multiples(integer_list, factor):
    integer_list.sort(reverse=True)
    
    for index in range((len(integer_list) - 1), -1, -1):
        if integer_list[index] % factor == 0:
            integer_list.pop(index)

integer_list = [10, 45, 20, 55, 90, 105, 70, 185]
descending_remove_multiples(integer_list, 10)
print(integer_list)

integer_list = [-2, 2, 4]
descending_remove_multiples(integer_list, 3)
print(integer_list)

integer_list = [-2, 2, 4]
descending_remove_multiples(integer_list, 2)
print(integer_list)
