# 10.9 (Statistics: compute deviation) Exercise 5.46 computes the standard deviation of
# numbers. This exercise uses a different but equivalent formula to compute the
# standard deviation of n numbers.To compute the standard deviation with this formula, you have to store the
# individual numbers using a list, so that they can be used after the mean is
# obtained.
# Your program should contain the following functions:
# # Compute the standard deviation of values
# def deviation(x):
# # Compute the mean of a list of values
# def mean(x):
# Write a test program that prompts the user to enter a list of numbers and displays
# the mean and standard deviation

# Compute the standard deviation of values
import math


def deviation(x):
    mn = mean(x)
    print("The mean is", mn)
    a = [(y - mn) ** 2 for y in x]
    sm = sum(a)
    dev = math.sqrt(sm / (len(a) - 1))
    return dev


# Compute the mean of a list of values
def mean(x):
    return sum(x) / len(x)


def main():
    lst = input("Enter numbers: ").split()
    lst = [float(x) for x in lst]
    print("The standard deviation", deviation(lst))


main()
