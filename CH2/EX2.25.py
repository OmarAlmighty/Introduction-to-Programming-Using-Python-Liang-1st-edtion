# (Turtle: draw a rectangle) Write a program that prompts the user to enter the
# center of a rectangle, width, and height, and displays the rectangle, as shown in
# Figure 2.4c.
import turtle

centerX, centerY, w, h = eval(input("Enter centerX,centerY, width, height: "))

turtle.penup()
turtle.goto(centerX - 0.5 * w, centerY + 0.5 * h)
turtle.pendown()
turtle.forward(w)
turtle.right(90)
turtle.forward(h)
turtle.right(90)
turtle.forward(w)
turtle.right(90)
turtle.forward(h)

turtle.done()  # pause window
