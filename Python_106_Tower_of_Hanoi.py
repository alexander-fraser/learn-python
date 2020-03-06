# Tower of Hanoi Solver
# Alexander Fraser
# 5 March 2020

# Solves a Tower of Hanoi puzzle using a recursive algorithm.

"""
Tower of Hanoi puzzle instructions:
- There are three sticks: A, B, and C.
- There are a specified number of disks arranged in ascending size.
- The disks all start on A. The goal is to get them all to C.
- Disks can only stack in the order they started (i.e. small to large).

This Tower of Hanoi solver uses a recursive algorithm. That is,
there is a function that calls itself to solve a simpler-and-simpler
version of the puzzle, eventually getting down to the base case of 0 disks
(where it does nothing).

The solver works by:
1. Moving all disks above the specified disk to a placeholder.
2. Then moving the specified disk to the "to" place.
3. Finally, moving the disks back on top of the specified disk.
"""


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
            if (user_value >= lower_limit) and (user_value <= upper_limit):
                break
            print("The integer was not between {} and {}. Please try again.".format(lower_limit, upper_limit))

    return user_value


def print_move(disk, move_from, move_to):
    # Prints the instructions for solving the puzzle.
    print("Move disk {} from {} to {}.".format(disk, move_from, move_to))


def hanoi_move(disk, move_from, move_via, move_to):
    # Recursive loop that solves the puzzle.
    # Moves all disks above the specified disk to a placeholder.
    # Then moves the specified disk to the "to" place.
    # Finally moves the disks above it back on top of the specified disk.
    if disk != 0:
        hanoi_move(disk-1, move_from, move_to, move_via)
        print_move(disk, move_from, move_to)
        hanoi_move(disk-1, move_via, move_from, move_to)


def main():
    # Prompts the user to specify the puzzle height.
    # Then calls the solver to print the instructions.
    print("Welcome to the Tower of Hanoi solver.")
    hanoi_height = collect_integer("How many disks are in the tower?", 1, 100)
    hanoi_move(hanoi_height, "A", "B", "C")


if __name__ == "__main__":
    main()