# 12.2 (The Location class) Design a class named Location for locating a maximal
# value and its location in a two-dimensional list. The class contains the public data
# fields row, column, and maxValue that store the maximal value and its indexes in
# a two-dimensional list, with row and column as int types and maxValue as a
# float type.
# Write the following method that returns the location of the largest element in a
# two-dimensional list.
# def Location locateLargest(a):
# The return value is an instance of Location. Write a test program that prompts
# the user to enter a two-dimensional list and displays the location of the largest element
# in the list.

class Location:
    def __init__(self):
        self.row = -1
        self.col = -1
        self.maxValue = -1


def getLocation(lst):
    loc = Location()

    for i in range(len(lst)):
        for j in range(len(lst[0])):
            if lst[i][j] > loc.maxValue:
                loc.maxValue = lst[i][j]
                loc.row = i
                loc.col = j

    return loc


def main():
    rows, cols = eval(input("Enter the number of rows and columns in the list: "))
    lst = []

    for i in range(rows):
        row = input("Enter row " + str(i) + ": ").split()
        row = [float(x) for x in row]
        lst.append(row)

    loc = getLocation(lst)
    print("The location of the largest element is " + str(loc.maxValue) + " at (" + str(loc.row) + "," + str(
        loc.col) + ")")


main()
