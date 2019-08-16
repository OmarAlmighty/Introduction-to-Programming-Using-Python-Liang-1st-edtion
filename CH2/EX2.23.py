# (Turtle: draw four circles) Write a program that prompts the user to enter the
# radius and draws four circles in the center of the screen, as shown in Figure 2.4a.
import turtle

radius = eval(input("Enter radius: "))
turtle.penup()
turtle.goto(-radius / 2, -radius * 2 + radius)
turtle.pendown()
turtle.circle(radius)

turtle.penup()
turtle.goto(-radius / 2, -radius * 4 + radius)
turtle.pendown()
turtle.circle(radius)

turtle.penup()
turtle.goto(-radius * 2.5, -radius * 2 + radius)
turtle.pendown()
turtle.circle(radius)

turtle.penup()
turtle.goto(-radius * 2.5, -radius * 4 + radius)
turtle.pendown()
turtle.circle(radius)

turtle.done()  # pause turtle window
