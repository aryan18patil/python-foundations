"""
Complete the remove_all_repeats(numbers_list) function which is passed a list of integers as a parameter. The function first sorts the parameter list and then removes any numbers which are
repeated (appear more than once in the list).

Note: the function updates the parameter list.
"""

def remove_all_repeats(numbers_list):
    numbers_list.sort()
    
    for index in range((len(numbers_list) - 2), -1, -1):
        if numbers_list[index] == numbers_list[index + 1]:
            numbers_list.pop(index)

numbers = [3, 71, 71, 3, 99, 3, 67, 88]
remove_all_repeats(numbers)
print(numbers)

numbers = [71, 71, 71, 71, 71, 71, 71, 71, 71, 71]
remove_all_repeats(numbers)
print(numbers)

numbers = [9, 71, 71, 9, 71, 9]
remove_all_repeats(numbers)
print(numbers)
