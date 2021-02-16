# 15.5 (Sum series) Write a recursive function to compute the following series:
# m(i) = 1/3 + 2/5 + 3/7 + 4/9 + 5/11 + 6/13 + ... + i/2i + 1
# Write a test program that displays m(i) for i 1, 2, ..., 10.

def sumSeries(i):
    if i == 1:
        return 1/3
    return i / (2 * i + 1) + sumSeries(i - 1)

for i in range(1, 11):
    print("The sum series for i=", i, "is", sumSeries(i))
