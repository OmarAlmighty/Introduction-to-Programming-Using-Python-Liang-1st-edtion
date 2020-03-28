# 10.15 (Sorted?) Write the following function that returns true if the list is already
# sorted in increasing order:
# def isSorted(lst):
# Write a test program that prompts the user to enter a list and displays whether the
# list is sorted or not.

def isSorted(lst):
    for i in range(len(lst)):
        current = lst[i]
        for y in range(i + 1, len(lst)):
            if current > lst[y]:
                return False

    return True


def main():
    lst = input("Enter list: ").split()
    lst = [int(x) for x in lst]
    print(isSorted(lst))


main()
