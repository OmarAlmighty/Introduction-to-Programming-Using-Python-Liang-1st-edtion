# 5.54 (Turtle: plot the square function) Write a program that draws a diagram for the
# function f(x) = x2 (see Figure 5.6a).
import turtle

turtle.speed(0)  # Fastest

# Draw a square function
scaleFactor = 0.01
left = -100
right = 100
x = left
turtle.penup()
turtle.goto(x, scaleFactor * x * x)
turtle.pendown()
for x in range(left, right + 1):
    turtle.goto(x, scaleFactor * x * x)

# Draw X-axis
turtle.penup()
turtle.goto(-160, 0)
turtle.pendown()
turtle.goto(160, 0)

# Draw Y-axis
turtle.penup()
turtle.goto(0, -80)
turtle.pendown()
turtle.goto(0, 80)

# Display X
turtle.penup()
turtle.goto(0, 80)
turtle.pendown()
turtle.write("Y")

# Display Y
turtle.penup()
turtle.goto(180, -15)
turtle.pendown()
turtle.write("X")

# Draw arrows
turtle.degrees()
turtle.penup()
turtle.goto(160, 0)
turtle.pendown()
turtle.setheading(150)
turtle.forward(20)

turtle.penup()
turtle.goto(160, 0)
turtle.pendown()
turtle.setheading(-150)
turtle.forward(20)

turtle.penup()
turtle.goto(0, 80)
turtle.pendown()
turtle.setheading(240)
turtle.forward(20)

turtle.penup()
turtle.goto(0, 80)
turtle.pendown()
turtle.setheading(-60)
turtle.forward(20)

turtle.hideturtle()

turtle.done()
