# 4.23 (Geometry: point in a rectangle?) Write a program that prompts the user to enter
# a point (x, y) and checks whether the point is within the rectangle centered at
# (0, 0) with width 10 and height 5. For example, (2, 2) is inside the rectangle and
# (6, 4) is outside the rectangle, as shown in Figure 4.8b. (Hint: A point is in the
# rectangle if its horizontal distance to (0, 0) is less than or equal to 10 / 2 and
# its vertical distance to (0, 0) is less than or equal to 5.0 / 2. Test your program
# to cover all cases.)
import math

HEIGHT = 5
WIDTH = 10
X = Y = 0
x, y = eval(input("Enter a point with two coordinates: "))

distance = math.sqrt((x - X) ** 2 + (y - Y) ** 2)

if WIDTH >= distance >= -WIDTH and HEIGHT >= distance >= -HEIGHT:
    print("Point (", format(x, "0.1f"), ",", format(y, "0.1f"), ")", "is in the rectangle")
else:
    print("Point (", format(x, "0.1f"), ",", format(y, "0.1f"), ")", "is not in the rectangle")

