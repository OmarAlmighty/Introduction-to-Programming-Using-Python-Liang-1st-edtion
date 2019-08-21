# (Turtle: paint a smiley face) Write a program that paints a smiley face, as shown in
# Figure 3.6a.
import turtle

turtle.circle(100)  # face

# smile
turtle.penup()
turtle.left(90)
turtle.forward(30)
turtle.right(60)
turtle.pendown()
turtle.forward(80)
turtle.backward(80)
turtle.left(120)
turtle.forward(80)
turtle.backward(80)

# nose
turtle.penup()
turtle.setheading(90)
turtle.forward(110)
turtle.pendown()
turtle.right(145)
turtle.forward(80)
turtle.backward(80)
turtle.right(70)
turtle.forward(80)
turtle.backward(80)

# right eye
turtle.penup()
turtle.setheading(0)
turtle.forward(40)
turtle.setheading(90)
turtle.forward(20)
turtle.pendown()
turtle.dot(35)

# left eye
turtle.penup()
turtle.setheading(180)
turtle.forward(80)
turtle.pendown()
turtle.dot(35)

turtle.done()
