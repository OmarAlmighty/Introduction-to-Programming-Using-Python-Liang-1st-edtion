# 11.20 (Game: Connect Four) Connect Four is a two-player board game in which the
# players alternately drop colored disks into a seven-column, six-row vertically
# suspended grid, as shown at cs.armstrong.edu/liang/ConnectFour/ConnectFour.html.
# The objective of the game is to connect four same-colored disks in a row, column,
# or diagonal before your opponent does. The program prompts two players
# to drop a red or yellow disk alternately. Whenever a disk is dropped, the program
# redisplays the board on the console and determines the status of the game
# (win, draw, or continue).

import sys


def dropADisc(player, board):
    done = False

    while not done:
        print("Drop a", "red" if player == 'R' else "yellow", end=" disk at column (0-6): ")
        column = eval(input())

        if placeADisk(board, column, player):
            done = True
        else:
            print("This column is full. Try a different column")


def placeADisk(board, column, player):
    for i in range(len(board)):
        if board[i][column] == '\u0000':
            board[i][column] = player
            return True  # successful

    return False  # full, unsuccessful


def displayBoard(board):
    for i in range(len(board) - 1, -1, -1):
        print("|", end="")
        for j in range(len(board[i])):
            print(board[i][j] + "|" if board[i][j] != '\u0000' else " |", end="")
        print()

    print("----------------------")


def isWon(board):
    return isConsecutiveFour(board)


def isDraw(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == '\u0000': return False

    return True  # All cells are now occupied


def isConsecutiveFour(values):
    numberOfRows = len(values)
    numberOfColumns = len(values[0])

    # Check rows
    for i in range(numberOfRows):
        if isConsecutiveFourInList(values[i]):
            return True

    # Check columns
    for j in range(numberOfColumns):
        column = numberOfRows * [' ']

        # Get a column into an array
        for i in range(numberOfRows):
            column[i] = values[i][j]

        if isConsecutiveFourInList(column):
            return True

    # Check major diagonal (lower part)
    for i in range(numberOfRows - 3):
        numberOfElementsInDiagonal = min(numberOfRows - i, numberOfColumns)
        diagonal = numberOfElementsInDiagonal * [' ']
        for k in range(numberOfElementsInDiagonal):
            diagonal[k] = values[k + i][k]

        if isConsecutiveFourInList(diagonal):
            return True

    # Check major diagonal (upper part)
    for j in range(1, numberOfColumns - 3):
        numberOfElementsInDiagonal = min(numberOfColumns - j, numberOfRows)
        diagonal = numberOfElementsInDiagonal * [' ']
        for k in range(numberOfElementsInDiagonal):
            diagonal[k] = values[k][k + j]

        if isConsecutiveFourInList(diagonal):
            return True

    # Check sub-diagonal (left part)
    for j in range(3, numberOfColumns):
        numberOfElementsInDiagonal = min(j + 1, numberOfRows)
        diagonal = numberOfElementsInDiagonal * [' ']

        for k in range(numberOfElementsInDiagonal):
            diagonal[k] = values[k][j - k]

        if isConsecutiveFourInList(diagonal):
            return True

    # Check sub-diagonal (right part)
    for i in range(1, numberOfRows - 3):
        numberOfElementsInDiagonal = min(numberOfRows - i, numberOfColumns)
        diagonal = numberOfElementsInDiagonal * [' ']

        for k in range(numberOfElementsInDiagonal):
            diagonal[k] = values[k + i][numberOfColumns - k - 1]

        if isConsecutiveFourInList(diagonal):
            return True

    return False


def isConsecutiveFourInList(values):
    for i in range(len(values) - 3):
        isEqual = True
        for j in range(i, i + 3):
            if values[j] == '\u0000' or values[j] != values[j + 1]:
                isEqual = False
                break

        if isEqual: return True

    return False


board = []
for i in range(6):
    board.append(8 * ["\u0000"])

displayBoard(board)

while True:
    # Prompt the first player
    dropADisc('R', board)

    displayBoard(board)
    if isWon(board):
        print("The red player won")
        sys.exit()
    elif isDraw(board):
        print("No winner")
        sys.exit()

    # Prompt the second player
    dropADisc('Y', board)
    displayBoard(board)

    if isWon(board):
        print("The yellow player won")
        sys.exit()
    elif isDraw(board):
        print("No winner")
        sys.exit()
