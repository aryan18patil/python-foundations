"""
Write a program that allows the user to edit the following list of names:

names = ["John", "Jane", "Peter", "Paul", "Michael", "Mary", "Robert", "Roland"]
The program prompts the user to enter "A" to add a new name to the list or "D" to delete a name from the list. You can assume the user will always enter either an "A" or a "D" at the
prompt.

If the user enters "A" then the program prompts the user to enter a new name, and then prompts the user to enter the name in the list they want to insert the new name before. While the
user enters a name that is not in the list of names, the program informs them of their error and re-prompts them to enter the name in the list they want to insert the new name before, as
in the example below. Once the user enters a name that is in the list, the program inserts the new name before this name.

If the user enters "D" then the program prompts the user to enter the name in the list they want to delete. While the user enters a name that is not in the list of names, the program
informs them of their error and re-prompts them to enter the name in the list they want to delete. Once the user enters a name that is in the list, the program deletes this name.

Finally, the program prints the updated list of names.
"""

names = ["John", "Jane", "Peter", "Paul", "Michael", "Mary", "Robert", "Roland"]
print(f"Current list of names: {names}")

task = input("Enter A to add a name or D to delete a name: ")

if task == "A":
    new_name = input("Enter a new name: ")
    
    while new_name in names:
        print(f"{new_name} is in the list of names!")
        new_name = input("Enter a new name: ")
        
    insert_before = input(
        "Enter the name you want to insert the new name before: "
    )
    
    while insert_before not in names:
        print(f"{insert_before} is not in the list of names!")
        insert_before = input(
            "Enter the name you want to insert the new name before: "
        )
        
    names.insert(names.index(insert_before), new_name)
    
else:
    name_to_delete = input("Enter a name to delete: ")
    
    while name_to_delete not in names:
        print(f"{name_to_delete} is not in the list of names!")
        name_to_delete = input("Enter a name to delete: ")
        
    names.remove(name_to_delete)
    
print(f"Updated list of names: {names}")
