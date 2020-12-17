# (Turtle: triangle angles) Revise Listing 3.2, ComputeAngles.py, to write a program
# that prompts the user to enter the three points p1, p2, and p3 for a triangle
# and display its angles, as shown in Figure 3.7b.
import math
import turtle

x1, y1, x2, y2, x3, y3 = eval(input("Enter three points: "))

a = math.sqrt((x2 - x3) * (x2 - x3) + (y2 - y3) * (y2 - y3))
b = math.sqrt((x1 - x3) * (x1 - x3) + (y1 - y3) * (y1 - y3))
c = math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))

A = math.degrees(math.acos((a * a - b * b - c * c) / (-2 * b * c)))
B = math.degrees(math.acos((b * b - a * a - c * c) / (-2 * a * c)))
C = math.degrees(math.acos((c * c - b * b - a * a) / (-2 * a * b)))

A = format(A,"0.2f")
B = format(B,"0.2f")
C = format(C,"0.2f")

turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()
turtle.write(str(A))
turtle.goto(x2, y2)
turtle.write(str(B))
turtle.goto(x3, y3)
turtle.write(str(C))
turtle.goto(x1, y1)

turtle.done()
