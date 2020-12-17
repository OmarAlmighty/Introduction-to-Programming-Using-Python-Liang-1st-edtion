# 6.47 (Turtle: two chessboards) Write a program that displays two chessboards, as
# shown in Figure 6.13. Your program should define at least the following function:
# # Draw one chessboard whose upper-left corner is at
# # (startx, starty) and bottom-right corner is at (endx, endy)
# def drawChessboard(startx, endx, starty, endy):

# Draw one chessboard whose upper-left corner is at
# (startx, starty) and bottom-right corner is at (endx, endy)
import math
import turtle

'''
please note that the following code does not work as intended
'''


def drawChessboard(startx, endx, starty, endy):
    turtle.left(0)
    turtle.speed(0)
    turtle.penup()
    turtle.goto(startx, starty)
    turtle.left(45)
    turtle.pendown()
    black = False
    xlen = abs(endx - startx)
    ylen = abs(endy - starty)
    size = (xlen + ylen) // 9
    print(size)
    for i in range(1, 9):
        for j in range(1, 9):
            turtle.begin_fill()
            turtle.circle(30, steps=4)
            if black:
                turtle.color("black")
                black = not black
            else:
                turtle.color("white")
                black = not black

            turtle.end_fill()

            turtle.penup()
            turtle.goto(turtle.xcor() + 42, turtle.ycor())
            turtle.pendown()

        turtle.penup()
        turtle.goto(startx, turtle.ycor() - 42)
        turtle.pendown()
        black = not black

    turtle.penup()
    turtle.left(180)
    turtle.goto(startx - 42, starty + 42)
    turtle.color("gray")
    turtle.pensize(6)
    turtle.pendown()
    turtle.circle(240, steps=4)
    turtle.left(45)


def main():
    drawChessboard(-50, 100, -50, 100)
    turtle.done()


main()
