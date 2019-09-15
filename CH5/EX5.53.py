# 5.53 (Turtle: plot the sine and cosine functions) Write a program that plots the sine
# function in red and cosine in blue, as shown in Figure 5.5b.
import math
import turtle

turtle.speed(0) # Fastest

# Draw X-axis
turtle.penup()
turtle.goto(-220, 0)
turtle.pendown()

turtle.goto(220, 0)

# Draw arrows
turtle.degrees()
turtle.setheading(150)
turtle.forward(20)

turtle.penup()
turtle.goto(220, 0)
turtle.pendown()
turtle.setheading(-150)
turtle.forward(20)

# Draw Y-axis
turtle.penup()
turtle.goto(0, -80)
turtle.pendown()
turtle.goto(0, 80)

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

# Draw sine function
x = -175
turtle.penup()
turtle.goto(x, 50 * math.sin((x / 100.0) * 2 * math.pi))
turtle.pendown()

for x in range(-175, 176):
    turtle.goto(x, 50 * math.sin((x / 100.0) * 2 * math.pi))

turtle.penup()
turtle.goto(x, 50 * math.cos((x / 100.0) * 2 * math.pi))
turtle.pendown()

for x in range(-175, 176):
    turtle.goto(x, 50 * math.cos((x / 100.0) * 2 * math.pi))

turtle.penup()
turtle.goto(-100, -15)
turtle.pendown()
turtle.write("-2\u03c0")

turtle.penup()
turtle.goto(100, -15)
turtle.pendown()
turtle.write("2\u03c0")

turtle.hideturtle()

turtle.done()