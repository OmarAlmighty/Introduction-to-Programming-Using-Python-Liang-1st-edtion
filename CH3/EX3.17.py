# (Turtle: triangle area) Write a program that prompts the user to enter the three
# points p1, p2, and p3 for a triangle and display its area below the triangle, as
# shown in Figure 3.7a. The formula for computing the area of a triangle is given
# in Exercise 2.14.

import turtle

x1, y1, x2, y2, x3, y3 = eval(input("Enter three points for a triangle: "))

side1 = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
side2 = ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5
side3 = ((x2 - x3) ** 2 + (y2 - y3) ** 2) ** 0.5
s = (side1 + side2 + side3) / 2
area = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5

turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()
s = "p1 (" + str(x1) + ":" + str(y1) + ")"
turtle.write(s)
turtle.goto(x2, y2)
s = "p2 (" + str(x2) + ":" + str(y2) + ")"
turtle.write(s)
turtle.goto(x3, y3)
s = "p3 (" + str(x3) + ":" + str(y3) + ")"
turtle.write(s)
turtle.goto(x1, y1)

turtle.penup()
turtle.goto(x2, y2 - 20)
turtle.write("The area is " + str(area))
turtle.done()
