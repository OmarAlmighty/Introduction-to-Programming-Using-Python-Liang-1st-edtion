# 4.22 (Geometry: point in a circle?) Write a program that prompts the user to enter a
# point (x, y) and checks whether the point is within the circle centered at (0, 0) with
# radius 10. For example, (4, 5) is inside the circle and (9, 9) is outside the circle, as
# shown in Figure 4.8a.
# (Hint: A point is in the circle if its distance to (0, 0) is less than or equal to 10. The
# formula for computing the distance is Test your
# program to cover all cases.) Two sample runs are shown next.
import math
RADIUS = 10
X = Y = 0
x, y = eval(input("Enter a point with two coordinates: "))

distance = math.sqrt((x - X) ** 2 + (y - Y) ** 2)

if RADIUS >= distance >= -RADIUS:
    print("Point (", format(x, "0.1f"), ",", format(y, "0.1f"), ")", "is in the circle")
else:
    print("Point (", format(x, "0.1f"), ",", format(y, "0.1f"), ")", "is not in the circle")
