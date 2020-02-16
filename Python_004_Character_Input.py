# Character Input
# Alexander Fraser
# 16 February 2020

"""
Create a program that asks the user to enter their name
and their age. Print out a message addressed to them
that tells them the year that they will turn 100 years old.
"""

def main():
    input_name = input("What is your name?")
    input_age = int(input("What is your age?"))
    input_repeat = int(input("How many times should the message be repeated?"))

    current_year = 2020
    year_of_age_100 = current_year + 100 - input_age

    for _ in range(0, input_repeat):
        print("{}, you will turn 100 in the year {}".format(input_name, year_of_age_100))

if __name__ == "__main__":
    main()