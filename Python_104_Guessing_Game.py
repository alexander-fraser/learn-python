# Guessing Game
# Alexander Fraser
# 26 February 2020

"""
Requirements:
- Python_005_Odd_or_Even

Generate a random number between 1 and 9 (inclusive).
Ask the user to guess the number, then tell them whether
they guessed too low, too high, or exactly right.
"""

from random import randint
from Python_005_Odd_or_Even import collect_integer


def get_computer_play():
    computer_play = randint(1,9)
    return computer_play

def collect_input():
    while True:
        try:
            userGuess = raw_input("Enter guess (1-9) or exit: ")
            if userGuess == "exit":
                break
            else:
                userGuess = int(userGuess)

            if userGuess in range(0,10):
                break
            else:
                print("Invalid entry. Try again.")

        except:
            print("Invalid entry. Try again.")

    return userGuess

def compare_plays(user_play, computer_play, counter):
    if user_play == computer_play:
        print("Correct! It took you {} tries.").format(counter)
        return False
    elif user_play > computer_play:
        print("Too high.")
    else:
        print("Too low.")

def main():
    while True:
        counter = 0
        computer_play = get_computer_play()

        while True:
            counter += 1
            user_play = collect_input()
            if user_play == "exit":
                break
            result = compare_plays(user_play, computer_play, counter)
            if result == False:
                break

        if user_play == "exit":
            break

if __name__ == "__main__":
    main()