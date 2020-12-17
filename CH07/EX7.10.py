# 7.10 (The Time class) Design a class named Time. The class contains:
# ■ The private data fields hour, minute, and second that represent a time.
# ■ A constructor that constructs a Time object that initializes hour, minute, and
# second using the current time.
# ■ The get methods for the data fields hour, minute, and second, respectively.
# ■ A method named setTime(elapseTime) that sets a new time for the object
# using the elapsed time in seconds. For example, if the elapsed time is 555550
# seconds, the hour is 10, the minute is 19, and the second is 12.
# Draw the UML diagram for the class, and then implement the class. Write a test
# program that creates a Time object and displays its hour, minute, and second.
# Your program then prompts the user to enter an elapsed time, sets its elapsed
# time in the Time object, and displays its hour, minute, and second.
from CH7.Time import Time

currentTime = Time()
print("Current time is", currentTime.getHour(),
      ":", currentTime.getMinute(), ":", currentTime.getSecond())

elapseTime = eval(input("Enter the elapse time: "))

currentTime.setTime(elapseTime)
print("The hour:minute:second for elapse time is",
      currentTime.getHour(), ":", currentTime.getMinute(), ":", currentTime.getSecond())
