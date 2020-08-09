# 11.9 (Game: play a tic-tac-toe game) In a game of tic-tac-toe, two players take turns
# marking an available cell in a 3*3  grid with their respective tokens (either X or
# O). When one player has placed three tokens in a horizontal, vertical, or diagonal
# row on the grid, the game is over and that player has won. A draw (no winner)
# occurs when all the cells in the grid have been filled with tokens and neither player
# has achieved a win. Create a program for playing tic-tac-toe.
# The program prompts two players to alternately enter an X token and an O
# token. Whenever a token is entered, the program redisplays the board on the
# console and determines the status of the game (win, draw, or continue).


def draw_board(p1, p2):
    print("---------------")
    for row in range(len(p1)):
        for col in range(len(p1[0])):
            if p1[row][col] == 1:
                print("| X", end=' |')
            elif p2[row][col] == 1:
                print("| O", end=' |')
            else:
                print("   ", end='  ')
        print("\n---------------")


def is_won(p):
    # check row
    for row in p:
        if row[0] == 1 and row[1] == 1 and row[2] == 1:
            return True

    # check column
    p_transpose = [[row[i] for row in p] for i in range(len(p[0]))]
    for row in p_transpose:
        if row[0] == 1 and row[1] == 1 and row[2] == 1:
            return True

    # check diagonals
    if (p[0][0] == 1 and p[1][1] == 1 and p[2][2] == 1) or \
            (p[0][2] == 1 and p[1][1] == 1 and p[2][0] == 1):
        return True

    return False


def is_correct_move(p1, p2, x, y):
    if p1[x][y] == 0 and p2[x][y] == 0 and 0 <= x <= 2 and 0 <= y <= 2:
        return True
    else:
        return False


def is_a_draw(board):
    for row in board:
        for col in row:
            if col == 0:
                return False
    return True


playAgain = 'y'
while playAgain.lower() == 'y':  # you can make it one board(list) for both players, player x is 1 and player o is 2.
    p1 = [[0, 0, 0],  # X
          [0, 0, 0],
          [0, 0, 0]]
    p2 = [[0, 0, 0],  # O
          [0, 0, 0],
          [0, 0, 0]]

    board = [[0, 0, 0],  # used to detect a draw
             [0, 0, 0],
             [0, 0, 0]]
    draw_board(p1, p2)
    turn = 'x'
    while not is_won(p1) and not is_won(p2) and not is_a_draw(board):
        if turn == 'x':
            x = int(input("Enter a row (0, 1, or 2) for player X: "))
            y = int(input("Enter a column (0, 1, or 2) for player X: "))

            while not is_correct_move(p1, p2, x, y):
                print("Please enter a valid row and column values")
                x = int(input("Enter a row (0, 1, or 2) for player X: "))
                y = int(input("Enter a column (0, 1, or 2) for player X: "))

            p1[x][y] = 1
            board[x][y] = 1
            draw_board(p1, p2)
            if is_won(p1):
                print("Player X is won")
                break
            turn = 'o'

        elif turn == 'o':
            x = int(input("Enter a row (0, 1, or 2) for player O: "))
            y = int(input("Enter a column (0, 1, or 2) for player O: "))

            while not is_correct_move(p1, p2, x, y):
                print("Please enter a valid row and column values")
                x = int(input("Enter a row (0, 1, or 2) for player X: "))
                y = int(input("Enter a column (0, 1, or 2) for player X: "))

            p2[x][y] = 1
            board[x][y] = 1
            draw_board(p1, p2)
            if is_won(p2):
                print("Player O is won")
                break
            turn = 'x'

        if is_a_draw(board):
            print("Draw")

    playAgain = input("Do you want to play again? y or n ")
