# 4.27 (Geometry: points in triangle?) Suppose a right triangle is placed in a plane as
# shown below. The right-angle point is at (0, 0), and the other two points are at
# (200, 0), and (0, 100). Write a program that prompts the user to enter a point with
# x- and y-coordinates and determines whether the point is inside the triangle.
import math

X1 = Y1 = 0
X2 = 0
Y2 = 100
X3 = 200
Y3 = 0
x, y = eval(input("Enter a point's x- and y-coordinates: "))

# below hypotenuse and to the right of y axis and above x axis
if x + 2 * y < X3 and 0 <= x <= X3 and 0 <= y <= Y2:
    print("The point is in the triangle ")
else:
    print("The point is not in the triangle ")

