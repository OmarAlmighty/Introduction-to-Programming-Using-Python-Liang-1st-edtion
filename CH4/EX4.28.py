# 4.28 (Geometry: two rectangles) Write a program that prompts the user to enter the
# center x-, y-coordinates, width, and height of two rectangles and determines
# whether the second rectangle is inside the first or overlaps with the first, as shown
# in Figure 4.10. Test your program to cover all cases.

x1, y1, w1, h1 = eval(input("Enter r1's center x-, y-coordinates, width, and height: "))
x2, y2, w2, h2 = eval(input("Enter r2's center x-, y-coordinates, width, and height: "))

xDistance = x1 - x2 if x1 - x2 >= 0 else x2 - x1
yDistance = y1 - y2 if y1 - y2 >= 0 else y2 - y1

if xDistance <= (w1 - w2) / 2 and yDistance <= (h1 - h2) / 2:
    print("r2 is inside r1")
elif xDistance <= (w1 + w2) / 2 and yDistance <= (h1 + h2) / 2:
    print("r2 overlaps r1")
else:
    print("r2 does not overlap r1")
