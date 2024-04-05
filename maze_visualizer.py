import numpy as np
import matplotlib.pyplot as plt                 # type: ignore
from matplotlib.colors import ListedColormap    # type: ignore


# USAGE EXAMPLE
# 
# # Import module
# from maze_visualizer import *

# # Visualize a blank maze
# show_maze(sample_maze)

# # List storing valid path squares 
# path = [[6, 6], [6, 5], [6, 4], [5, 4], [5, 3], [5, 2], [5, 1], [4, 1], [3, 1], [2, 1]]

# # Visualize the searched maze
# add_path(sample_maze, path)
# show_maze(sample_maze)
# 


# Define mapping of colors
color_map = {
    "white": 0,
    "black": 1,
    "yellow": 2,
    "blue": 3,
    "red": 4
}


# Edit these for your own maze design
blank_maze = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
              [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
              [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
              [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
              [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
              [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
              [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
              [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
              [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
              [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
              [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
              [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]


sample_maze = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
               [1, 4, 1, 0, 0, 0, 0, 1, 0, 0, 4, 1],
               [1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1],
               [1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
               [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
               [1, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 1],
               [1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1],
               [1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1],
               [1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1],
               [1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1],
               [1, 4, 1, 0, 0, 0, 0, 0, 0, 0, 4, 1],
               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]


    
# Visualises the maze corresponding to grid passed in
# Rejects incomplete mazes, i.e. mazes without all four colors
def show_maze(grid):
    # Input validation
    if not valid_maze(grid):
        raise ValueError("Maze is incomplete! Must have all four colors")
    
    # Define the colors for specific values
    colors = color_map.keys()
    
    # Create a colormap with distinct colors for specific values
    cmap = ListedColormap(colors)

    # Create a figure and axis
    fig, ax = plt.subplots()

    # Draw the grid with the custom colormap
    ax.imshow(grid, cmap=cmap, interpolation='nearest')

    # Hide the axes labels
    ax.axis('off')

    # Display the plot
    plt.show()

    
# Accepts a list of coordinates of the path squares
# Checks if all path squares are valid before adding them to the maze grid
def add_path(grid, path):
    for coords in range(len(path)):
        x, y = path[coords]
        if grid[x][y] == 1:
            raise ValueError(f"Invalid path! Failed to add ({x}, {y})")
        grid[x][y] = 3
    
    return grid
        

# Helper function to determine maze validity
def valid_maze(grid):
    yellow = red = False
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 2:
                yellow = True
            elif grid[i][j] == 4:
                red = True
    
    return yellow and red