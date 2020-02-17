# Sudoku Solver
# Alexander Fraser
# 16 February 2020

# Solves Sudoku puzzles using a recursive algorithm.

def main():
    unsolved_puzzle = import_sudoku()
    solved_puzzle = sudoku_solver(unsolved_puzzle)

def import_sudoku():
    # Asks the user to enter the sudoku puzzle as a series of 81 integers.
    # 0s take the place of the blank cells.
    # The function outputs the puzzle as a list.

    #sudoku_string = input("Pass the sudoku values from top-left to bottom-right, with 0s for blank cells:\n")
    sudoku_string = "123456789223456789323456789423456789523456789623456789723456789823456789923456789"

    sudoku_list = []

    for i in range(9):
        sudoku_row = []

        for j in range(9):
            sudoku_row.append( sudoku_string[(9*i + j)] )
        sudoku_list.append(sudoku_row)

    #print(sudoku_string)
    #print(sudoku_list)

    return sudoku_list

def sudoku_solver(unsolved_puzzle):
    

if __name__ == "__main__":
    main()
