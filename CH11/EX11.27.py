# 11.27 (Column sorting) Implement the following function to sort the columns in a twodimensional
# list. A new list is returned and the original list is intact.
# def sortColumns(m):
# Write a test program that prompts the user to enter a 3 * 3matrix of numbers and
# displays a new column-sorted matrix.

def sortColumns(m):
    m1 = [[x[i] for x in m] for i in range(len(m))]

    for col in m1:
        col.sort()

    m1 = [[x[i] for x in m1] for i in range(len(m1))]
    return m1


print('Enter a 3-by-3 matrix row by row: ')
m = []
for i in range(3):
    m.append(input().split())

print('The column-sorted list is ')
res = sortColumns(m)
for r in res:
    for v in r:
        print(v, end=' ')
    print()

