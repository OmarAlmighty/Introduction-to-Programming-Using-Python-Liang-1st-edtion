# 5.38 (Simulation: clock countdown) You can use the time.sleep(seconds) function
# in the time module to let the program pause for the specified seconds. Write a
# program that prompts the user to enter the number of seconds, displays a message
# at every second, and terminates when the time expires.
import time

seconds = eval(input("Enter the number of second: "))

while seconds > 0:
    time.sleep(1)
    if seconds > 1:
        print(str(seconds) + " seconds remaining")
    else:
        print("1 second remaining")
    seconds -= 1

print("Stopped")