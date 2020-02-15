# Maze: Kruskal
# Alexander Fraser
# 15 February 2020

# A maze generator using Kruskal's algorithm.

"""
Requirements:
- Numpy
- Matplotlib
- Python_05_Maze_Depth_First

The maze is generated by:
1. Starting with a complete list of walls and each cell in its own set.
2. Randomly select a wall from the list and remove it if the neighbouring cells
   are not part of the same set.
3. Combine the sets containing these two cells.
4. The algorithm stops when all walls have been visited.

The array M is going to hold the array information for each cell.
The first four coordinates tell if walls exist on those sides.
The fifth is NULL and is used to keep the format of the table consistent.
The last coordinate is used to trace how the maze is generated using colour.
M(LEFT, UP, RIGHT, DOWN, NULL, COLOUR)
"""

import random
import numpy as np
from matplotlib import pyplot as plt
from Python_05_Maze_Depth_First import collect_inputs, generate_maze_image, generate_path_image

def main():
    # Default inputs.
    maze_defaults = {}
    maze_defaults['save_maze'] = 'Kruskal Maze 01.png'
    maze_defaults['save_path'] = 'Kruskal Maze 01 - Path.png'
    maze_defaults['num_rows'] = 10
    maze_defaults['num_cols'] = 10
    maze_defaults['colour_on'] = 0
    maze_defaults['colour_incrementer'] = 1
    
    maze_inputs = collect_inputs(maze_defaults)   # Collect inputs from user. 
    
    wall_list = generate_wall_list(maze_inputs)
    M = generate_kruskal_maze(maze_inputs, wall_list)   # Run the maze generator.
    generate_maze_image(maze_inputs, M)   # Visualize the maze.
    generate_path_image(maze_inputs, M)   # Visualize the maze as a path.

def generate_wall_list(maze_inputs):
    num_rows = maze_inputs['num_rows']
    num_cols = maze_inputs['num_cols'] 
    wall_list = []
    
    for r in range(num_rows):
        for c in range(num_cols):
            for wall in range(4):
                if c > 0 and wall == 0:
                    wall_list.append((r, c, wall))
                if r > 0 and wall == 1:
                    wall_list.append((r, c, wall))
                if c < num_cols - 1 and wall == 2:
                    wall_list.append((r, c, wall))
                if r < num_rows - 1 and wall == 3:
                    wall_list.append((r, c, wall))

    return wall_list

def generate_kruskal_maze(maze_inputs, wall_list):
    # Generate the maze using a depth-first algorithm.
    # Set up the maze board.
    
    num_rows = maze_inputs['num_rows']
    num_cols = maze_inputs['num_cols']    
    M = np.zeros((num_rows, num_cols, 6), dtype=np.uint8)
    
    while wall_list:   # The list of all walls.
        wall = random.choice(wall_list)
        wall_list.remove(wall)

    # Currently, this code just goes through all walls and does nothing.
    # Enter the code here that checks the walls and combines the sets.


    # Open the walls at the start and finish.
    M[0, 0, 0] = 1   # Left side of top-left-most cell.
    M[num_rows - 1, num_cols - 1, 2] = 1   # Right side of bottom-right-most cell.

    return M

if __name__ == "__main__":
    main()