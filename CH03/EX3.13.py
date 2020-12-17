# (Turtle: display a STOP sign) Write a program that displays a STOP sign, as
# shown in Figure 3.5b. The hexagon is in red and the text is in white

import turtle

turtle.begin_fill()
turtle.left(90)
turtle.circle(100, steps=6)
turtle.color("red")
turtle.end_fill()
turtle.color("white")
turtle.penup()
turtle.goto(turtle.xcor() - 140, turtle.ycor() - 15)
turtle.pendown()
turtle.write("STOP", font=("Arial", 20, "normal"))
turtle.hideturtle()

turtle.done()
