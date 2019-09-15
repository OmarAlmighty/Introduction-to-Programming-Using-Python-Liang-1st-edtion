# 5.13 (Find numbers divisible by 5 or 6, but not both) Write a program that displays, ten
# numbers per line, all the numbers from 100 to 200 that are divisible by 5 or 6, but
# not both. The numbers are separated by exactly one space.

counter = 0
for i in range(100, 200):
    if i % 5 == 0 or i % 6 == 0 and not (i % 5 == 0 and i % 6 == 0):
        if counter == 10:
            print()
            counter = 0
        print(i, end=" ")
        counter += 1
