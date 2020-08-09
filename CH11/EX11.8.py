# 11.8 (All closest pairs of points) Revise Listing 11.4, FindNearestPoints.py, to find all
# the nearest pairs of points that have the same minimum distance.

def distance(x1, y1, x2, y2):
    return ((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)) ** 0.5


def nearestPoints(points):
    p1, p2 = 0, 1
    short_distance_lst = []
    shortestDistance = distance(points[p1][0], points[p1][1],
                                points[p2][0], points[p2][1])

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            d = distance(points[i][0], points[i][1],
                         points[j][0], points[j][1])

            if shortestDistance > d:
                short_distance_lst.clear()  # new shortest distance, clear other old values
                short_distance_lst.append([i, j])
                shortestDistance = d
            elif shortestDistance == d:
                short_distance_lst.append([i, j])
    return short_distance_lst


numberOfPoints = eval(input("Enter the number of points: "))

points = []
print("Enter", numberOfPoints, "points:", end='')
for i in range(numberOfPoints):
    point = 2 * [0]
    point[0], point[1] = \
        eval(input("Enter coordinates separated by a comma: "))
    points.append(point)

res = nearestPoints(points)
print("The closest two points are:")
for i in res:
    p1 = i[0]
    p2 = i[1]
    print(points[p1], "and", points[p2])
