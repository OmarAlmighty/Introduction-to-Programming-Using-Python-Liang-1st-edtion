# 5.10 (Find the highest score) Write a program that prompts the user to enter the number
# of students and each student’s score, and displays the highest score. Assume that
# the input is stored in a file named score.txt, and the program obtains the input from
# the file.

studentName = ""
studentScore = 0
maxScore = -1
maxName = ""
while True:
    studentName = input("Enter a student name(x to stop): ")
    if studentName.lower() == "x":
        break
    studentScore = eval(input("Enter a student score: "))

    if studentScore > maxScore:
        maxScore = studentScore
        maxName = studentName

print("Top student is", maxName, "with score", maxScore)
