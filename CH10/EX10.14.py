# 10.14 (Revise selection sort) In Section 10.11.1, you used selection sort to sort a list.
# The selection-sort function repeatedly finds the smallest number in the current
# list and swaps it with the first one. Rewrite this program by finding the largest
# number and swapping it with the last one. Write a test program that reads in ten
# numbers, invokes the function, and displays the sorted numbers.

# The function for sorting elements in ascending order
def selectionSort(lst):
    for i in range(len(lst) - 1, 0, -1):
        # Find the minimum in the lst[i : len(lst)]
        currentMax, currentMaxIndex = lst[i], i

        for j in range(i):
            if currentMax < lst[j]:
                currentMax, currentMaxIndex = lst[j], j

        # Swap lst[i] with lst[currentMaxIndex] if necessary
        if currentMaxIndex != i:
            lst[currentMaxIndex], lst[i] = lst[i], currentMax


def main():
    lst = [5, 9, 14, 2, 0, 1, 3]
    selectionSort(lst)
    print(lst)


main()
