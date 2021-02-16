# 15.4 (Sum series) Write a recursive function to compute the following series:
# m(i) = 1 + 1/2 + 1/3 + ... + 1/i
# Write a test program that displays m(i) for i 1, 2, ..., 10.

def sumSeries(i):
    if i == 1:
        return 1
    return 1 / i + sumSeries(i-1)


for i in range(1, 11):
    print("The sum series for i=", i, "is", sumSeries(i))
