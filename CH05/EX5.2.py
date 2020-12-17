# 5.2 (Repeat additions) Listing 5.4, SubtractionQuizLoop.py, generates five random
# subtraction questions. Revise the program to generate ten random addition questions
# for two integers between 1 and 15. Display the correct count and test time.
import random
import time

correct = 0
count = 0
NUMBER_OF_QUESTIONS = 10
startTime = time.time()
while count < NUMBER_OF_QUESTIONS:
    n1 = random.randint(1, 15)
    n2 = random.randint(1, 15)
    ans = eval(input("What is " + str(n1) + "+" + str(n2) + " = "))

    if ans == (n1 + n2):
        print("You are correct!")
        correct += 1
    else:
        print("Your answer is wrong.\n", n1, "+", n2, "=", (n1 + n2))

    count += 1

endTime = time.time()
testTime = int(endTime - startTime)
print("Correct count is", correct, "out of",
      NUMBER_OF_QUESTIONS, "\nTest time is", testTime, "seconds")
