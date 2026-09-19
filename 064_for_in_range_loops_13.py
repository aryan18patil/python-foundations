"""
Complete the remove_from_odd_indices(numbers_list) function that takes a single parameter, an integer list called numbers_list. The function removes all the items in this list that are
located at odd indices. Note that this function does not create a new list or return a list - it modifies numbers_list in place.
"""

def remove_from_odd_indices(numbers_list):
    for index in range((len(numbers_list) - 1), -1, -1):
        if index % 2 != 0:
                numbers_list.pop(index)

numbers_list = [1]
print("Before:", numbers_list)
remove_from_odd_indices(numbers_list)
print("After:", numbers_list)

numbers_list = [1, 2, 3, 4, 5]
print("Before:", numbers_list)
remove_from_odd_indices(numbers_list)
print("After:", numbers_list)
