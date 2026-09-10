"""
HTML (Hypertext Markup Language) is a markup language used to format content designed to be displayed in a web browser. Content is annotated using HTML tags. All HTML tags have the
following format:

<tag_name>


For example, the name of the tag <p> is p, while the name of the tag </body> is /body.

Write a program that prompts the user to enter some text. The program processes this text and adds all the names of the HTML tags contained in the text into a list. Finally, the program
prints this list of HTML tag names.


Note:

Ignore content that is not part of an HTML tag.
"""

text = input("Enter your text: ")

html_tags_list = []
in_tag = False
current_tag = ""

for char in text:
    if char == "<":
        in_tag = True
        current_tag = ""
        
    elif char == ">" and in_tag:
        html_tags_list.append(current_tag)
        in_tag = False
        
    elif in_tag:
        current_tag += char

print(f"List of HTML tags: {html_tags_list}")
