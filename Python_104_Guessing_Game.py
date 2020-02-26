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
    # Generates the computer's random integer.
    computer_play = randint(1,9)
    return computer_play


def compare_plays(user_play, computer_play, counter):
    # Tells the player if they guessed correctly.
    # Otherwise tells them if their guess was too high or too low.
    if user_play == computer_play:
        print("Correct! It took you {} tries.".format(counter))
        return False
    elif user_play > computer_play:
        print("Too high.")
    else:
        print("Too low.")


def main():
    # The main gamplay loop. Will continue indefinitely until player chooses to quit.
    while True:
        counter = 0
        computer_play = get_computer_play()

        while True:
            counter += 1
            user_play = collect_integer("Pick a random number between 1 and 9 (inclusive): ", 1, 9)

            result = compare_plays(user_play, computer_play, counter)
            if result == False:
                break

        user_continue = input("Would you like to play again (y/n)?")
        if user_continue != "y":
            break


if __name__ == "__main__":
    main()