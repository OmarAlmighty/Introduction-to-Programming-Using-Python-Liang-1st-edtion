# 5.29 (Display leap years) Write a program that displays, ten per line, all the leap years
# in the twenty-first century (from year 2001 to 2100). The years are separated by
# exactly one space.

counter = 0
for i in range(2001, 2100):

    if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
        if counter == 10:
            print()
            counter = 0
        print(i, end='   ')
        counter += 1
