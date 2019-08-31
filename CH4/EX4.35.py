# 4.35 (Turtle: point position) Write a program that prompts the user to enter the x- and
# y-coordinates for the three points p0+ p1+ and p2+ and displays a message to
# indicate whether p2 is on the left side+ the right side+ or on the line from p0 to p1+
# as shown in Figure 4.13. See Exercise 4.31 for determining the point position.
import turtle

x0, y0, x1, y1, x2, y2 = eval(input("Enter coordinates for the three points p0, p1, and p2: "))

d = (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)

turtle.penup()
turtle.goto(x0, y0)
turtle.pendown()
turtle.write("p0 (" + str(x0) + "," + str(y0) + ")")

turtle.goto(x1, y1)
turtle.write("p1 (" + str(x1) + "," + str(y1) + ")")

turtle.penup()
turtle.goto(x2, y2)
turtle.pendown()
turtle.dot(10)

turtle.penup()
turtle.goto(x2, y2 - 3)
turtle.pendown()
if d > 0:
    turtle.write("p2 is on the left side of the line from p0 to p1")
elif d == 0:
    turtle.write("p2 is on the same line from p0 to p1")
else:
    turtle.write("p2 is on the right side of the line from p0 to p1")

turtle.hideturtle()
turtle.done()
