# 10.32 (Turtle: draw a line) Write the following function that draws a line from point
# p1 ([x1, y1]) to point p2 ([x2, y2]).
# # Draw a line
# def drawLine(p1, p2):
import math
import turtle


def drawLine(p1, p2):
    d = math.sqrt((p2[0] - p1[0]) * (p2[0] - p1[0]) + (p2[1] - p1[1]) * (p2[1] - p1[1]))

    turtle.penup()
    turtle.penup()
    turtle.goto(p1[0], p1[1])
    turtle.pendown()
    turtle.forward(d)
    turtle.done()

drawLine([120, 80], [60, 20])

