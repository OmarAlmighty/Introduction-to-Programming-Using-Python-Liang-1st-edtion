# 6.42 (Turtle: plot the sine function) Simplify the code for Exercise 5.52 by using the
# functions in Listing 6.14.
import math
import turtle


# Draw a line from (x1, y1) to (x2, y2)
def drawLine(x1, y1, x2, y2):
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)


# Write a text at the specified location (x, y)
def writeText(s, x, y):
    turtle.penup()  # Pull the pen up
    turtle.goto(x, y)
    turtle.pendown()  # Pull the pen down
    turtle.write(s)  # Write a string


turtle.speed(0)  # Fastest

# Draw X-axis
drawLine(-220, 0, 220, 0)

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
drawLine(0, -80, 0, 80)

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

writeText("-2\u03c0", -100, -15)
writeText("2\u03c0", 100, -15)

turtle.hideturtle()

turtle.done()
