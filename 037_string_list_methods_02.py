"""
Write a program that prompts the user to enter a password. The program processes the password and prints a message indicating whether or not the password is valid. A valid password needs
to meet the following criteria:

The password should have a length of at least 8 characters, but less than 15 characters.
The password must not include the substrings "123", "abc" or "pass".
The password should have at least 4 alphabetical characters.
The password should have at least 3 numerical characters.


Note:

The program must remove any leading and trailing white space from the password the user has entered.
"""

password = input("Please enter your password: ")

stripped_password = password.strip()

if (
        (8 <= len(stripped_password) < 15)
        and ("123" not in stripped_password)
        and ("abc" not in stripped_password)
        and ("pass" not in stripped_password)
):
    alpha_count = 0
    digit_count = 0
    index = 0
    while index < len(stripped_password):
        if stripped_password[index].isalpha():
            alpha_count += 1

        elif stripped_password[index].isdigit():
            digit_count += 1

        index += 1

    if (alpha_count >= 4) and (digit_count) >= 3:
        print("Your password is valid!")

    else:
        print("Your password is invalid!")

else:
    print("Your password is invalid!")
