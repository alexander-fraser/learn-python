# Rock, Paper, Scissors
# Alexander Fraser
# 25 February 2020

"""
A one-player Rock-Paper-Scissors game.
"""

from random import randint

def collectInput():
    validEntries = ["r", "p", "s"]

    while True:
        userPlay = raw_input("Enter rock (r), paper (p), or scissors (s): ")
        if userPlay in validEntries:
            break
        else:
            print("Invalid entry. Try again.")

    return userPlay

def getComputerPlay():
    validEntries = ["r", "p", "s"]

    computerNumber = randint(1,3)
    computerPlay = validEntries[computerNumber - 1]

    return computerPlay

def comparePlays(userPlay, computerPlay):
    if userPlay == computerPlay:
        print("Draw.")
    elif userPlay == "r" and computerPlay == "s":
        print("Player wins!")
    elif userPlay == "p" and computerPlay == "r":
        print("Player wins!")
    elif userPlay == "s" and computerPlay == "p":
        print("Player wins!")
    else:
        print("Computer wins.")

def main():
    while True:
        userPlay = collectInput()
        computerPlay = getComputerPlay()
        comparePlays(userPlay, computerPlay)

if __name__ == "__main__":
    main()