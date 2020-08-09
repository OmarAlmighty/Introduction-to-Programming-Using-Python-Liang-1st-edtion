# 11.52 (Latin square) A Latin square is an n by n list filled with n different Latin letters,
# each occurring exactly once in each row and once in each column. Write a program
# that prompts the user to enter the number n and the list of characters, as
# shown in the sample output and check if the input list is a Latin square. The characters
# are the first n characters starting from A.
import sys


def main():
    n = eval(input("Enter number n: "))
    print("Enter", n, "rows of letters separated by spaces:  ")

    letters = []
    for i in range(n):
        letters.append(chr(ord('A') + i))

    matrix = []
    for i in range(n):
        s = input()
        row = s.split()
        matrix.append(row)

        tempRow = [x for x in row]
        tempRow.sort()
        if len(row) != n:
            print("Wrong input: you need to enter exactly ", n, "characters")
            sys.exit()
        elif letters != tempRow:
            print("Wrong input: the letters must be from", letters[0], "to", letters[-1])
            sys.exit()

    transposedMatrix = getTransposed(matrix)

    for i in range(n):
        transposedMatrix[i].sort()
        if letters != transposedMatrix[i]:
            print("The input array is not a Latin square")
            sys.exit()

    print("The input array is a Latin square")


def getTransposed(matrix):
    result = []

    for j in range(len(matrix)):
        row = []
        for i in range(len(matrix)):
            row.append(matrix[i][j])
        result.append(row)

    return result


main()
