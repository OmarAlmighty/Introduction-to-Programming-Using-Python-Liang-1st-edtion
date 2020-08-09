# 11.6 (Algebra: multiply two matrices) Write a function to multiply two matrices. The
# header of the function is:
# def multiplyMatrix(a, b)
# To multiply matrix a by matrix b, the number of columns in a must be the same as
# the number of rows in b, and the two matrices must have elements of the same or
# compatible types. Let c be the result of the multiplication. Assume the column size
# of matrix a is n. Each element cij is For
# example, ai1 * b1j + ai2 * b2j + c cij + ain * bnj for two matrices a and b, c is
# where cij = ai1 * b1j + ai2 * b2j + ai3 * b3j. Write a test program that prompts the user to enter two matrices and displays
# their product.
import math


def multiplyMatrix(a, b):
    list = len(m2[0]) * [0]
    result = []
    for i in range(len(m1)):
        result.append([x for x in list])

    for i in range(len(result)):
        for j in range(len(result[0])):
            for k in range(len(m2)):
                result[i][j] += m1[i][k] * m2[k][j]

    return result


l1 = input("Enter matrix 1: ").split()
l2 = input("Enter matrix 2: ").split()

# shape the input into a 3*3 matrix
m1 = []
m2 = []
counter = 0
size = int(math.sqrt(len(l1)))
for i in range(size):
    m1.append([0] * size)
    m2.append([0] * size)
    for j in range(size):
        m1[i][j] = float(l1[counter])
        m2[i][j] = float(l2[counter])
        counter += 1

res = multiplyMatrix(m1, m2)
res = [["%.1f" % x for x in member] for member in res]  # format values
for i in range(size):
    print(m1[i], end=' ')
    if i == 1:
        print(' *', end='')
        print('  ', end='')
    else:
        print('\t', end='')
    print(m2[i], end=' ')
    if i == 1:
        print(' =', end='')
        print('  ', end='')
    else:
        print('\t', end='')
    print(res[i], end=' ')
    print()
