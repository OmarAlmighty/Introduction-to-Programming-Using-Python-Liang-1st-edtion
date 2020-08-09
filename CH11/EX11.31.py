# 11.31 (Geometry: intersecting point) Write a function that returns the intersecting point of
# two lines. The intersecting point of the two lines can be found by using the formula
# shown in Exercise 4.25. Assume that (x1, y1) and (x2, y2) are the two points on line
# 1 and (x3, y3) and (x4, y4) are the two points on line 2. The function header is:
# def getIntersectingPoint(points):
# The points are stored in the 4*2 two-dimensional list points, with
# (points[0][0], points[0][1]) for (x1, y1). The function returns the intersecting
# point (x, y) in a list, and None if the two lines are parallel. Write a program
# that prompts the user to enter four points and displays the intersecting point. See
# Exercise 4.25 for a sample run.

def getIntersectingPoint(points):
    x1 = points[0][0];
    y1 = points[0][1]
    x2 = points[1][0];
    y2 = points[1][1]
    x3 = points[2][0];
    y3 = points[2][1]
    x4 = points[3][0];
    y4 = points[3][1]

    cramer = (y1 - y2) * (x4 - x3) - (x2 - x1) * (y3 - y4)
    res = []
    if cramer == 0:
        return res
    else:
        a = y1 - y2
        b = x2 - x1
        c = y3 - y4
        d = x4 - x3
        e = (y1 - y2) * x1 + (x2 - x1) * y1
        f = (y3 - y4) * x3 + (x4 - x3) * y3
        x = (e * d - b * f) / cramer
        y = (a * f - e * c) / cramer
        res.append(x)
        res.append(y)
        return res


points = []
for i in range(4):
    m = input("Enter x,y: ").split()
    m = [eval(x) for x in m]
    points.append(m)

res = getIntersectingPoint(points)
if len(res) == 0:
    print("The two lines are parallel")
else:
    print("The intersection point is (", format(res[0], '0.5f'), ',', format(res[1], '0.5f'), ')')
