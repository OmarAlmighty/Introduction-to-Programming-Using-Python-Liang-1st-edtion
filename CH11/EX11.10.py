# 11.10 (Largest rows and columns) Write a program that randomly fills in 0s and 1s into
# a 4*4 matrix, prints the matrix, and finds the rows and columns with the most
# 1s.
import random


def count_ones(lst):
    count = 0
    current_count = count
    indx = []
    for row in range(len(lst)):
        for col in lst[row]:
            if col == 1:
                current_count += 1
        if current_count > count:
            indx.clear()
            count = current_count
            indx.append(row)
        elif current_count == count:
            indx.append(row)
        current_count = 0
    return indx


lst = []
for i in range(4):
    lst.append([])
    for j in range(4):
        lst[i].append(random.randint(0, 1))

for r in lst:
    for c in r:
        print(c, end=" ")
    print()

print("The largest row index:", count_ones(lst))

# transose matrix
lst = [[row[i] for row in lst] for i in range(len(lst[0]))]

print("The largest column index:", count_ones(lst))
