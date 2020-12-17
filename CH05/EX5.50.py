# 5.50 (Turtle: display numbers in a triangular pattern) Write a program that displays
# numbers in a triangular pattern, as shown in Figure 5.4b.
import turtle

turtle.penup()
turtle.goto(-170,150)
turtle.pendown()

for i in range(1,11):
    for j in range(1,i+1):
        turtle.write(str(j),font = ("Times", 18, "bold"))
        turtle.penup()
        turtle.forward(30)
        turtle.pendown()
    turtle.penup()
    turtle.goto(-170,turtle.ycor()-40)
    turtle.pendown()

turtle.done()