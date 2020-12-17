# (Turtle: draw a line) Write a program that prompts the user to enter two points
# and draw a line to connect the points and displays the coordinates of the points,
# as shown in Figure 3.7c.

import turtle

x1, y1, x2, y2 = eval(input("Enter two points: "))

turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()
s = "(" + str(x1) + "," + str(y1) + ")"
turtle.write(s)
turtle.goto(x2, y2)
s = "(" + str(x2) + "," + str(y2) + ")"
turtle.write(s)

turtle.done()