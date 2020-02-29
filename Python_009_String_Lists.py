# String Lists
# Alexander Fraser
# 28 Febuary 2020

"""
Ask the user for a string and print out whether this string
is a palindrome or not. (A palindrome is a string that reads
the same forwards and backwards.)
"""


def collect_input():
    # Get the input from the user.
    input_string = input("Input a string (possibly a palindrome): ")
    return input_string


def test_for_palindrome(input_string):
    # Check whether the string is a palindrome by going through
    # every character in the string.
    palindrome_test = True

    for counter in range(0, len(input_string)):
        if input_string[counter] != input_string[len(input_string) - 1 - counter]:
            palindrome_test = False

    if palindrome_test == True:
        print("That's a palindrome!")
    else:
        print("That's nothing.")


def main():
    input_string = collect_input()
    test_for_palindrome(input_string)


if __name__ == "__main__":
    main()