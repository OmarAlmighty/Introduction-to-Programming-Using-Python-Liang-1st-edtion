# 6.40 (Turtle: filled rectangle and circle) Write the following functions that fill a rectangle
# with the specified color, center, width, and height, and a circle with the specified
# color, center, and radius.
# # Fill a rectangle
# def drawRectangle(color = "black",
# x = 0, y = 0, width = 30, height = 30):
# # Fill a circle
# def drawCircle(color = "black", x = 0, y = 0, radius = 50):
# Fill a rectangle
import turtle


def drawRectangle(color="black", x=0, y=0, width=30, height=30):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color(color)
    for i in range(4):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
    turtle.end_fill()


# Fill a circle
def drawCircle(color="black", x=0, y=0, radius=50):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color(color)
    turtle.circle(radius)
    turtle.end_fill()


def main():
    drawRectangle("Blue", 60, 60, 100, 200)
    drawCircle()
    turtle.done()

main()