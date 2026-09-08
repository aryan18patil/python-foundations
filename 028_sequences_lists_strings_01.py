"""
Write a function called match_parentheses(expression) that returns True if parentheses are used correctly within the expression and False otherwise. To use parentheses correctly,
parentheses must appear in pairs, with the opening parenthesis appearing before the closing parenthesis in the sequence.


Note:

Ignore all characters that are not parentheses.
"""

def match_parentheses(expression):
    check = 0
    index = 0
    
    while (check >= 0) and (index < len(expression)):
        if expression[index] == "(":
            check += 1

        elif expression[index] == ")":
            check -= 1

        index += 1

    if check == 0:
        output = True

    else:
        output = False

    return output

print(match_parentheses("((1 + 2) * (2 - (2 + 4) / 4))"))
print(match_parentheses("(( )))(() "))
