# 5.46 (Statistics: compute mean and standard deviation) In business applications, you
# are often asked to compute the mean and standard deviation of data. The mean is
# simply the average of the numbers. The standard deviation is a statistic that tells
# you how tightly all the various data are clustered around the mean in a set of data.
# For example, what is the average age of the students in a class? How close are the
# ages? If all the students are the same age, the deviation is 0. Write a program that
# prompts the user to enter ten numbers, and displays the mean and standard deviations
# of these numbers using the following formula:
import math

COUNT = 10
sum = 0
squareSum = 0
print("Enter ten numbers: ", end='')

for i in range(COUNT):
    n = eval(input())
    sum += n
    squareSum += n * n

mean = sum / COUNT
dev = math.sqrt((squareSum - sum * sum / COUNT) / (COUNT - 1))

print("The mean is", mean)
print("The standard deviation is", dev)
