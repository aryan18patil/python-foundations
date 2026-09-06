"""
Define a function called guessing_game() that accepts a single parameter, goal (int). The function repeatedly prompts the user to guess a number between 1 and 50 inclusive, until the user
guesses the goal. If the guess is smaller then the number, the function should display "Bigger". If the guess is larger than the number, the function should display "Smaller". If the user
guesses the number correctly, the function should display "Congratulations!". The function should return the number of guesses entered by the user.


Note:

You can assume the user always enters a valid integer between 1 and 50
"""
def guessing_game(goal):
    guess = int(input("Enter your guess: "))

    count = 1
    while guess != goal:
        if guess < goal:
            print("Bigger")

        else:
            print("Smaller")

        guess = int(input("Enter your guess: "))
        count += 1

    print("Congratulations!")

    return count

print(f"You took {guessing_game(25)} guess(es)!")
print(f"You took {guessing_game(43)} guess(es)!")
