"""
Write a program that asks the user to enter two lines of data. Each item of data is separated by a single space. You can assume that each line will have at least 1 item of data and that
both lines will have the same number of data items. If an item of data is numerical, you can assume that it will be an integer. 


The corresponding items in each line are merged and added to a new list as follows:

If both of the corresponding items are numerical, their sum (as an integer) is added to the new list.
Else, the corresponding items are concatenated as strings and added to the new list.


Note

You must use a for...in range() loop for this question.
The output of the program must be in the format shown in the examples below, including the format of the prompt, and all spaces and punctuation.
You may find the following methods useful: isdigit(), split() and append()
Integers can be positive, negative or zero. Think about how negative integers differ, and what you would need to do to handle this difference.
"""

line1 = input("Enter the first line of data: ")
line2 = input("Enter the second line of data: ")

list1 = line1.split()
list2 = line2.split()

merged_list = []
for index in range(len(list1)):
    if ("-" not in (list1[index])) and (list1[index].isdigit()):
        item1 = int(list1[index])
        
    elif ("-" in list1[index]) and (list1[index][1::].isdigit()):
        item1 = int(list1[index])
        
    else:
        item1 = list1[index]
        
    if ("-" not in (list2[index])) and (list2[index].isdigit()):
        item2 = int(list2[index])
        
    elif ("-" in list2[index]) and (list2[index][1::].isdigit()):
        item2 = int(list2[index])
        
    else:
        item2 = list2[index]
        
    if (isinstance(item1, int)) and (isinstance(item2, int)):
        merged_list.append(item1 + item2)
        
    else:
        merged_list.append(str(item1) + str(item2))
        
print(f"The merged data is: {merged_list}")
