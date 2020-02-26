# Rock, Paper, Scissors
# Alexander Fraser
# 25 February 2020

"""
A one-player Rock-Paper-Scissors game.
"""

from random import randint


def collect_input():
    # Prompts the user for their input or to quit the game.
    valid_entries = ["r", "p", "s", "q"]

    while True:
        user_play = input("Enter rock (r), paper (p), or scissors (s). Enter (q) to quit: \n")
        if user_play in valid_entries:
            break
        else:
            print("Invalid entry. Try again.")

    return user_play


def get_computer_play():
    # Selects the "computer's play" at random.
    valid_entries = ["r", "p", "s"]

    computer_number = randint(1,3)
    computer_play = valid_entries[computer_number - 1]

    return computer_play


def compare_plays(user_play, computer_play):
    # Determines the winner of the round. Goes through every case where the player wins.
    if user_play == computer_play:
        print("Draw.")
    elif user_play == "r" and computer_play == "s":
        print("Player wins!")
    elif user_play == "p" and computer_play == "r":
        print("Player wins!")
    elif user_play == "s" and computer_play == "p":
        print("Player wins!")
    else:
        print("Computer wins.")


def main():
    # The main gamplay loop. It will loop until the player decides to quit.
    while True:
        user_play = collect_input()

        if user_play == "q":
            break

        computer_play = get_computer_play()
        compare_plays(user_play, computer_play)


if __name__ == "__main__":
    main()