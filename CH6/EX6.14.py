# 6.14 (Estimate ) can be computed using the following series:
# Write a function that returns m(i) for a given i and write a test program that displays
# the following table:
# i m(i)
# 1 4.0000
# 101 3.1515
# 201 3.1466
# 301 3.1449
# 401 3.1441
# 501 3.1436
# 601 3.1433
# 701 3.1430
# 801 3.1428
# 901 3.1427
from CH6Module import MyFunctions


def main():
    print("i\t\t\t  m(i)")
    for i in range(1, 1001, 100):
        print(format(i, ".0f"), "\t\t", format(MyFunctions.computePi(i), "-3.4f"))


main()
