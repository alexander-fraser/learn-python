# Sudoku Solver
# Alexander Fraser
# 16 February 2020

# Solves Sudoku puzzles using a recursive algorithm.

import numpy as np

def main():
    unsolved_puzzle = import_sudoku()
    print(np.asarray(unsolved_puzzle))
    
    global puzzle
    puzzle = unsolved_puzzle
    
    solved_puzzle = sudoku_solver()
    print(np.asarray(solved_puzzle))

def import_sudoku():
    # Asks the user to enter the sudoku puzzle as a series of 81 integers.
    # 0s take the place of the blank cells.
    # The function outputs the puzzle as a list.

    #sudoku_string = input("Pass the sudoku values from top-left to bottom-right, with 0s for blank cells:\n")
    sudoku_string = "530070000600195000098000060800060003400803001700020006060000280000419005000080079"

    sudoku_list = []

    for i in range(9):
        sudoku_row = []

        for j in range(9):
            sudoku_row.append( int(sudoku_string[(9*i + j)] ))
        sudoku_list.append(sudoku_row)

    #print(sudoku_string)
    #print(sudoku_list)

    return sudoku_list

def check_valid(puzzle, row, col, value):
    # Checks whether the given value is a valid option for the specified cell,
    # given the rules of Sudoku.

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

def sudoku_solver():
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == 0:
                
                for value in range(9):
                    if check_valid(puzzle, row, col, value):
                        puzzle[row][col] = value
                        print(row, col, value)
                        sudoku_solver()
                        puzzle[row][col] = 0
                return
    
    return puzzle

if __name__ == "__main__":
    main()
