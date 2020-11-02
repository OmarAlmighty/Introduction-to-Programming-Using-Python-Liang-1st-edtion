# 13.3 (Process scores in a text file) Suppose that a text file contains an unspecified number
# of scores. Write a program that reads the scores from the file and displays their
# total and average. Scores are separated by blanks. Your program should prompt
# the user to enter a filename.

filename = input("Enter a filename: ").strip()
file = open(filename, 'r')
count = 0
avg = 0
sum = 0
for line in file:
    scores = line.split()
    scores = [eval(s) for s in scores]
    count += len(scores)
    for s in scores:
        sum += s

avg = sum / count

print("There are", count, "scores")
print("The total is", sum)
print("The average is", avg)
