import MazeCreation
from MazeCreation import mazeStructure, printMaze, movementOptions
from ValueIteration import valueIteration, policyPrint, solvingMaze
from time import sleep


# Main

def main():
    mazeStructure()  # Creating the structure of the maze
    printMaze(1)  # Printing the maze graphically
    sleep(2)  # Waiting before next printing
    print('~~~~~~~~~~~~~~~')
    # printMaze(0)  # Printing the maze as integers
    sleep(2)  # Waiting before next printing
    print('~~~~~~~~~~~~~~~')
    movementOptions()  # Creating the grid world
    valueIteration(0.71)  # Running the value iteration algorithm
    # policy = valueIteration(0.71)  # Running the value iteration algorithm
    # print(policy)  # Printing the policy as letters
    sleep(2)  # Waiting before next printing
    print('~~~~~~~~~~~~~~~')
    policyPrint()  # Printing the policy as arrows
    sleep(2)  # Waiting before next printing
    print('~~~~~~~~~~~~~~~')
    solvingMaze()  # The smiley walking the maze


if __name__ == '__main__':
    main()

