# 15.12 (Find the largest number in a list) Write a recursive function that returns the
# largest integer in a list. Write a test program that prompts the user to enter a list
# of integers and displays the largest element.

def getLargest(lst):
    max = lst[0]
    return getLargestHelper(lst, 0, len(lst), max)


def getLargestHelper(lst, startIndx, endIndx, max):
    if startIndx == endIndx:
        return max

    if lst[startIndx] > max:
        max = lst[startIndx]

    return getLargestHelper(lst, startIndx + 1, endIndx, max)


lst = input("Enter a list of integers: ").split()
lst = [eval(x) for x in lst]

print(getLargest(lst))
