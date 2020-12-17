# 6.44 (Turtle: plot the square function) Simplify the code for Exercise 5.54 by using the
# functions in Listing 6.14.
import turtle


# Draw a line from (x1, y1) to (x2, y2)
def drawLine(x1, y1, x2, y2):
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)

# Write a text at the specified location (x, y)
def writeText(s, x, y):
    turtle.penup() # Pull the pen up
    turtle.goto(x, y)
    turtle.pendown() # Pull the pen down
    turtle.write(s) # Write a string


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
drawLine(-160, 0, 160, 0)

# Draw Y-axis
drawLine(0, -80, 0, 80)

# Display X
writeText("Y", 0, 80)

# Display Y
writeText("X", 180, -15)

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
