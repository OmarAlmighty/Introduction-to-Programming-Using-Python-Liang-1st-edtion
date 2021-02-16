# 15.34 (Turtle: Hilbert curve) Rewrite the Hilbert curve in Exercise 15.33 using Turtle,
# as shown in Figure 15.20. Your program should prompt the user to enter the
# order and display the corresponding fractal for the order.

import turtle

def upperU(order):
    if order > 0:
        leftU(order - 1)
        turtle.setheading(270)
        turtle.forward(length)
        upperU(order - 1)
        turtle.setheading(0)
        turtle.forward(length)
        upperU(order - 1)
        turtle.setheading(90)
        turtle.forward(length)
        rightU(order - 1)


def leftU(order):
    if order > 0:
        upperU(order - 1)
        turtle.setheading(0)
        turtle.forward(length)
        leftU(order - 1)
        turtle.setheading(270)
        turtle.forward(length)
        leftU(order - 1)
        turtle.setheading(180)
        turtle.forward(length)
        downU(order - 1)


def rightU(order):
    if order > 0:
        downU(order - 1)
        turtle.setheading(180)
        turtle.forward(length)
        rightU(order - 1)
        turtle.setheading(90)
        turtle.forward(length)
        rightU(order - 1)
        turtle.setheading(0)
        turtle.forward(length)
        upperU(order - 1)


def downU(order):
    if order > 0:
        rightU(order - 1)
        turtle.setheading(90)
        turtle.forward(length)
        downU(order - 1)
        turtle.setheading(180)
        turtle.forward(length)
        downU(order - 1)
        turtle.setheading(270)
        turtle.forward(length)
        leftU(order - 1)


order = eval(input("Enter an order: "))

SIZE = 400
length = 400

for i in range(order):
    length = length / 2  # Get the right length for the order

# Get the start point
x = -SIZE / 2 + length / 2
y = SIZE / 2 - length / 2

turtle.penup()
turtle.goto(x, y)
turtle.pendown()

upperU(order)
turtle.done()
