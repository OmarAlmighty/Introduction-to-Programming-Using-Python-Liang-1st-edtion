# (Geometry: area of a pentagon) Write a program that prompts the user to enter the
# length from the center of a pentagon to a vertex and computes the area of the pentagon,
# as shown in the following figure.The formula for computing the area of a pentagon is where s is
# the length of a side. The side can be computed using the formula
# where r is the length from the center of a pentagon to a vertex.
import math

r = eval(input("Enter the length from the center to a vertex: "))
s = 2 * r * math.sin(math.pi / 5)
area = 3 * math.sqrt(3) / 2 * s ** 2
print("The area of the pentagon is", area)
