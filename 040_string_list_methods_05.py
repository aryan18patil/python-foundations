"""
Write a program that allows the user to insert a colour name in the following list, at a chosen position, only if this name is not already in the following list:

colours = ["Red", "Yellow", "Green", "Purple", "Orange", "Cyan", "Magenta"]


The user is asked to enter the colour name to be inserted, and the colour name it should be inserted before in the list. If the user wants to insert the new colour at the end, the user
enters "End". Then, the program inserts the new colour at the chosen position, and prints the updated list.

If the colour name to be inserted is already in the list, or if the colour name it should be inserted before is not in the list, then the program prints "The new colour is already in the
list or the preceding colour is not in the list.".
"""

colours = ["Red", "Yellow", "Green", "Purple", "Orange", "Cyan", "Magenta"]
print(f"Current list of colours: {colours}")

new_colour = input("Enter a new colour: ")
insert_before = input(
    "Enter the name of the colour you want to insert the "
    "new colour before: "
)

if (
        (new_colour not in colours)
        and ((insert_before in colours) or (insert_before == "End"))
):
    if insert_before != "End":
        colours.insert(colours.index(insert_before), new_colour)
        
    else:
        colours.append(new_colour)
        
    print(f"Updated list of colours: {colours}")
    
else:
    print(
        "The new colour is already in the list or the preceding colour is "
        "not in the list."
    )
