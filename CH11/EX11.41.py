# 11.41 (Tkinter: Sudoku solutions) The complete solution for the Sudoku problem is
# given in Supplement III.A. Write a GUI program that enables the user to enter a
# Sudoku puzzle and click the Solve button to display a solution, as shown in
# Figure 11.14.
from tkinter import *


# Obtain a list of free cells from the puzzle
def getFreeCellList(grid):
    freeCellList = []
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                freeCellList.append([i, j])

    return freeCellList


# Display the values in the grid
def printGrid(grid):
    for i in range(9):
        for j in range(9):
            print(grid[i][j], end=" ")
        print()


# Search for a solution
def search(grid):
    freeCellList = getFreeCellList(grid)
    numberOfFreeCells = len(freeCellList)
    if numberOfFreeCells == 0:
        return True  # No free cells

    k = 0  # Start from the first free cell
    while True:
        i = freeCellList[k][0]
        j = freeCellList[k][1]
        if grid[i][j] == 0:
            grid[i][j] = 1  # Fill the free cell with number 1

        if isValid(i, j, grid):
            if k + 1 == numberOfFreeCells:
                # No more free cells
                return True  # A solution is found
            else:
                # Move to the next free cell
                k += 1
        elif grid[i][j] < 9:
            # Fill the free cell with the next possible value
            grid[i][j] = grid[i][j] + 1
        else:
            # grid[i][j] is 9, backtrack
            while grid[i][j] == 9:
                if k == 0:
                    return False  # No possible value
                grid[i][j] = 0  # Reset to free cell
                k -= 1  # Backtrack to the preceding free cell
                i = freeCellList[k][0]
                j = freeCellList[k][1]

            # Fill the free cell with the next possible value,
            # search continues from this free cell at k
            grid[i][j] = grid[i][j] + 1

    return True  # A solution is found


# Check whether grid[i][j] is valid in the grid
def isValid(i, j, grid):
    # Check whether grid[i][j] is valid at the i's row
    for column in range(9):
        if column != j and grid[i][column] == grid[i][j]:
            return False

    # Check whether grid[i][j] is valid at the j's column
    for row in range(9):
        if row != i and grid[row][j] == grid[i][j]:
            return False

    # Check whether grid[i][j] is valid in the 3-by-3 box
    for row in range((i // 3) * 3, (i // 3) * 3 + 3):
        for col in range((j // 3) * 3, (j // 3) * 3 + 3):
            if row != i and col != j and grid[row][col] == grid[i][j]:
                return False

    return True  # The current value at grid[i][j] is valid


# Check whether the fixed cells are valid in the grid
def isValidGrid(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] < 0 or grid[i][j] > 9 or \
                    (grid[i][j] != 0 and not isValid(i, j, grid)):
                return False

    return True  # The fixed cells are valid



class GUI:
    def __init__(self):
        window = Tk()
        self.frame = Frame(window)
        self.frame.pack()
        self.lst = []
        for i in range(9):
            x = []
            for j in range(9):
                x.append(Text(self.frame, width=2, height=1))
                x[j].grid(row=i, column=j)
            self.lst.append(x)
        btn = Button(window, text='Solve', command=self.solve)
        btn2 = Button(window, text='Clear', command=self.clear)
        btn2.pack()
        btn.pack()

        window.mainloop()

    def clear(self):
        self.lst = []
        for i in range(9):
            x = []
            for j in range(9):
                x.append(Text(self.frame, width=2, height=1))
                x[j].grid(row=i, column=j)
            self.lst.append(x)

    def solve(self):
        self.grid = self.readPuzzle()
        if not isValidGrid(self.grid):
            print("Invalid input")
        elif search(self.grid):
            print("The solution is found:")
            printGrid(self.grid)
            self.lst = []
            for i in range(9):
                x = []
                for j in range(9):
                    x.append(Text(self.frame, width=2, height=1))
                    x[j].insert(INSERT, str(self.grid[i][j]))
                    x[j].grid(row=i, column=j)
                self.lst.append(x)
        else:
            print("No solution")

    def readPuzzle(self):
        grid = []
        for i in range(9):
            x = []
            for j in range(9):
                if len(self.lst[i][j].get("1.0", "end-1c")) == 0:
                    x.append(0)
                else:
                    x.append(int(self.lst[i][j].get("1.0", END)))
            grid.append(x)
        return grid

GUI()


