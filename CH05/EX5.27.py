# 5.27 (Compute ) You can approximate by using the following series:
# Write a program that displays the value for i = 10000, 20000, . . ., and
# 100000.

for i in range(10000, 100001, 10000):
    sum = 0
    for j in range(1, i + 1):
        sum += ((-1) ** (j + 1)) / (2 * j - 1)

    pi = 4 * sum
    print("PI value for i=", i, "is", pi)
