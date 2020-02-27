# Cows and Bulls
# Alexander Fraser
# 26 February 2020

"""
Requirements:
- Python_005_Odd_or_Even

Randomly generate a 4-digit number. Ask the user to guess
a 4-digit number. For every digit that the user guessed
correctly in the correct place , they have a "cow". For
every digit the user guessed correctly in the wrong place,
they have a "bull". Every time the user makes a guess, tell them
how many "cows" and "bulls" they have. Once the user guesses
the correct number, the game is over. Keep track of the number
of guesses the user makes throughout teh game and tell the user
at the end.
"""

from random import randint
from Python_005_Odd_or_Even import collect_integer


def generate_number():
    # Generate a 4-digit string of random integers.
    number = ''

    for _ in range(0,4):
        digit = randint(0,9)
        number += str(digit)

    return number


def compare_plays(user_play, number, counter):
    # Tells the player if they guessed correctly.
    # Otherwise tells them how many cows and bulls they have.
    if user_play == number:
        print("Correct! It took you {} tries.".format(counter))
        return False
    else:
        cows = 0
        bulls = 0
        for i in range(0,4):
            if user_play[i] == number[i]:
                cows += 1

        for digit in user_play:
            if digit in number:
                bulls += 1

        bulls = bulls - cows
        print("You have {} cows and {} bulls.".format(cows, bulls))

        return True


def main():
    # The main gameplay loop. Will continue indefinitely until player
    # chooses to quit.
    while True:
        print("Welcome to the cows and bulls game!")
        counter = 0
        number = generate_number()

        while True:
            counter += 1
            user_play = collect_integer("Enter 4-digit guess: ", 1000, 9999)
            user_string = str(user_play)
            
            result = compare_plays(user_string, number, counter)
            if result == False:
                break

        user_continue = input("Would you like to play again (y/n)?")
        if user_continue != "y":
            break


if __name__ == "__main__":
    main()