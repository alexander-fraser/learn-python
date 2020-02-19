# Even or Odd
# Alexander Fraser
# 16 Febuary 2020

"""
Ask the user for a number. Depending on whether the number is even
or odd, print out an appropriate message to the user.
"""

def main():
    inputNumber = input("Pick a random number: ")

    try:
        inputNumber = int(inputNumber)
    except:
        print("That's not a number! Try again.")
        exit()

    if inputNumber % 4 == 0:
        print("The number is a multiple of 4.")
    elif inputNumber % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")

def collect_integer(user_message, lower_limit, upper_limit):
    # This function prompts the user for an integer.
    # It loops until an integer is entered by the user that satisfies the limits.
    while True:
        try:
            user_input = input(user_message + "\n")
            user_value = int(user_input)
        except:
            print("That was not a valid integer. Please try again.")

        else:
            if user_value >= lower_limit:
                break
            elif user_value <= upper_limit:
                break
            print("The integer was not between {} and {}. Please try again.".format(lower_limit, upper_limit))

    return user_value

if __name__ == "__main__":
    main()