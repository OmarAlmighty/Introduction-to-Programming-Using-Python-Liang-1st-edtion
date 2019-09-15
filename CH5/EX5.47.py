# 5.47 (Turtle: draw random balls) Write a program that displays 10 random balls in
# a rectangle with width 120 and height 100, centered at (0, 0), as shown in
# Figure 5.3a.
import random
import turtle

WIDTH = 120
HEIGHT = 100
count = 0
turtle.penup()
turtle.goto(0 - WIDTH / 2, 0 - HEIGHT / 2)
turtle.pendown()

for i in range(4):
    if i % 2 == 0:
        turtle.forward(WIDTH)

    else:
        turtle.forward(HEIGHT)
    turtle.left(90)

while count < 10:
    turtle.penup()
    x = random.randint(-WIDTH / 2, WIDTH / 2)
    y = random.randint(-HEIGHT / 2, HEIGHT / 2)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.dot(5, "red")
    count += 1

turtle.ht()  # Same as turtle.hideturtle()
turtle.done()
