# 4.31 (Geometry: point position) Given a directed line from point p0(x0, y0) to p1(x1,
# y1), you can use the following condition to decide whether a point p2(x2, y2) is
# on the left side of the line, on the right side of the line, or on the same line (see
# Figure 4.12):
# Write a program that prompts the user to enter the x- and y-coordinates for the
# three points p0, p1, and p2 and displays whether p2 is on the left side of the line
# from p0 to p1, on the right side, or on the same line.

x0, y0, x1, y1, x2, y2 = eval(input("Enter coordinates for the three points p0, p1, and p2: "))

d = (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)

if d > 0:
    print("p2 is on the left side of the line from p0 to p1")
elif d == 0:
    print("p2 is on the same line from p0 to p1")
else:
    print("p2 is on the right side of the line from p0 to p1")
