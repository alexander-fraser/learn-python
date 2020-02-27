# Cows and Bulls
# Alexander Fraser
# 26 February 2020

"""
Randomly generate a 4-digit number. Ask the user to guess
a 4-digit number. For every digit that the user guessed
correctly in the correct place , they have a "cow". For
every digit the user guessed correctly in the wrong place
is a "bull". Every time the user makes a guess, tell them
how many "cows" and "bulls" they have. Once the user guesses
the correct number, the game is over. Keep track of the number
of guesses the user makes throughout teh game and tell the user
at the end.
"""

from random import randint

def generateNumber():
    number = ''

    for i in range(0,4):
        digit = randint(0,9)
        number += str(digit)

    print(number)
    return number

def collectInput():
    while True:
        try:
            user_guess = raw_input("Enter 4-digit guess or exit: ")
            if user_guess == "exit":
                break
            else:
                user_guess_int = int(user_guess)

            if user_guess_int in range(0,10000):
                break
            else:
                print("Invalid entry. Try again.")

        except:
            print("Invalid entry. Try again.")

    user_guess = str(user_guess)
    return user_guess

def comparePlays(userPlay, number, counter):
    if userPlay == number:
        print("Correct! It took you {} tries.").format(counter)
        return False
    else:
        cows = 0
        bulls = 0
        for i in range(0,4):
            if userPlay[i] == number[i]:
                cows += 1

        for digit in userPlay:
            if digit in number:
                bulls += 1

        bulls = bulls - cows
        print("You have {} cows and {} bulls.").format(cows, bulls)

        return True

def main():
    while True:
        print("Welcome to the cows and bulls game!")
        counter = 0
        number = generateNumber()

        while True:
            counter += 1
            userPlay = collectInput()
            if userPlay == "exit":
                break
            result = comparePlays(userPlay, number, counter)
            if result == False:
                break

        if userPlay == "exit":
            break

if __name__ == "__main__":
    main()