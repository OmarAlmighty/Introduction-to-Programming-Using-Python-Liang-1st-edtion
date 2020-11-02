# 13.17 (Process large dataset) A university posts its employee salary at http://cs
# .armstrong.edu/liang/data/Salary.txt. Each line in the file consists of faculty first
# name, last name, rank, and salary (see Exercise 13.16). Write a program to display
# the total salary for assistant professors, associate professors, full professors, and
# all faculty, respectively, and display the average salary for assistant professors,
# associate professors, full professors, and all faculty, respectively.

import urllib
from urllib import request

#file = open("database.txt", "r")
file = urllib.request.urlopen("http://cs.armstrong.edu/liang/data/Salary.txt")
data = file.readlines()

sumAssistant = 0
countAssistant = 0

sumAssociate = 0
countAssociate = 0

sumFull = 0
countFull = 0

for line in data:
    line = line.split()
    if line[2] == "assistant":
        sumAssistant += eval(line[3])
        countAssistant += 1
    elif line[2] == "associate":
        sumAssociate += eval(line[3])
        countAssociate += 1
    else:
        sumFull += eval(line[3])
        countFull += 1

print("The total salary for assistant professors: ", sumAssistant)
print("The total salary for associate professors: ", sumAssociate)
print("The total salary for full professors: ", sumFull)
print("The total salary for all faculty: ", (sumFull + sumAssociate + countAssistant))

print("The average salary for assistant professors: ", sumAssistant / countAssistant)
print("The average salary for associate professors: ", sumAssociate / countAssociate)
print("The average salary for full professors: ", sumFull / countFull)
print("The average salary for all faculty: ", (sumFull + sumAssociate + countAssistant) /
      (countAssociate + countFull + countAssistant))
