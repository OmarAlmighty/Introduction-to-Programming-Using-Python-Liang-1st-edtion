# 11.19 (Pattern recognition: four consecutive equal numbers) Write the following
# function that tests whether a two-dimensional list has four consecutive numbers
# of the same value, either horizontally, vertically, or diagonally:
# def isConsecutiveFour(values):
# Write a test program that prompts the user to enter the number of rows and
# columns of a two-dimensional list and then the values in the list. The program
# displays True if the list contains four consecutive numbers with the
# same value; otherwise, it displays False. Here are some examples of the
# True cases:

def isConsecutiveFour(values):
    for i in range(len(values)):
        for j in range(len(values[i])):
            val = values[i][j]

            # search horizontally
            if j <= len(values[i]) - 4:
                v1 = values[i][j + 1]
                v2 = values[i][j + 2]
                v3 = values[i][j + 3]
                if val == v1 == v2 == v3:
                    return True

            # search vertically
            if i <= len(values) - 4:
                v1 = values[i + 1][j]
                v2 = values[i + 2][j]
                v3 = values[i + 3][j]
                if val == v1 == v2 == v3:
                    return True

            # search diagonally
            if i <= len(values) - 4 and j <= len(values[i]) - 4:
                v1 = values[i + 1][j + 1]
                v2 = values[i + 2][j + 2]
                v3 = values[i + 3][j + 3]
                if val == v1 == v2 == v3:
                    return True

            # search diagonally
            if i <= len(values) - 4 and j >= 3:
                v1 = values[i + 1][j - 1]
                v2 = values[i + 2][j - 2]
                v3 = values[i + 3][j - 3]
                if val == v1 == v2 == v3:
                    return True
    return False


row, col = eval(input("Enter number of rows and columns: "))
values = []

for i in range(row):
    r = input("Enter a row " + str(i) + " values separted by space: ").split()
    if len(r) > col or len(r) < col:
        print("Error more or less values input")
        break
    r = [eval(x) for x in r]
    values.append(r)

for x in values:
    print(x)

print(isConsecutiveFour(values))
