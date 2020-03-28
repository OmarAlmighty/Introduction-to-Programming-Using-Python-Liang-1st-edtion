# 10.31 (Occurrences of each digit in a string) Write a function that counts the occurrences
# of each digit in a string using the following header:
# def count(s):
# The function counts how many times a digit appears in the string. The return
# value is a list of ten elements, each of which holds the count for a digit. For
# example, after executing counts = count("12203AB3"), counts[0] is 1,
# counts[1] is 1, counts[2] is 2, and counts[3] is 2.
# Write a test program that prompts the user to enter a string and displays the
# number of occurrences of each digit in the string.

def getDistinctDigits(s):
    lst = []
    for x in s:
        if x not in lst:
            lst.append(x)

    return lst
def count(s):
    counts = []
    lst = getDistinctDigits(s)
    for i in range(len(lst)):
        n = lst[i]
        counts.append(s.count(n))
    return counts


s = input("Enter a string: ")
counts = count(s)
s = list(s)
lst = getDistinctDigits(s)
lst2 = [x for x in lst]
lst.sort()
for i in lst:
    print(i, "occurs", counts[lst2.index(i)], "times")
