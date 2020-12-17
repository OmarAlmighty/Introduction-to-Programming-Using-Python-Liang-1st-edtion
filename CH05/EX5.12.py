# 5.12 (Find numbers divisible by 5 and 6) Write a program that displays, ten numbers
# per line, all the numbers from 100 to 1,000 that are divisible by 5 and 6. The numbers
# are separated by exactly one space.

counter = 0
for i in range(100, 1000):
    if i % 5 == 0 and i % 6 == 0:
        if counter == 10:
            print()
            counter = 0

        print(i, end=" ")
        counter += 1
