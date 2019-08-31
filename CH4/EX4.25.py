# 4.25 (Geometry: intersecting point) Two points on line 1 are given as (x1, y1) and (x2,
# y2) and on line 2 as (x3, y3) and (x4, y4), as shown in Figure 4.9a–b.
# The intersecting point of the two lines can be found by solving the following linear
# equation:
# (y1 - y2)x - (x1 - x2)y = (y1 - y2)x1 - (x1 - x2)y1
# (y3 - y4)x - (x3 - x4)y = (y3 - y4)x3 - (x3 - x4)y3
# This linear equation can be solved using Cramer’s rule (see Exercise 4.3). If the
# equation has no solutions, the two lines are parallel (Figure 4.9c). Write a program
# that prompts the user to enter four points and displays the intersecting point.

x1, y1, x2, y2, x3, y3, x4, y4 = eval(input("Enter x1, y1, x2, y2, x3, y3, x4, y4: "))

cramer = (y1 - y2) * (x4 - x3) - (x2 - x1) * (y3 - y4)

if cramer == 0:
    print("The two lines are parallel")
else:
    a = y1 - y2
    b = x2 - x1
    c = y3 - y4
    d = x4 - x3
    e = (y1 - y2) * x1 + (x2 - x1) * y1
    f = (y3 - y4) * x3 + (x4 - x3) * y3
    x = (e * d - b * f) / cramer
    y = (a * f - e * c) / cramer
    print("The intersecting point is at (", format(x, "0.5f"), ",", format(y, "0.5f"), ")")
