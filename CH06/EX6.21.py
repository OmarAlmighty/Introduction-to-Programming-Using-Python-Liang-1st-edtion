# 6.21 (Math: approximate the square root) There are several techniques for implementing
# the sqrt function in the math module. One such technique is known as the
# Babylonian function. It approximates the square root of a number, n, by repeatedly
# performing a calculation using the following formula:
# nextGuess = (lastGuess + (n / lastGuess)) / 2
# When nextGuess and lastGuess are almost identical, nextGuess is the
# approximated square root. The initial guess can be any positive value (e.g., 1).
# This value will be the starting value for lastGuess. If the difference between
# nextGuess and lastGuess is less than a very small number, such as 0.0001,
# you can claim that nextGuess is the approximated square root of n. If not,
# nextGuess becomes lastGuess and the approximation process continues.
# Implement the following function that returns the square root of n.
from CH6Module import MyFunctions

n = eval(input("Enter a number: "))
print("The square root of", n, "is", MyFunctions.sqrt(n))
