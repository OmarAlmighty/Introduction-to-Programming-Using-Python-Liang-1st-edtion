# 5.11 (Find the two highest scores) Write a program that prompts the user to enter the
# number of students and each student’s score, and displays the highest and secondhighest
# scores.

maxScroe1 = 0
maxScore2 = -1
maxName1 = maxName2 = ""

while True:
    name = input("Enter Student's name(x to Stop): ")
    if name.lower() == "x":
        break
    score = eval(input("Enter student's score: "))

    if score > maxScroe1 and score > maxScore2:
        maxScore2 = maxScroe1
        maxScroe1 = score
        maxName2 = maxName1
        maxName1 = name
    elif score > maxScore2:
        maxScore2 = score
        maxName2 = name

print("Top Student is", maxName1, "with score", maxScroe1)
print("The 2nd Top student is", maxName2, "with score", maxScore2)
