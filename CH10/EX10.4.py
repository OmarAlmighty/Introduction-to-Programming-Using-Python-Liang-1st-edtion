# 10.4 (Analyze scores) Write a program that reads an unspecified number of scores and
# determines how many scores are above or equal to the average and how many
# scores are below the average. Assume the input numbers are separated by one
# space in one line.

s = input("Enter scores: ")
lst = [int(x) for x in s.split()]
avg = sum(lst) / len(lst)
above = 0
below = 0
for x in lst:
    if x >= avg:
        above += 1
    else:
        below += 1
print("There are", above, "value >= ", avg, "and", below, "<", avg)
