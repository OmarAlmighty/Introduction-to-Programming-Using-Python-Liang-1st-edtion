# 15.27 (All eight queens) Modify Listing 15.10, EightQueens.py, to find all the possible
# solutions to the Eight Queens problem.
# Function to check if two queens threaten each other or not

'''
THIS SOLUTION IS A CONSOLE VERSION CLONED FROM https://www.techiedelight.com/print-possible-solutions-n-queens-problem/
MY GUI VERSION WILL BE CREATED LATER...
'''


def isValid(mat, r, c):
    # return false if two queens share the same column
    for i in range(r):
        if mat[i][c] == 'Q':
            return False

    # return false if two queens share the same `` diagonal
    (i, j) = (r, c)
    while i >= 0 and j >= 0:
        if mat[i][j] == 'Q':
            return False
        i = i - 1
        j = j - 1

    # return false if two queens share the same `/` diagonal
    (i, j) = (r, c)
    while i >= 0 and j < N:
        if mat[i][j] == 'Q':
            return False
        i = i - 1
        j = j + 1

    return True


def printSolution(mat):
    for i in range(N):
        print(mat[i])
    print()


def searchAll(mat, r):
    # if `N` queens are placed successfully, print the solution
    if r == N:
        printSolution(mat)
        return

    # place queen at every square in the current row `r`
    # and recur for each valid movement
    for i in range(N):

        # if no two queens threaten each other
        if isValid(mat, r, i):
            # place queen on the current square
            mat[r][i] = 'Q'

            # recur for the next row
            searchAll(mat, r + 1)

            # backtrack and remove the queen from the current square
            mat[r][i] = '–'


if __name__ == '__main__':
    # `N × N` chessboard
    N = 8

    # `mat[][]` keeps track of the position of queens in
    # the current configuration
    mat = [['–' for x in range(N)] for y in range(N)]

    searchAll(mat, 0)
