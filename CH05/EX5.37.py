# 5.37 (Summation) Write a program that computes the following summation:
import math

sum = 0

for i in range(1, 625):
    sum += 1 / (i + math.sqrt((i + 1)))

print("The summation of the series is", sum)
