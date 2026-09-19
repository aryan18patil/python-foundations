"""
Complete the function remove_ints_from_list(data_list), which takes a list, data_list, as a parameter. The data_list parameter will only contain string and/or integer objects. The
remove_ints_from_list() function removes all integer elements from data_list.
"""

def remove_ints_from_list(data_list):
    for index in range((len(data_list) - 1), -1, -1):
        if isinstance(data_list[index], int):
            data_list.pop(index)

data_list = [1,"hello",2,3,"world"]
remove_ints_from_list(data_list)
print(data_list)
