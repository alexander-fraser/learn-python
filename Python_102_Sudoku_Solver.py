# Sudoku Solver
# Alexander Fraser
# 22 February 2020

# Solves Sudoku puzzles using a depth-first search recursive algorithm.

"""
Requirements:
- Numpy

This Sudoku solver uses a depth-first search algorithm implemented
using recursion. That is, the solver will go down each possible path
as far as it can until it gets stuck, at which point it will back up
until it finds a new path it can take. The solver stops when it finds
a path that solves the entire puzzle. 

Implementing this method using recursion means that we don't need to 
keep track of which cells were empty/filled at the start (i.e. to keep 
track of the input puzzle), since backtracking will only occur along  
the path that we took (i.e. the empty cells).

The solver works by:
1. Moving to the next empty cell (denoted by a '0').
2. Looking for an integer (1-9) that works for that cell.
3. If a valid integer is found, it moves on to the next cell.
4. If a valid integer is not found, it moves back to the last cell.
"""

import numpy as np

def main():
    # Runs the functions to import and solve the Sudoku puzzle.
    unsolved_puzzle = import_sudoku()
    sudoku_solver(unsolved_puzzle)

def import_sudoku():
    # Asks the user to enter the sudoku puzzle as a series of 81 integers.
    # 0s take the place of the blank cells.
    # The function outputs the puzzle as a list of lists (for rows and columns).

    while True:
        # This loops until a valid puzzle is entered by the user.
        try:
            sudoku_string = input("Pass the sudoku values from top-left to bottom-right,"
                                  "with 0s for blank cells:\n Enter 'y' to use default Sudoku puzzle.\n")
            if sudoku_string == 'y':
                sudoku_string = ("3008010022010306040002040008090001060600000507"
                                "02000409000509000904080705600107003")
            int(sudoku_string)
        
        except:
            print("That was not a valid Sudoku puzzle. Please try again.\n")

        else:
            if len(sudoku_string) == 81:
                break
            print("Too few or too many cells. Please try again.\n")      

    # Converts the string into a list of lists.
    sudoku_list = []
    for i in range(9):
        sudoku_row = []
        for j in range(9):
            sudoku_row.append( int(sudoku_string[(9*i + j)] ))
        sudoku_list.append(sudoku_row)

    print("Unsolved puzzle:\n", np.asarray(sudoku_list), "\n")

    return sudoku_list

def check_valid(puzzle, row, col, value):
    # Checks whether the given value is a valid option for the specified cell.
    # Check rows.
    for i in range(9):
        if puzzle[row][i] == value:
            return False

    # Check columns.
    for i in range(9):
        if puzzle[i][col] == value:
            return False

    # Check square.
    square_row = int(row / 3)
    square_col = int(col / 3)

    for i in range(3):
        for j in range(3):
            if puzzle[square_row * 3 + i][square_col * 3 + j] == value:
                return False

    return True

def sudoku_solver(puzzle):
    # Goes through each cell in the puzzle.
    for row in range(9):
        for col in range(9):
            
            # Checks if the cell is empty.
            if puzzle[row][col] == 0:
                
                # Tries every possible value (1-9).
                for value in range(1, 10): 
                    if check_valid(puzzle, row, col, value):    
                        puzzle[row][col] = value  # Updates the puzzle with the valid value.
                        puzzle = sudoku_solver(puzzle)  # The recursive element, to move onto next cell.
                        puzzle[row][col] = 0  # If the function gets to here, it is backtracking and you must try the next value.

                return puzzle  # If no value works, then backtrack one step.
    
    # If the function gets to here, it has solved every cell in the puzzle. 
    print("Solved puzzle:\n", np.asarray(puzzle), "\n")
    return puzzle

if __name__ == "__main__":
    main()