# 6.45 (Turtle: draw a regular polygon) Write the following function to draw a regular
# polygon:
# def drawPolygon(x = 0, y = 0, radius = 50, numberOfSides = 3):
# The polygon is centered at (x, y) with a specified radius for the bounding circle for
# the polygon and the number of sides. Write a test program that displays a triangle,
# square, pentagon, hexagon, heptagon, and octagon, as shown in Figure 6.12a.
import turtle


def drawPolygon(x=0, y=0, radius=50, numberOfSides=3):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(radius, steps=numberOfSides)


def main():
    drawPolygon(-200,50)  # Triangle
    drawPolygon(-100, 50, numberOfSides=4)  # Square
    drawPolygon(0, 50, numberOfSides=5)  # Pentagon
    drawPolygon(100, 50, numberOfSides=6)  # hexagon
    drawPolygon(200, 50, numberOfSides=7)  # heptagon
    drawPolygon(300, 50, numberOfSides=8)  # octagon
    turtle.done()


main()
