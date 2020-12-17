# 7.8 (Stopwatch) Design a class named StopWatch. The class contains:
# ■ The private data fields startTime and endTime with get methods.
# ■ A constructor that initializes startTime with the current time.
# ■ A method named start() that resets the startTime to the current time.
# ■ A method named stop() that sets the endTime to the current time.
# ■ A method named getElapsedTime() that returns the elapsed time for the
# stop watch in milliseconds.
# Draw the UML diagram for the class, and then implement the class. Write a test
# program that measures the execution time of adding numbers from 1 to
# 1,000,000.
from CH7.StopWatch import StopWatch

sw = StopWatch()
res = 0
sw.start()
for i in range(1, 1000001):
    res += i

sw.end()
print("The elapsed time is:", sw.getElapsedTime())
