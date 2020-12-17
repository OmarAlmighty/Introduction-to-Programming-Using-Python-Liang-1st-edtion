# 6.37 (Turtle: generate random characters) Use the functions in RandomCharacter
# in Listing 6.11 to display 100 lowercase letters, fifteen per line, as shown in
# Figure 6.11a.
import turtle
from random import randint


def getRandomCharacter(ch1, ch2):
    return chr(randint(ord(ch1), ord(ch2)))


# Generate a random uppercase letter
def getRandomUpperCaseLetter():
    return getRandomCharacter('A', 'Z')


def main():
    turtle.penup()
    turtle.forward(-100)
    turtle.pendown()
    x = turtle.xcor()
    y = turtle.ycor()
    for i in range(100):
        c = getRandomUpperCaseLetter()
        turtle.write(c)
        turtle.penup()
        turtle.forward(30)
        turtle.pendown()
        if (i + 1) % 15 == 0:
            turtle.penup()
            turtle.goto(x, y - 30)
            turtle.pendown()
            x = turtle.xcor()
            y = turtle.ycor()

    turtle.done()


main()
