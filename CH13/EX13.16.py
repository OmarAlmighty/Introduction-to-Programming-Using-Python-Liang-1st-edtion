# 13.16 (Create large dataset) Create a data file with 1000 lines. Each line in the file consists
# of a faculty first name, last name, rank, and salary. Faculty’s first name and
# last name for the ith line are FirstNamei and LastNamei. The rank is randomly
# generated as assistant, associate, and full. The salary is randomly generated as a
# number with two digits after the decimal point. The salary for assistant professor
# should be in the range from 50,000 to 80,000, for associate professor from 60,000
# to 110,000, and for full professor from 75,000 to 130,000. Save the file in
# Salary.txt. Here are some sample data:.
# FirstName1 LastName1 assistant 60055.95
# FirstName2 LastName2 associate 81112.45
# . . .
# FirstName1000 LastName1000 full 92255.21
import os
import random

if not os.path.isfile("database.txt"):
    file = open("database.txt", 'w')

rank = ["assistant", "associate", "full"]
for i in range(1, 1001):
    fn = "FirstName" + str(i)
    ln = "LastName" + str(i)
    r = random.randint(0, 2)
    rnk = rank[r]
    if r == 0:
        sal = str(round(random.random() * 30000 + 50000, 2))
    elif r == 1:
        sal = str(round(random.random() * 50000 + 60000, 2))
    else:
        sal = str(round(random.random() * 55000 + 75000, 2))

    line = fn + ' ' + ln + ' ' + rnk + ' ' + sal + '\n'
    file.write(line)

file.close()

