# 5.48 (Turtle: draw circles) Write a program that draws 10 circles with centers (0, 0), as
# shown in Figure 5.3b.
import turtle

rad = 60
for i in range(10):
    turtle.penup()
    turtle.goto(0, -rad)
    turtle.pendown()
    turtle.circle(rad)
    rad += 10

turtle.done()
