# Imports
import numpy as np
from GridSquare import GridSquare

#######################
# Globals
maze_structure = []
gridWorld = np.zeros((21, 21), GridSquare)
lastStep = 'O'
nextStep = 'O'
iteration = 1


#######################
# Functions

def mazeStructure():  # Creating the structure of the maze
    global maze_structure  # 0 - wall, 1 - path, 2 - the smiley
    #                      0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18  19 20
    maze_structure.append([0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])  # 0
    maze_structure.append([0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0])  # 1
    maze_structure.append([0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0])  # 2
    maze_structure.append([0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])  # 3
    maze_structure.append([0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])  # 4
    maze_structure.append([0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0])  # 5
    maze_structure.append([0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0])  # 6
    maze_structure.append([0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0])  # 7
    maze_structure.append([0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0])  # 8
    maze_structure.append([0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0])  # 9
    maze_structure.append([0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0])  # 10
    maze_structure.append([0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0])  # 11
    maze_structure.append([0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0])  # 12
    maze_structure.append([0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0])  # 13
    maze_structure.append([0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0])  # 14
    maze_structure.append([0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0])  # 15
    maze_structure.append([0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0])  # 16
    maze_structure.append([0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0])  # 17
    maze_structure.append([0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0])  # 18
    maze_structure.append([0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0])  # 19
    maze_structure.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0])  # 20


def printMaze(isGraphic):  # Printing the maze graphically or as integers
    global maze_structure
    if isGraphic:
        for i in range(21):
            for j in range(21):
                if maze_structure[i][j] == 0:  # For wall
                    print("♥ ", end='')
                elif maze_structure[i][j] == 1:  # For path
                    print("  ", end='')
                elif maze_structure[i][j] == 2:  # For the smiley
                    print("☺ ", end='')
            print("")
    else:
        for i in range(21):
            print(maze_structure[i])  # Print the matrix as is


def movementOptions():  # Creating the grid world
    global gridWorld, maze_structure

    # Checking what are the options for every square in the grid world
    for i in range(0, 21):
        for j in range(0, 21):
            right = left = up = down = 0
            try:
                if maze_structure[i][j + 1]:
                    right = 1
            except IndexError:
                pass
            try:
                if maze_structure[i][j - 1]:
                    left = 1
            except IndexError:
                pass
            try:
                if maze_structure[i - 1][j]:
                    up = 1
            except IndexError:
                pass
            try:
                if maze_structure[i + 1][j]:
                    down = 1
            except IndexError:
                pass
            if maze_structure != 0:
                gridWorld[i][j] = GridSquare(up, down, right, left)  # Creating the grid world - creating the
                # attribute of the squares

    gridWorld[20][19].reward = 11  # Defining the reward for the exit square
