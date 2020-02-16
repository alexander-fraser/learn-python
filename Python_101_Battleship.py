# Battleship
# Alexander Fraser
# 9 February 2020

# A simple 1-player game of battleship.

"""
Overview:
1. Create game board
2. Computer randomly places ships
3. Draw board
4. Get input from player
5. Determine hits/misses and record them
6. End game
"""

import random

def generate_board(rows, columns):
    # Creates the game board, which is a 2D list.

    game_board = []

    for _ in range(0, rows):
        game_row = []

        for _ in range(0, columns):
            game_cell = 0
            game_row.append(game_cell)
    
        game_board.append(game_row)

    return game_board

def draw_board(game_board):
    # Draws the game board to the screen. SHows hits and misses, but not hidden ships.
    
    for row in game_board:
        print("|", end="")

        for cell in row:

            if cell == 0:        # Empty
                value = "-"
            elif cell == 1:      # Ship
                value = "-"
            elif cell == 2:      # Hit 
                value = "W"
            elif cell == 3:      # Miss
                value = "O"
            else:
                value = "?"

            print(value, end="")
            print("|", end="")

        print("")

def place_ships(game_board, ship_number, ship_length):
    # Places the ships on the board randomly.
    
    for i in range(0, ship_number):
        while True:
            random_row = random.randint(0, len(game_board) - 1)
            random_column = random.randint(0, len(game_board[0]) - 1)
            random_direction = random.randint(0,3)

            if random_direction == 0:
                if random_row - ship_length >= 0:
                    break
            elif random_direction == 1:
                if random_column + ship_length <= len(game_board[0]):
                    break
            elif random_direction == 2:
                if random_row + ship_length <= len(game_board):
                    break
            elif random_direction == 3:
                if random_column - ship_length >= 0:
                    break

        # Now that we have the random row, column, and direction, place the ship.
        game_board[random_row][random_column] = 1

        for i in range(0, ship_length):
            if random_direction == 0:
                game_board[random_row-i][random_column] = 1
            elif random_direction == 1:
                game_board[random_row][random_column+i] = 1
            elif random_direction == 2:
                game_board[random_row+i][random_column] = 1
            elif random_direction == 3:
                game_board[random_row][random_column-i] = 1

    return game_board

def get_player_move(game_board):
    # This function prompts the user for an integer.
    row_limit = len(game_board)
    column_limit = len(game_board[0])
        
    while True:
        try:
            input_row = input("Where should we fire, Captain! (row)?")
            int_row = int(input_row)
        except:
            print("That was not a valid integer. Please try again.")
        else:
            if int_row < 1:
                print("The integer entered was less than 1. Please try again.")
            elif int_row > row_limit:
                print("The integer entered was greater than {}. Please try again.".format(row_limit))
            else:
                break

    while True:
        try:
            input_column = input("Where should we fire, Captain! (column)?")
            int_column = int(input_column)
        except:
            print("That was not a valid integer. Please try again.")
        else:
            if int_column < 1:
                print("The integer entered was less than 1. Please try again.")
            elif int_column > column_limit:
                print("The integer entered was greater than {}. Please try again.".format(column_limit))
            else:
                break

    return int_row - 1, int_column - 1

def compute_move(game_board, input_row, intput_column):
    # Makes changes to the game board for player moves.

    before = game_board[input_row][intput_column]
    after = 0

    if (before == 1) or (before == 2):      # Ship or hit
        after = 2                           # Hit
    else:                                   # Empty or miss
        after = 3                           # Miss

    game_board[input_row][intput_column] = after

    return game_board

def check_score(game_board, score):
    # Scores the game and checks end condition.

    end_game = False
    count = [0,0,0,0]               # Count number of different spaces.

    for row in game_board:
        for cell in row:
            count[cell] += 1

    for i in range(0,4):
        score[i] = count[i]

    score[4] += 1                   # Number of turns. 

    print("You have {} hits, {} misses, and there are {} ship spaces left".format(score[2], score[3], score[1]))

    if score[1] == 0:               # If all ship spaces are hit.
        end_game = True

    return score, end_game

def play_game(game_board):
    # Runs the gameplay loop.

    score = [0,0,0,0,0]

    while True:
        draw_board(game_board)
        input_row, intput_column = get_player_move(game_board)
        game_board = compute_move(game_board, input_row, intput_column)
        score, end_game = check_score(game_board, score)

        if end_game == True:
            print("You win!")
            break

def main():
    # Runs the game.
    game_board = generate_board(5, 5)               # Arguments are number of rows and columns.
    game_board = place_ships(game_board, 3, 3)      # Arguments are number and length of ships.
    play_game(game_board)

if __name__ == "__main__":
    main()