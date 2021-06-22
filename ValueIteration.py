from MazeCreation import maze_structure, gridWorld, printMaze
import numpy as np
from time import sleep

policy = []  # The policy - for every square, which direction to choose
numOfIteration = 0  # The number of the iteration
actions = ['U', 'D', 'R', 'L']  # Up, Down, Right, Left
current_i = 0  # The current location - row
current_j = 1  # The current location - column
last_i = 0  # The last location - row
last_j = 0  # The last location - column


def valueIteration(gamma):  # Running the value iteration algorithm
    global policy, numOfIteration, actions
    policy = np.zeros((21, 21), str)

    # Initializing the policy to be Down or a Wall
    for i in range(21):
        for j in range(21):
            if maze_structure[i][j] != 0:
                policy[i][j] = 'D'
            else:
                policy[i][j] = '♥ '

    gridWorldHasChanged = True  # For entering the first iteration

    while gridWorldHasChanged:  # As long as at least one square has changed
        gridWorldHasChanged = False  # No square has been changed yet
        for i in range(21):
            for j in range(21):
                if maze_structure[i][j] != 0:  # If the square is not a wall
                    values = []
                    availableActions = returnActions(i, j)  # Returning the available actions
                    for act in availableActions:  # For every available action in the square
                        val = returnVal(i, j, act)  # Return the value of the next square by the given action
                        values.append(gridWorld[i][j].reward + gamma * val)  # Calculate the value of the current square

                    if values:  # If values is not empty
                        val = max(values)  # Choose the biggest value
                        if val != gridWorld[i][j].val:  # If the value is not equal to the current value
                            gridWorldHasChanged = True  # The grid world has changed - one of the square updated its
                            # value
                            gridWorld[i][j].val = val  # Update the value

        numOfIteration = numOfIteration + 1  # Increase the number of the current iteration

    for i in range(21):
        for j in range(21):
            if maze_structure[i][j] != 0:  # If the square is not a wall
                availableActions = returnActions(i, j)  # Returning the available actions
                try:
                    maxVal = returnVal(i, j, availableActions[0])  # initializing the maximal value to be one of the
                    # possible values
                except IndexError:
                    pass
                for act in availableActions:  # For every available action in the square
                    if returnVal(i, j, act) >= maxVal:  # If the maximal value is bigger than the current value
                        maxVal = returnVal(i, j, act)  # Update the maximal value
                        policy[i][j] = act  # Update the policy to the act with the current maximal value

            else:
                policy[i][j] == '♥ '  # If the square is a wall
    return policy


def returnVal(i, j, action):  # Returns the value of the next square by the given action
    hasChanged = 0
    try:
        if action == 'R' and maze_structure[i][j + 1]:
            j = j + 1
            hasChanged = 1
    except IndexError:
        pass
    try:
        if action == 'L' and maze_structure[i][j - 1]:
            j = j - 1
            hasChanged = 1
    except IndexError:
        pass
    try:
        if action == 'U' and maze_structure[i - 1][j]:
            i = i - 1
            hasChanged = 1
    except IndexError:
        pass
    try:
        if action == 'D' and maze_structure[i + 1][j]:
            i = i + 1
            hasChanged = 1
    except IndexError:
        pass
    if hasChanged:
        return gridWorld[i][j].val
    else:
        return False


def policyPrint():  # Printing the policy as arrows
    global policy, numOfIteration
    for i in range(21):
        for j in range(21):
            if maze_structure[i][j] != 0:
                if i == 20 and j == 19:
                    print('♫', end=' ')  # If the square is the exit square
                else:
                    if policy[i][j] == 'U':
                        print('↑', end=' ')
                    if policy[i][j] == 'D':
                        print('↓', end=' ')
                    if policy[i][j] == 'R':
                        print('→', end=' ')
                    if policy[i][j] == 'L':
                        print('←', end=' ')
            else:
                print('♥', end=' ')  # If the square is a wall
        print('')
    print(numOfIteration)


def returnActions(i, j):  # Returns the available actions
    global actions
    availableActions = []
    if gridWorld[i][j].U == 1:
        availableActions.append('U')
    if gridWorld[i][j].D == 1:
        availableActions.append('D')
    if gridWorld[i][j].R == 1:
        availableActions.append('R')
    if gridWorld[i][j].L == 1:
        availableActions.append('L')
    return availableActions


def solvingMaze():  # The smiley walking the maze
    global current_i, current_j
    while maze_structure[20][19] != 2:
        move(policy[current_i][current_j])  # Move to the preferred action that is given by the policy
        sleep(0.8)
        screenClear()
        printMaze(1)
    screenClear()
    print('(っ◔◡◔)っ ♥ Congratulations ♥')


def move(action):  # Move the smiley from current location to the next square by the given action
    global current_i, current_j, last_i, last_j
    last_i = current_i
    last_j = current_j
    if action == 'D':
        current_i = current_i + 1
    if action == 'U':
        current_i = current_i - 1
    if action == 'L':
        current_j = current_j - 1
    if action == 'R':
        current_j = current_j + 1

    maze_structure[current_i][current_j] = 2  # The current location of the smiley
    maze_structure[last_i][last_j] = 1  # The last location the smiley was in


def screenClear():  # Clearing the screen - to have an animation/to make the run look better
    print('\n' * 80)  # prints 80 line breaks
