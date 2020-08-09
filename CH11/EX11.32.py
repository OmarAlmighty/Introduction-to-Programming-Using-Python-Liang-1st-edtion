# 11.32 (Geometry: area of a triangle) Write a function that returns the area of a triangle
# using the following header:
# def getTriangleArea(points):
# The points are stored in the 3*2 two-dimensional list points, with
# (points[0][0], points[0][1]) for (x1, y1). The triangle area can be computed
# using the formula in Exercise 2.14. The function returns None if the three
# points are on the same line. Write a program that prompts the user to enter three
# points and displays the area of the triangle.

def main():
    line = input("Enter x1, y1, x2, y2, x3, y3: ").split()
    points = [[eval(line[i]), eval(line[i + 1])] for i in range(0, 6, 2)]

    result = getTriangleArea(points)

    if result == None:
        print("The three points are on the same line")
    else:
        print("The area of the triangle is", result)


def getTriangleArea(points):
    x1, y1, x2, y2, x3, y3 = points[0][0], points[0][1], \
                             points[1][0], points[1][1], points[2][0], points[2][1]

    # Compute the length of the three sides
    side1 = ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) ** 0.5
    side2 = ((x1 - x3) * (x1 - x3) + (y1 - y3) * (y1 - y3)) ** 0.5
    side3 = ((x3 - x2) * (x3 - x2) + (y3 - y2) * (y3 - y2)) ** 0.5

    s = (side1 + side2 + side3) / 2;
    temp = s * (s - side1) * (s - side2) * (s - side3)
    area = temp ** 0.5

    if temp < 0 or temp <= 0.0000000000001:
        return None
    else:
        return area


main()
