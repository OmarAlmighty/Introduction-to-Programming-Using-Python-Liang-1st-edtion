# 11.1 (Sum elements column by column) Write a function that returns the sum of all the
# elements in a specified column in a matrix using the following header:
# def sumColumn(m, columnIndex):
# Write a test program that reads a 3*4 matrix and displays the sum of each column.

def sumColumn(m, columnIndex):
    sum = 0
    for row in range(len(m)):
        sum += m[row][columnIndex]

    return sum


m = []

for i in range(3):
    row = input("Enter a 3-by-4 matrix row for row " + str(i)+": ").split()
    m.append([float(x) for x in row])

for i in range(4):
    s = sumColumn(m, i)
    print("Sum of the elements for column", i, 'is', s)
