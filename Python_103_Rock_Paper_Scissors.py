# Rock, Paper, Scissors
# Alexander Fraser
# 25 February 2020

"""
A one-player Rock-Paper-Scissors game.
"""

from random import randint

def collect_input():
    valid_entries = ["r", "p", "s"]

    while True:
        user_play = input("Enter rock (r), paper (p), or scissors (s): ")
        if user_play in valid_entries:
            break
        else:
            print("Invalid entry. Try again.")

    return user_play

def get_computer_play():
    valid_entries = ["r", "p", "s"]

    computer_number = randint(1,3)
    computer_play = valid_entries[computer_number - 1]

    return computer_play

def compare_plays(user_play, computer_play):
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
    while True:
        user_play = collect_input()
        computer_play = get_computer_play()
        compare_plays(user_play, computer_play)

if __name__ == "__main__":
    main()