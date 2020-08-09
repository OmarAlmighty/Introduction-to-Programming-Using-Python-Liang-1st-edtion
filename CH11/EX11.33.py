# 11.33 (Geometry: polygon subareas) A convex four-vertex polygon is divided into four
# triangles, as shown in Figure 11.10.
# Write a program that prompts the user to enter the coordinates of four vertices and
# displays the areas of the four triangles in increasing order.

def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
        print('lines do not intersect')

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    intesct = [x, y]
    return intesct


def getTriangleArea(points):
    x1, y1, x2, y2, x3, y3 = points[0][0], points[0][1], \
                             points[1][0], points[1][1], points[2][0], points[2][1]
    # Compute the length of the three sides
    side1 = ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) ** 0.5
    side2 = ((x1 - x3) * (x1 - x3) + (y1 - y3) * (y1 - y3)) ** 0.5
    side3 = ((x3 - x2) * (x3 - x2) + (y3 - y2) * (y3 - y2)) ** 0.5

    s = (side1 + side2 + side3) / 2
    temp = s * (s - side1) * (s - side2) * (s - side3)
    area = temp ** 0.5

    if temp < 0 or temp <= 0.0000000000001:
        return None
    else:
        return area


x1, y1, x2, y2, x3, y3, x4, y4 = eval(input("Enter x1, y1, x2, y2, x3, y3, x4, y4: "))

points = [[x1, y1], [x2, y2],
          [x3, y3], [x4, y4]]

line1 = [points[0], points[2]]
line2 = [points[1], points[3]]

intersect = line_intersection(line1, line2)

areas = []

x = [[x1, y1], [x2, y2], intersect]
areas.append(getTriangleArea(x))

x = [[x2, y2], [x3, y3], intersect]
areas.append(getTriangleArea(x))

x = [[x3, y3], [x4, y4], intersect]
areas.append(getTriangleArea(x))

x = [[x4, y4], [x1, y1], intersect]
areas.append(getTriangleArea(x))

areas.sort()

for x in areas:
    print(format(x,'0.2f'),end='  ')
