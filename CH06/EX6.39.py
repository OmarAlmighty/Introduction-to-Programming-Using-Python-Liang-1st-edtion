# 6.39 (Turtle: draw a star) Write a program that draws a star, as shown in Figure 6.11b.
# Use the drawLine function defined in Exercise 6.38.
import turtle


def drawLine(x1, y1, x2, y2, color="black", size=1):
    turtle.color(color)
    turtle.pensize(size)
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)


def main():
    drawLine(10, 50, 110, 50, "blue", 5)
    drawLine(110, 50, 20, 110, "blue", 5)
    drawLine(20, 110, 60, 20, "blue", 5)
    drawLine(60, 20, 100, 110, "blue", 5)
    drawLine(100, 110, 10, 50, "blue", 5)

    turtle.done()


main()
