# 6.6 (Display patterns) Write a function to display a pattern as follows:
#               1
#             2 1
#           3 2 1
#             ...
# n n-1 ... 3 2 1
# The function header is
# def displayPattern(n):
# Write a test program that prompts the user to enter a number n and invokes
# displayPattern(n) to display the pattern.

def displayPattern(n):
    for i in range(1, n + 1):
        for j in range(n, i - 1, -1):
            print(format(" ", "2s"), end=" ")
        for j in range(i, 0, -1):
            print(format(j, "2d"), end=" ")
        print()


n = eval(input("Enter an integer: "))
displayPattern(n)
