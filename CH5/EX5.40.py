# 5.40 (Simulation: heads or tails) Write a program that simulates flipping a coin one
# million times and displays the number of heads and tails.
import random

print("Simulating flipping a coin 1000000 times")

head = 0
tail = 0

print("Wait....")
for i in range(0, 1000000):
    if random.randint(0, 1) == 0:
        head += 1
    else:
        tail += 1

print("The number of heads:", head, "and the number of tails:", tail)
