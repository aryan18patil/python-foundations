"""
Write a program that prompts the user to enter movie names. Each name entered by the user is added to a Python list, only if the name is not already in the list. When the user enters "end"
at the prompt, the program stops prompting them for names, sorts the list into ascending alphabetical order, then prints out the sorted list.
"""

movie_name = input("Please enter the movie name or end to print the list: ")

movie_list = []
while movie_name != "end":
    if movie_name not in movie_list:
        movie_list.append(movie_name)
        
    movie_name = input("Please enter the movie name or end to print the list: ")
    
movie_list.sort()
print(movie_list)
