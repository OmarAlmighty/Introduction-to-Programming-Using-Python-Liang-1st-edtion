# (Turtle: draw the Olympic symbol ) Write a program that prompts the user to
# enter the radius of the rings and draws an Olympic symbol of five rings of the
# same size with the colors blue, black, red, yellow, and green, as shown in
# Figure 3.5c.
import turtle as t

r = eval(input("Enetr radius: "))
t.speed(10)
x = t.xcor()

t.penup()
t.backward(200)
t.pendown()
t.pensize(15)

t.color("blue")
t.circle(r)

t.penup()
t.forward(x + r * 2.5)
t.pendown()

t.color("black")
t.circle(r)

t.penup()
t.forward(x + r * 2.5)
t.pendown()

t.color("red")
t.circle(r)

t.penup()
t.backward(x + r * 4.75)
t.left(-90)
t.forward(x + 20)
t.pendown()

t.color("yellow")
t.circle(r)

t.penup()
t.left(90)
t.forward(x + r * 2.5)
t.left(-90)
t.forward(x)
t.pendown()

t.color("green")
t.circle(r)
t.done()
