# 4.38 (Geometry: two rectangles) Write a program that prompts the user to enter the
# center x-, y-coordinates, width, and height of two rectangles and determines
# whether the second rectangle is inside the first or overlaps with the first, as shown
# in Figure 4.15.
import turtle

x1, y1, w1, h1 = eval(input("Enter r1's center x-, y-coordinates, width, and height: "))
x2, y2, w2, h2 = eval(input("Enter r2's center x-, y-coordinates, width, and height: "))

# Draw first rectangle
turtle.penup()
turtle.goto(x1 - w1, y1 - h1)
turtle.pendown()
turtle.forward(w1)
turtle.left(90)
turtle.forward(h1)
turtle.left(90)
turtle.forward(w1)
turtle.left(90)
turtle.forward(h1)

# Draw second rectangle
turtle.penup()
turtle.left(90)
turtle.goto(x2 - w2, y2 - h2)
turtle.pendown()
turtle.forward(w2)
turtle.left(90)
turtle.forward(h2)
turtle.left(90)
turtle.forward(w2)
turtle.left(90)
turtle.forward(h2)

xDistance = x1 - x2 if x1 - x2 >= 0 else x2 - x1
yDistance = y1 - y2 if y1 - y2 >= 0 else y2 - y1

turtle.penup()
turtle.goto(max(x1, x2), max(y1, y2))
turtle.pendown
if xDistance <= (w1 - w2) / 2 and yDistance <= (h1 - h2) / 2:
    turtle.write("r2 is inside r1", font=("Arial", 16, "bold"))
elif xDistance <= (w1 + w2) / 2 and yDistance <= (h1 + h2) / 2:
    turtle.write("r2 overlaps r1", font=("Arial", 16, "bold"))
else:
    turtle.write("r2 does not overlap r1", font=("Arial", 16, "bold"))

turtle.hideturtle()
turtle.done()
