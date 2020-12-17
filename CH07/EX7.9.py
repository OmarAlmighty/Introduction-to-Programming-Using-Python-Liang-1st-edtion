# 7.9 (Geometry: intersection) Suppose two line segments intersect. The two endpoints
# for the first line segment are (x1, y1) and (x2, y2) and for the second line segment
# are (x3, y3) and (x4, y4). Write a program that prompts the user to enter these
# four endpoints and displays the intersecting point. (Hint: Use the
# LinearEquation class from Exercise 7.7.)
from CH7.LinearEquation import LinearEquation

x1, y1, x2, y2 = eval(input("Enter the endpoints of the first line segment: "))
x3, y3, x4, y4 = eval(input("Enter the endpoints of the second line segment: "))

a = y1 - y2
b = -x1 + x2
c = y3 - y4
d = -x3 + x4
e = -y1 * (x1 - x2) + (y1 - y2) * x1
f = -y3 * (x3 - x4) + (y3 - y4) * x3

eq = LinearEquation(a, b, c, d, e, f)
print("The intersecting point is: (", eq.getX(), ",", eq.getY(), ")")
