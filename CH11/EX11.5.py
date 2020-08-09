# 11.5 (Algebra: add two matrices) Write a function to add two matrices. The header of
# the function is:
# def addMatrix(a, b):
# In order to be added, the two matrices must have the same dimensions and the
# same or compatible types of elements. Let c be the resulting matrix. Each element
# cij is aij + bij.

l1 = input("Enter matrix 1: ").split()
l2 = input("Enter matrix 2: ").split()

# shape the input into a 3*3 matrix
m1 = []
m2 = []
counter = 0
for i in range(3):
    m1.append([0] * 3)
    m2.append([0] * 3)
    for j in range(3):
        m1[i][j] = float(l1[counter])
        m2[i][j] = float(l2[counter])
        counter += 1

# add the matrices and store result in sum
sum = []
for i in range(3):
    sum.append([0] * 3)
    for j in range(3):
        sum[i][j] = m1[i][j] + m2[i][j]

for i in range(3):
    print(m1[i], end=' ')
    if i == 1:
        print(' +', end='')
        print('  ', end='')
    else:
        print('\t', end='')
    print(m2[i], end=' ')
    if i == 1:
        print(' =', end='')
        print('  ', end='')
    else:
        print('\t', end='')
    print(sum[i], end=' ')
    print()
