# 10.8 (Find the index of the smallest element) Write a function that returns the index of
# the smallest element in a list of integers. If the number of such elements is greater
# than 1, return the smallest index. Use the following header:
# def indexOfSmallestElement(lst):
# Write a test program that prompts the user to enter a list of numbers, invokes this
# function to return the index of the smallest element, and displays the index.

def indexOfSmallestElement(lst):
    smallest = float("inf")
    smallestInd = 0
    for x in range(len(lst)):
        if lst[x] < smallest:
            smallest = lst[x]
            smallestInd = x
    return smallestInd


def main():
    lst = [0, 3, 4, 5, 7, 8]
    print(indexOfSmallestElement(lst))

main()
