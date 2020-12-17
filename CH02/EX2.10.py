# (Physics: find runway length) Given an airplane’s acceleration a and take-off
# speed v, you can compute the minimum runway length needed for an airplane to
# take off using the following formula:
# Write a program that prompts the user to enter v in meters/second (m/s) and the
# acceleration a in meters/second squared and displays the minimum runway
# length.

speed, acc = eval(input("Enter speed and acceleration: "))
len = speed ** 2 / (2 * acc)
print("The minimum runway length for this airplane is", len, "meters")
