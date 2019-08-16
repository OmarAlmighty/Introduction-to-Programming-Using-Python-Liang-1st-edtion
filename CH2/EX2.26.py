# (Turtle: draw a circle) Write a program that prompts the user to enter the
# center and radius of a circle, and then displays the circle and its area, as shown
# in Figure 2.5.
import turtle

centerX, centerY, rad = eval(input("Enter centerX, centerY, radius: "))
turtle.penup()
turtle.goto(centerX, centerY - 0.5 * rad)
turtle.pendown()
turtle.circle(rad)
turtle.penup()
turtle.goto(centerX+20,centerY+20)
area = 3.14 * rad ** 2
turtle.write(area)

turtle.done()