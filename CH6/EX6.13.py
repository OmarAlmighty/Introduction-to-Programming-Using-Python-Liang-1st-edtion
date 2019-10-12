# 6.13 (Sum series) Write a function to compute the following series:
# Write a test program that displays the following table:
# i m(i)
# 1 0.5000
# 2 1.1667
# ...
# 19 16.4023
# 20 17.3546

def sumSeries(i):
    sum = 0
    for i in range(1, i + 1):
        sum += i / (i + 1)
    return sum


def main():
    print("i\t    m(i)")
    for i in range(1, 21):
        print(format(i, "-0.0f"), format(" ", "4s"), format(sumSeries(i), ".4f"))


main()
