# 15.30 (Turtle: H-tree fractal) Rewrite the H-tree fractal in Exercise 15.29 using Turtle,
# as shown in Figure 15.16. Your program should prompt the user to enter the
# order and display the corresponding fractal for the order.

import turtle


# Draw H shapes with the specified order
def displayHShape(order, center, length):
    if order >= 0:
        p1 = [center[0] - length / 2, center[1] + length / 2]
        p2 = [center[0] - length / 2, center[1] - length / 2]
        p3 = [center[0] + length / 2, center[1] + length / 2]
        p4 = [center[0] + length / 2, center[1] - length / 2]

        # Draw an H shape
        drawLine(center[0] - length / 2, center[1],
                 center[0] + length / 2, center[1])
        drawLine(p1[0], p1[1], p2[0], p2[1])
        drawLine(p3[0], p3[1], p4[0], p4[1])

        # Recursively display three H shape of a smaller order
        displayHShape(order - 1, p1, length / 2)
        displayHShape(order - 1, p2, length / 2)
        displayHShape(order - 1, p3, length / 2)
        displayHShape(order - 1, p4, length / 2)


def drawLine(x1, y1, x2, y2):
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)


def main():
    order = eval(input("Enter an order: "))
    length = eval(input("Enter the length of a side: "))
    displayHShape(order, [0, 0], length)

    turtle.done()


main()
