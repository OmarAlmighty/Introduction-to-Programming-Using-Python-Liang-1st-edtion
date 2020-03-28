# 10.13 (Eliminate duplicates) Write a function that returns a new list by eliminating the
# duplicate values in the list. Use the following function header:
# def eliminateDuplicates(lst):
# Write a test program that reads in a list of integers, invokes the function, and displays
# the result.

def eliminateDuplicates(lst):
    size = len(lst)
    i = 0
    while i < size:
        current = lst[i]
        x = i + 1
        while x < size:
            if current == lst[x]:
                lst.pop(x)
                size = len(lst)
            x += 1
        i += 1


def main():
    lst = input("Enter ten numbers: ").split()
    lst = [int(x) for x in lst]
    eliminateDuplicates(lst)
    print("The distinct numbers are:", lst)


main()
