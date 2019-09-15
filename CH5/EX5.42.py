# 5.42 (Monte Carlo simulation) A square is divided into four smaller regions as shown in
# (a). If you throw a dart into the square one million times, what is the probability for
# the dart to fall into an odd-numbered region? Write a program to simulate the
# process and display the result. (Hint: Place the center of the square in the center of
# a coordinate system, as shown in (b). Randomly generate a point in the square and
# count the number of times for a point to fall in an odd-numbered region.)
import random

counter = 0
print("Throwing the dart....")
for i in range(0, 1000000):
    if random.randint(1, 4) % 2 != 0:
        counter += 1

prob = counter / 1000000
print("The probability that the dart fall in an odd numbered region is", prob)
