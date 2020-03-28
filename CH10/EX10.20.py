# 10.20 (Game: multiple Eight Queens solutions) Exercise 10.18 has you find one
# solution for the Eight Queens puzzle. Write a program to count all possible
# solutions for the Eight Queens problem and display all the solutions.
def main():
    count = 0

    # Queen positions
    queens = 8 * [-1]  # queens are placed at (i, queens[i])
    # -1 indicates that no queen is currently placed in the ith row

    queens[0] = 0  # Initially, place a queen at (0, 0) in the 0th row

    # k - 1 indicates the number of queens placed so far
    # We are looking for a position in the kth row to place a queen
    k = 1
    while k >= 0:
        # Find a position to place a queen in the kth row
        j = findPosition(k, queens)
        if j < 0:
            queens[k] = -1
            k -= 1  # back track to the previous row
        else:
            queens[k] = j
            if k == 7:
                count += 1  # One more solution found
                print("Solution" + str(count) + ":")
                printResult(queens)
            else:
                k += 1

    print("How many solutions?", count)


def findPosition(k, queens):
    start = 0 if queens[k] == -1 else (queens[k] + 1)

    for j in range(start, 8):
        if isValid(k, j, queens):
            return j  # (k, j) is the place to put the queen now

    return -1


# Return true if you a queen can be placed at (k, j)
def isValid(k, j, queens):
    # See if (k, j) is a possible position
    # Check jth column
    for i in range(k):
        if queens[i] == j:
            return False

    # Check major diagonal
    row = k - 1
    column = j - 1
    while row >= 0 and column >= 0:
        if queens[row] == column:
            return False

        row -= 1
        column -= 1

    # Check minor diagonal
    row = k - 1
    column = j + 1
    while row >= 0 and column <= 7:
        if queens[row] == column:
            return False

        row -= 1
        column -= 1

    return True


# Print a two-dimensional board to display the queens
def printResult(queens):
    # Display the output
    for i in range(8):
        for j in range(queens[i]):
            print("| ", end="")
        print("|Q|", end="")

        for j in range(queens[i] + 1, 8):
            print(" |", end="")
        print()


main()
