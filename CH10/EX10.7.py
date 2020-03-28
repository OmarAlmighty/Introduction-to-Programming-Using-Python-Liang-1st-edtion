# 10.7 (Count single digits) Write a program that generates 1,000 random integers
# between 0 and 9 and displays the count for each number. (Hint: Use a list of ten
# integers, say counts, to store the counts for the number of 0s, 1s, ..., 9s.)
import random

lst = []
for i in range(1000):
    lst.append(random.randint(0, 9))

counts = []
for i in range(10):
    counts.append(lst.count(lst[i]))

for i in range(10):
    print(i, ":", counts[i], "times")
