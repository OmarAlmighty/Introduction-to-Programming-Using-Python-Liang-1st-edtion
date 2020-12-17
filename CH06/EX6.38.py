# 6.38 (Turtle: draw a line) Write the following function that draws a line from point
# (x1, y1) to (x2, y2) with color (default to black) and line size (default to 1).
# def drawLine(x1, y1, x2, y2, color = "black", size = 1):
import turtle


def drawLine(x1, y1, x2, y2, color="black", size=1):
    turtle.color(color)
    turtle.pensize(size)
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)


def main():
    drawLine(10, 20, 70, 90, "blue", 5)
    drawLine(40, 20, -70, 50, "yellow", 8)
    turtle.done()

main()