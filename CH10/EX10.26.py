# 10.26 (Merge two sorted lists) Write the following function that merges two sorted lists
# into a new sorted list:
# def merge(list1, list2):
# Implement the function in a way that takes len(list1) + len(list2) comparisons.
# Write a test program that prompts the user to enter two sorted lists and
# displays the merged list.

def merge(l1, l2):
    res = []
    c1 = 0
    c2 = 0
    while c1 < len(l1) and c2 < len(l2):
        m1 = l1[c1]
        m2 = l2[c2]
        if m1 < m2:
            res.append(m1)
            c1 += 1
        else:
            res.append(m2)
            c2 += 1

    while c1 < len(l1):
        res.append(l1[c1])
        c1 += 1

    while c2 < len(l2):
        res.append(l2[c2])
        c2 += 1

    return res


l1 = [int(x) for x in input("Enter list1: ").split()]
l2 = [int(x) for x in input("Enyer list2: ").split()]
res = merge(l1, l2)

print(res)
