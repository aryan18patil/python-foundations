"""
Complete the get_common_elements(list1, list2) function which is passed two Python lists as parameters. The function returns a sorted list of all the elements which are elements of both
parameter lists.

Note: you may assume that both the parameter lists are unique, i.e. each element only occurs once in the list.
"""

def get_common_elements(list1, list2):
    common_elements_list = []
    
    for element in list1:
        if element in list2:
            common_elements_list.append(element)
            
    common_elements_list.sort()
    return common_elements_list

numbers1 = [3, 78, 785, 4, 99, 677, 23, 9]
numbers2 = [3, 2, 9, 4]
print(get_common_elements(numbers1, numbers2))

print(get_common_elements([], [3, 23, 77, 4]))
