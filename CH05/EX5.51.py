# 5.51 (Turtle: display a lattice) Write a program that displays an 18-by-18 lattice, as
# shown in Figure 5.4c.
import turtle

turtle.penup()
turtle.goto(-170,150)
turtle.pendown()

for i in range(18):
    turtle.forward(170)
    turtle.penup()
    turtle.goto(-170,turtle.ycor()-10)
    turtle.pendown()

turtle.penup()
turtle.goto(-170,150)
turtle.pendown()
turtle.right(90)

for i in range(18):
    turtle.forward(170)
    turtle.penup()
    turtle.goto(turtle.xcor()+10,150)
    turtle.pendown()

turtle.done()