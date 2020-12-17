# 6.19 (Geometry: point position) Exercise 4.31 shows how to test whether a point is on
# the left side of a directed line, on the right, or on the same line. Write the following
# functions:
# # Return true if point (x2, y2) is on the left side of the
# # directed line from (x0, y0) to (x1, y1)
# def leftOfTheLine(x0, y0, x1, y1, x2, y2):
# # Return true if point (x2, y2) is on the same
# # line from (x0, y0) to (x1, y1)
# def onTheSameLine(x0, y0, x1, y1, x2, y2):
# # Return true if point (x2, y2) is on the
# # line segment from (x0, y0) to (x1, y1)
# def onTheLineSegment(x0, y0, x1, y1, x2, y2):
# Write a program that prompts the user to enter the three points for p0, p1, and p2
# and displays whether p2 is on the left of the line from p0 to p1, on the right, on the
# same line, or on the line segment.
from CH6Module import MyFunctions

x0, y0, x1, y1, x2, y2 = eval(input("Enter coordinates for the three points p0, p1, and p2: "))
if MyFunctions.leftOfTheLine(x0, y0, x1, y1, x2, y2):
    print("p2 is on the left side of the line from p0 to p1")

elif MyFunctions.onTheSameLine(x0, y0, x1, y1, x2, y2):
    print("p2 is on the same line from p0 to p1")

elif MyFunctions.onTheLineSegment(x0, y0, x1, y1, x2, y2):
    print("p2 is on the line segment from p0 to p1")
