# (Geometry: area of a pentagon) The area of a pentagon can be computed using the
# following formula (s is the length of a side):
# Write a program that prompts the user to enter the side of a pentagon and displays
# the area.
import math

s = eval(input("Enter the side: "))
area = (5 * s**2) / (4 * math.tan(math.pi / 5))
print("The area of the pentagon is", area)
