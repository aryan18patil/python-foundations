"""
Complete the check_password(password) function that takes a single string parameter - a password. The function checks the password and returns True if the password is valid and False
otherwise. For a password to be valid it needs to meet the following criteria:

Has to be at least 8 characters in length.
Has to have at least one alphabetical character.
Has to have at least one numerical digit.
Has to have at least one of the following symbols: . ; ! * ?
"""

def check_password(password):
    symbols = ".;!*?"
    
    if len(password) >= 8:
        alpha_count = 0
        digit_count = 0
        special_count = 0
        
        for char in password:
            if char.isalpha():
                alpha_count += 1
            
            elif char.isdigit():
                digit_count += 1
            
            elif char in symbols:
                special_count += 1
            
        if (alpha_count >= 1) and (digit_count >= 1) and (special_count >= 1):
            output = True
            
        else:
            output = False
            
    else:
        output = False
        
    return output

password = "abc012"
print("Is",password,"valid:",check_password(password))

password = "abcd0123"
print("Is",password,"valid:",check_password(password))

password = "dAmIr007!"
print("Is",password,"valid:",check_password(password))
