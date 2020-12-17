# (Geometry: area of a regular polygon) A regular polygon is an n-sided polygon in
# which all sides are of the same length and all angles have the same degree (i.e., the
# polygon is both equilateral and equiangular). The formula for computing the area
# of a regular polygon is
# Here, s is the length of a side. Write a program that prompts the user to enter the
# number of sides and their length of a regular polygon and displays its area.
import math

n = int(input("Enter the number of sides: "))
s = eval(input("Enter the side: "))
area = (n * s ** 2) / (4 * math.tan(math.pi / n))
print("The area of the polygon is", area)
