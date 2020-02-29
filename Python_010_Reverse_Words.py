# Reverse Words
# Alexander Fraser
# 28 Febuary 2020


"""
Write a program (using functions!) that asks the user
for a long string containing multiple words. Print back
to the user the same string, except with the words in
backwards order.
"""


def collect_input():
    # Get the input from the user.
    input_string = input("Input a string of words: ")
    return input_string


def reverse_order(input_string):
    # Split the string into words (based on spaces)
    # then print out the words in reverse order
    split_string = input_string.split(" ")
    length = len(split_string)

    for i in range(0, length):
        print('{} '.format(split_string[length - i - 1], ))


def main():
    input_string = collect_input()
    reverse_order(input_string)


if __name__ == "__main__":
    main()