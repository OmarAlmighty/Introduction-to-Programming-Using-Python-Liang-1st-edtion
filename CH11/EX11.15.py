# 11.15 (Geometry: same line?) Exercise 6.19 gives a function for testing whether three
# points are on the same line. Write the following function to test whether all the
# points in the points list are on the same line:
# def sameLine(points):
# Write a program that prompts the user to enter five points and displays whether
# they are on the same line.

def sameLine(points):
    x0 = points[0]
    y0 = points[1]
    x4 = points[-2]
    y4 = points[-1]
    for i in range(2, len(points) - 1, 2):
        x = points[i]
        y = points[i + 1]
        d = (x - x0) * (y4 - y0) - (x4 - x0) * (y - y0)
        if d != 0:
            return False
    return True


points = input("Enter five points: ").split()
points = [eval(x) for x in points]
if sameLine(points):
    print("The five points are on the same line")
else:
    print("The five points are not on the same line")
