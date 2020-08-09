# 11.23 (Game: find the flipped cell) Suppose you are given a 6*6 matrix filled
# with 0s and 1s. All rows and all columns have the even number of 1s. Let the
# user flip one cell (i.e., flip from 1 to 0 or from 0 to 1) and write a program to
# find which cell was flipped. Your program should prompt the user to enter a
# 6*6two-dimensional list with 0s and 1s and find the first row r and first
# column c where the even number of 1s property is violated. The flipped cell
# is at (r, c).

mat = []
print("Enter 6*6 matrix: ")
for i in range(0, 6):
    x = input()
    mat.append(x.split())

transpose = [[row[i] for row in mat] for i in range(len(mat))]

for i in range(len(mat)):
    row = mat[i]
    col = transpose[i]
    c1 = row.count('1')
    c2 = col.count('1')

    if c1 % 2 != 0:
        ind = row.index('1')
        if col.count('1')%2 == 0:
            print('The flipped cell at (', i, ',', ind, ')')
            break

    if c2 % 2 != 0:
        ind = col.index('1')
        if row.count('1')%2 == 0:
            print('The flipped cell at (', ind, ',', i, ')')
            break