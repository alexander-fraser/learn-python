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


def getComputerPlay():
    computerPlay = randint(1,9)
    return computerPlay

def collectInput():
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

def comparePlays(userPlay, computerPlay, counter):
    if userPlay == computerPlay:
        print("Correct! It took you {} tries.").format(counter)
        return False
    elif userPlay > computerPlay:
        print("Too high.")
    else:
        print("Too low.")

def main():
    while True:
        counter = 0
        computerPlay = getComputerPlay()

        while True:
            counter += 1
            userPlay = collectInput()
            if userPlay == "exit":
                break
            result = comparePlays(userPlay, computerPlay, counter)
            if result == False:
                break

        if userPlay == "exit":
            break

if __name__ == "__main__":
    main()