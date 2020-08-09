# 11.2 (Sum the major diagonal in a matrix) Write a function that sums all the numbers
# of the major diagonal in an matrix of integers using the following header:
# def sumMajorDiagonal(m):
# The major diagonal is the diagonal that runs from the top left corner to the bottom
# right corner in the square matrix. Write a test program that reads a matrix and
# displays the sum of all its elements on the major diagonal.

def sumMajorDiagonal(m):
    sum = 0
    for i in range(len(m)):
        sum += m[i][i]

    return sum


m = []
for i in range(4):
    row = input("Enter a 4-by-4 matrix row for row " + str(i + 1) + ": ").split()
    m.append([float(x) for x in row])

print("Sum of the elements in the major diagonal is", sumMajorDiagonal(m))
