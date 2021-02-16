# 15.6 (Summing series) Write a recursive function to compute the following series:
# m(i) = 1/2 + 2/3 + ... + i/i + 1
# Write a test program that prompts the user to enter an integer for i and displays m(i).

def sumSeries(i):
    if i == 1:
        return 1 / 2
    return i / (i + 1) + sumSeries(i - 1)


for i in range(1, 11):
    print("The sum series for i=", i, "is", sumSeries(i))
