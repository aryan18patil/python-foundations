"""
Bulls and Cows is an old codebreaking game where a player needs to guess a 4 digit number. Each digit in this number, referred to as the secret, is unique. When the user makes a guess,
each digit in their guess is compared with the digits in secret. Matching digits in the same position are referred to as Bulls. Matching digits in the wrong position are referred to as
Cows. For example, if 1234 is the secret, and the guess is 3215, then there is 1 Bull (2) and 2 Cows (1 and 3).

Complete the bulls_and_cows(guess, secret) function that takes two integer lists as parameters - guess and secret. You can assume that each digit in both lists are unique. The function
should return a tuple of two integer values. The first value is the number of Bulls and the second value is the number of Cows.
"""

def bulls_and_cows(guess, secret):
    bulls = 0
    cows = 0
    
    for i in range(len(guess)):
        if guess[i] in secret:
            if guess[i] == secret[i]:
                bulls += 1
                
            else:
                cows += 1
                
    return (bulls, cows)

secret = [4, 2, 7, 1]
guess = [1, 2, 3, 4]
result_tuple = bulls_and_cows(guess, secret)
print(type(result_tuple))
print("Bulls:", result_tuple[0], "Cows:", result_tuple[1])

secret = [5, 6, 7, 8]
guess = [1, 2, 3, 4]
result_tuple = bulls_and_cows(guess, secret)
print("Bulls:", result_tuple[0], "Cows:", result_tuple[1])
