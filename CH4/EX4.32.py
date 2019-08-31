# 4.32 (Geometry: point on line segment) Exercise 4.31 shows how to test whether a point
# is on an unbounded line. Revise Exercise 4.31 to test whether a point is on a line
# segment. Write a program that prompts the user to enter the x- and y-coordinates
# for the three points p0, p1, and p2 and displays whether p2 is on the line segment
# from p0 to p1.
x0, y0, x1, y1, x2, y2 = eval(input("Enter coordinates for the three points p0, p1, and p2: "))

d = (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)

if d <= 0.0000000001 and ((x0 <= x2 and x2 <= x1) or (x0 >= x2 and x2 >= x1)):
    print("(", x2, ", ", y2, ") is on the line segment from"
          , "(", x0, ", ", y0, ") to ", "(",
          x1, ", ", y1, ")")
else:
    print("(", x2, ", ", y2, ") is not on the line segment from"
          , "(", x0, ", ", y0, ") to ", "("
          , x1, ", ", y1, ")")
