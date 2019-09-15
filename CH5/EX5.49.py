# 5.49 (Turtle: display a multiplication table) Write a program that displays a multiplication
# table, as shown in Figure 5.4a.
import turtle

turtle.penup()
turtle.goto(-140,180)
turtle.pendown()
turtle.write("Multiplication Table",font=("Arial", 20, "normal"))
turtle.penup()
turtle.goto(-140,130)
turtle.pendown()

for i in range(1,10):
    turtle.write(str(i),font=("Arial", 18, "normal"))
    turtle.penup()
    turtle.goto(turtle.xcor()+45,130)
    turtle.pendown()

turtle.penup()
turtle.goto(-170,110)
turtle.pendown()
turtle.write("-----------------------------------------",font=("Arial", 20, "normal"))

turtle.penup()
turtle.goto(-170,90)
turtle.pendown()

for i in range(1,10):
    turtle.write(str(i)+"|", font=("Arial", 18, "normal"))
    turtle.penup()
    turtle.goto(-170,turtle.ycor()-45)
    turtle.pendown()

turtle.penup()
turtle.goto(-140,90)
turtle.pendown()

for i in range(1,10):
    for j in range(1,10):
        turtle.write(str(i*j),font=("Arial", 18, "normal"))
        turtle.penup()
        turtle.goto(turtle.xcor()+45,turtle.ycor())
        turtle.pendown()
    turtle.penup()
    turtle.goto(-140,turtle.ycor()-45)
    turtle.pendown()

turtle.done()