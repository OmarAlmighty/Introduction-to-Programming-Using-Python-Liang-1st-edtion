# 6.46 (Turtle: connect all points in a hexagon) Write a program that displays a hexagon
# with all the points connected, as shown in Figure 6.12b.
import math
import turtle


# Draw a line from (x1, y1) to (x2, y2)
def drawLine(x1, y1, x2, y2):
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)


def drawPolygon(x=0, y=0, radius=50, numberOfSides=3):
    angle = 2 * math.pi / numberOfSides

    # Connect points for the polygon
    for i in range(numberOfSides + 1):
        for j in range(numberOfSides + 1):
            drawLine(x + radius * math.cos(i * angle),
                     y - radius * math.sin(i * angle),
                     x + radius * math.cos(j * angle),
                     y - radius * math.sin(j * angle))


turtle.speed(0)  # Fastest

drawPolygon(0, 0, 50, 6)

turtle.hideturtle()

turtle.done()
