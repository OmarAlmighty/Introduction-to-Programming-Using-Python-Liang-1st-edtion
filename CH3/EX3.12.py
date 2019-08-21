# (Turtle: draw a star) Write a program that prompts the user to enter the length of
# the star and draw a star, as shown in Figure 3.5a. (Hint: The inner angle of each
# point in the star is 36 degrees.)
import turtle

l = eval(input("Enter length: "))

turtle.forward(l)
turtle.right(144)

turtle.forward(l)
turtle.right(144)

turtle.forward(l)
turtle.right(144)

turtle.forward(l)
turtle.right(144)

turtle.forward(l)
turtle.right(144)

turtle.done()
