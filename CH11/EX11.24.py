# 11.24 (Check Sudoku solution) Listing 11.7 checks whether a solution is valid by checking
# whether every number is valid in the grid. Rewrite the program by checking
# whether every row, column, and box has the numbers 1 to 9.

def main():
    # Read a Sudoku solution
    grid = readASolution()

    if isValidGrid(grid):
        print("Valid solution")
    else:
        print("Invalid solution")


# Read a Sudoku solution from the console
def readASolution():
    print("Enter a Sudoku puzzle solution:")
    grid = []
    for i in range(9):
        line = input().strip().split()
        grid.append([eval(x) for x in line])

    return grid


# Check whether the fixed cells are valid in the grid
def isValidGrid(grid):
    # Check whether each row has numbers 1 to 9
    for i in range(9):
        if not is1To9(grid[i]):  # If grid[i] does not contain 1 to 9
            return False

    # Check whether each column has numbers 1 to 9
    for j in range(9):
        # Obtain a column in the one-dimensional array
        column = []
        for i in range(9):
            column.append(grid[i][j])

        if not is1To9(column):  # If column does not contain 1 to 9
            return False

    # Check whether each 3 by 3 box has numbers 1 to 9
    for i in range(3):
        for j in range(3):
            # The starting element in a small 3 by 3 box
            k = 0
            list = 9 * [0]  # Get all number in the box to list
            for row in range(i * 3, i * 3 + 3):
                for column in range(j * 3, j * 3 + 3):
                    list[k] = grid[row][column]
                    k += 1

            if not is1To9(list):  # If list does not contain 1 to 9
                return False

    return True  # The fixed cells are valid


# Check whether the one-dimensional array contains 1 to 9
def is1To9(list):
    # Make a copy of the array
    temp = [x for x in list]

    # Sort the array
    temp.sort()

    # Check if list contains 1, 2, 3, ..., 9
    return temp == [1, 2, 3, 4, 5, 6, 7, 8, 9]


main()
