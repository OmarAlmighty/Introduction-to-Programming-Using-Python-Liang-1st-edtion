# 10.34 (Turtle: draw histograms) Rewrite the preceding program using Turtle.
import random
import turtle


def drawHistogram(list):
    WIDTH = 600  # Width of the histogram
    HEIGHT = 300  # Height of the histogram

    # Draw a base line
    turtle.penup()
    turtle.goto(-WIDTH / 2, -HEIGHT / 2)
    turtle.pendown()
    turtle.forward(WIDTH)

    widthOfBar = WIDTH / len(list)  # Width of each bar

    for i in range(len(list)):
        height = list[i] * HEIGHT / max(list)
        drawABar(-WIDTH / 2 + i * widthOfBar + 10,
                 -HEIGHT / 2, widthOfBar - 5, height)
        drawAString(-WIDTH / 2 + i * widthOfBar + 18,
                    -HEIGHT / 2 - 15, chr(i + ord('a')))

    turtle.hideturtle()


def drawABar(i, j, widthOfBar, height):
    turtle.penup()
    turtle.goto(i, j)
    turtle.setheading(90)  # Set orientation to north
    turtle.pendown()

    turtle.forward(height)  # Draw a vertical line
    turtle.right(90)  # Turn right 90 degrees
    turtle.forward(widthOfBar)  # Draw a horizontal line
    turtle.right(90)  # Turn right 90 degrees
    turtle.forward(height)  # Draw a vertical line


def drawAString(i, j, ch):
    turtle.penup()
    turtle.goto(i, j)
    turtle.setheading(90)  # Set orientation to north
    turtle.pendown()

    turtle.write(ch)


counts = [0] * 26
for i in range(1000):
    c = random.randint(0, 25)
    counts[c] += 1

drawHistogram(counts)

turtle.done()
