# 6.1 (Math: pentagonal numbers) A pentagonal number is defined as for
# and so on. So, the first few numbers are 1, 5, 12, 22, .... Write a
# function with the following header that returns a pentagonal number:
# def getPentagonalNumber(n):
# Write a test program that uses this function to display the first 100 pentagonal
# numbers with 10 numbers on each line.

def getPentagonalNumber(n):
    num = n * (3 * n - 1) / 2
    return int(num)


def main():
    count = 1
    for i in range(1, 101):
        print(getPentagonalNumber(i), end=' ')
        if count % 10 == 0:
            print()
            count = 0

        count += 1


main()
