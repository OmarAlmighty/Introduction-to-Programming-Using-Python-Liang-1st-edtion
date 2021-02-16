# 15.36 (Turtle: Sierpinski triangle) Rewrite Listing 15.9, SierpinskiTriangle.py, using
# Turtle.

import turtle
import math


# Draw a Sierpinski triangle with the specified order
def displayTriangles(order, p1, p2, p3):
    if order == 0:  # Base condition
        # Draw a triangle to connect three points
        drawLine(p1, p2)
        drawLine(p2, p3)
        drawLine(p3, p1)
    else:
        # Get the midpoint on each edge in the triangle
        p12 = midpoint(p1, p2)
        p23 = midpoint(p2, p3)
        p31 = midpoint(p3, p1)

        # Recursively display three triangles
        displayTriangles(order - 1, p1, p12, p31)
        displayTriangles(order - 1, p12, p2, p23)
        displayTriangles(order - 1, p31, p23, p3)


# Draw a line between two points p1 and p2
def drawLine(p1, p2):
    # Compute the distance between p1 and p2
    d = distance(p1[0], p1[1], p2[0], p2[1])

    if p1[0] <= p2[0]:  # p2 is on the right of p1
        angle = math.asin((p2[1] - p1[1]) / d)
    else:
        angle = -math.asin((p2[1] - p1[1]) / d) + math.pi

    turtle.radians()
    turtle.setheading(angle)
    turtle.penup()
    turtle.goto(p1[0], p1[1])
    turtle.pendown()
    turtle.forward(d)
    turtle.setheading(0)


# Return the distance between two points
def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))


# Return the midpoint between two points
def midpoint(p1, p2):
    p = 2 * [0]
    p[0] = (p1[0] + p2[0]) / 2
    p[1] = (p1[1] + p2[1]) / 2
    return p


def main():
    p1 = [0, 125]
    p2 = [-150, -125]
    p3 = [150, -125]

    order = eval(input("Enter an order: "))
    displayTriangles(order, p1, p2, p3)

    turtle.done()


main()
