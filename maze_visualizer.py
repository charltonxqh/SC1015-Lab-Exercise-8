import matplotlib.pyplot as plt                 # type: ignore
from matplotlib.colors import ListedColormap    # type: ignore
from copy import deepcopy


'''
USAGE EXAMPLE

# Import module
from maze_visualizer import *

# Visualize a blank maze
show_maze(sample_maze)

# Visualize a maze with Pac-Man at (5, 6)
show_maze(sample_maze, (5, 6))

# List storing valid cell coordinates
path = [[6, 6], [6, 5], [6, 4], [5, 4], [5, 3], [5, 2], [5, 1], [4, 1], [3, 1], [2, 1]]

# Visualize the searched maze
show_maze(sample_maze, (5, 6), path)

'''


# Edit this for your own maze design
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


# For testing
sample_maze = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
               [1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
               [1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1],
               [1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
               [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
               [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
               [1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1],
               [1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1],
               [1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1],
               [1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1],
               [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]


    
# Visualises the maze corresponding to grid passed in
def show_maze(grid, start=None, path=None, show_corners=[1, 1, 1, 1], CELL_SIZE=3):
    # Make a copy of the maze
    grid_copy = deepcopy(grid)
    
    color_map = {
        "white": 0,
        "black": 1,
        "yellow": 2,
        "blue": 3,
        "red": 4
    }
    
    # Input validation
    # if not valid_maze(grid):
    #    raise ValueError("Maze is incomplete! Must have all four colors")
    
    # Add path to the maze
    if path:
        grid_copy = add_path(grid_copy, path)
    
    # Add color for four corners
    corners = [(1, 1), (1, len(grid[0]) - 2), (len(grid) - 2, 1), (len(grid) - 2, len(grid[0]) - 2)]
    for i in range(4):
        if show_corners[i]:
            grid_copy[corners[i][0]][corners[i][1]] = color_map["red"]
        
    # Add Pac-Man to the maze
    if start:
        grid_copy[start[0]][start[1]] = color_map["yellow"]
    
    # Define the colors for specific values
    colors = color_map.keys()
    
    # Create a colormap with distinct colors for specific values
    cmap = ListedColormap(colors)

    # Create a figure and axis
    fig, ax = plt.subplots(figsize=(CELL_SIZE, CELL_SIZE))

    # Draw the grid with the custom colormap
    ax.imshow(grid_copy, cmap=cmap, interpolation='nearest')

    # Hide the axes labels
    ax.axis('off')

    # Display the plot
    plt.show()


# Visualises the complete solution found by a search
# Works by displaying each segment of the solution path with a copy of the maze
def show_solution(maze, start, path):
    corners = [(1, 1), (1, len(maze[0]) - 2), (len(maze) - 2, 1), (len(maze) - 2, len(maze[0]) - 2)]
    label = [1, 1, 1, 1]
    for segment in path:
        show_maze(maze, segment[0], segment, label)
        label[corners.index(segment[-1])] = 0


    
# Helper function
# Accepts a list of coordinates of the path squares
# Checks if all path squares are valid before adding them to the maze grid
def add_path(grid, path):
    for coords in range(len(path)):
        x, y = path[coords]
        if grid[x][y] == 1:
            raise ValueError(f"Invalid path! Failed to add ({x}, {y})")
        grid[x][y] = 3
    
    return grid
        

# Determines maze validity 
def valid_maze(grid):
    yellow = red = False
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 2:
                yellow = True
            elif grid[i][j] == 4:
                red = True
    
    return yellow and red
