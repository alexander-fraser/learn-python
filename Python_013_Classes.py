# Classes
# Alexander Fraser
# 7 March 2020

"""
Refactoring the odd_or_even snippet to use classes.
"""


class odd_or_even():
    # Define the elements of the odd_or_even snippet.

    def collect_integer(self, user_message, lower_limit, upper_limit):
        # This method prompts the user for an integer.
        # It loops until an integer is entered by the user that satisfies the 
        # limits specified.
        while True:
            try:
                user_input = input(user_message + "\n")
                user_value = int(user_input)
            except:
                print("That was not a valid integer. Please try again.")

            else:
                if (user_value >= lower_limit) and (user_value <= upper_limit):
                    break
                print("The integer was not between {} and {}. Please try again."
                    .format(lower_limit, upper_limit))

        return user_value


    def classify_integer(self, input_number):
        # This method classifies the integer as even, odd, or multiple of 4.
        if input_number % 4 == 0:
            print("The number is even and a multiple of 4.")
        elif input_number % 2 == 0:
            print("The number is even.")
        else:
            print("The number is odd.")


def main():
    # Instantiate the class and call its methods.
    game = odd_or_even()
    input_number = game.collect_integer("Pick a random number: ", 0, 1000000)
    game.classify_integer(input_number)
    exit()


if __name__ == "__main__":
    main()