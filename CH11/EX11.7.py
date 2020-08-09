# 11.7 (Points nearest to each other) The program in Listing 11.3 finds the two points in a
# two-dimensional space nearest to each other. Revise the program so that it finds the
# two points in a three-dimensional space nearest to each other. Use a two-dimensional
# list to represent the points. Test the program using the following points:
# points = [[-1, 0, 3], [-1, -1, -1], [4, 1, 1],
# [2, 0.5, 9], [3.5, 2, -1], [3, 1.5, 3], [-1.5, 4, 2],
# [5.5, 4, -0.5]]
# The formula for computing the distance between two points (x1, y1, z1)
# and (x2, y2, z2) in a three-dimensional space is
import math


def distance(p1, p2):
    x1 = p1[0]
    y1 = p1[1]
    z1 = p1[2]
    x2 = p2[0]
    y2 = p2[1]
    z2 = p2[2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def nearestPoints(points):
    p1, p2 = 0, 1
    shortestDistance = distance(points[p1], points[p2])

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            d = distance(points[i], points[j])

            if shortestDistance > d:
                p1, p2 = i, j
                shortestDistance = d

    return p1, p2


points = [[-1, 0, 3], [-1, -1, -1], [4, 1, 1],
          [2, 0.5, 9], [3.5, 2, -1], [3, 1.5, 3], [-1.5, 4, 2],
          [5.5, 4, -0.5]]

p1, p2 = nearestPoints(points)
print("The closest two points are (" +
      str(points[p1][0]) + ", " + str(points[p1][1]) + ", " + str(points[p1][2]) + ") and (" +
      str(points[p2][0]) + ", " + str(points[p2][1]) + ", " + str(points[p2][2]) + ")")
