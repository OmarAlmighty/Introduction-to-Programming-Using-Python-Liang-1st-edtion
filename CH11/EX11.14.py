# 11.14 (Explore matrix) Write a program that prompts the user to enter the length of a
# square matrix, randomly fills in 0s and 1s into the matrix, prints the matrix, and
# finds the rows, columns, and major diagonal with all 0s or all 1s.
import random


def print_matrix(mat):
    for i in mat:
        for j in i:
            print(j, end='')
        print()


def find_in_row(mat, x):
    indx = []
    for row in mat:
        if sum(row) == x * len(row):
            indx.append(mat.index(row))
    if len(indx) == 0:
        return None

    return indx


def find_in_diagonal(mat, x):
    indx = []
    for i in range(len(mat)):
        if mat[i][i] != x:
            return None

    for i in range(len(mat)-1, 0, -1):
        if mat[i][i] != x:
            return None

    return True


size = int(input("Enter the size for the matrix: "))
mat = []
for r in range(size):
    mat.append([0] * size)
    for c in range(size):
        mat[r][c] = random.randint(0, 1)

print_matrix(mat)

a = find_in_row(mat, 0)
b = find_in_row(mat, 1)
if a is None and b is None:
    print("No same numbers in a row")
else:
    if a is not None:
        print("All 0s on row ", end='')
        for i in a:
            print(i, end=' ')
    print()

    if b is not None:
        print("All 1s on row ", end='')
        for i in b:
            print(i, end=' ')

print()

# transpose matrix
mat_traspose = [[row[i] for row in mat] for i in range(len(mat[0]))]

a = find_in_row(mat_traspose, 0)
b = find_in_row(mat_traspose, 1)
if a is None and b is None:
    print("No same numbers in a column")
else:
    if a is not None:
        print("All 0s on column ", end='')
        for i in a:
            print(i, end=' ')
    print()

    if b is not None:
        print("All 1s on column ", end='')
        for i in b:
            print(i, end=' ')

print()

c = find_in_diagonal(mat, 0)
d = find_in_diagonal(mat, 1)
if c is None and d is None:
    print("No same numbers in the major diagonal")
else:
    if c is not None:
        print("All 0s on the diagonal")

    elif d is not None:
        print("All 1s on the diagonal")

print()
