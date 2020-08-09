# 11.13 (Locate the largest element) Write the following function that returns the location
# of the largest element in a two-dimensional list:
# def locateLargest(a):
# The return value is a one-dimensional list that contains two elements. These
# two elements indicate the row and column indexes of the largest element in the
# two-dimensional list. Write a test program that prompts the user to enter a two dimensional
# list and displays the location of the largest element in the list.

def locateLargest(a):
    max_indx_row = 0
    max_indx_col = 0
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] > a[max_indx_row][max_indx_col]:
                max_indx_row = i
                max_indx_col = j

    return max_indx_row, max_indx_col


rows = int(input("Enter the number of rows in the list: "))
matrix = []

for i in range(rows):
    r = input("Enter a row: ").split()
    r = [float(x) for x in r]
    matrix.append(r)

row, col = locateLargest(matrix)
print("The location of the largest element is at (" + str(row) + "," + str(col) + ")")
