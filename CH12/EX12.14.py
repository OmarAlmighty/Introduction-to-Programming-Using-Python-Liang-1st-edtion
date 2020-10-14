# 12.14 (Tkinter: Mandelbrot fractal) The Mandelbrot fractal is a well-known image
# created from a Mandelbrot set (see Figure 12.26a). A Mandelbrot set is defined
# using the following iteration:
# Z(n+1) = Z(n)^2 + c
# c is a complex number, and the starting point of the iteration is Z(0) = 0(For
# information on complex numbers, see Exercise 8.21.) For a given c, the iteration
# will produce a sequence of complex numbers: [Z(0), Z(1), ... , Z(n), ... ].It can be
# shown that the sequence either tends to infinity or stays bounded, depending on
# the value of c. For example, if c is 0, the sequence is which is
# bounded. If c is i, the sequence is [0, 0, c], which
# is bounded. If c is the sequence is [0, i, -1 + i, -i, -1 + i, i, ...], which is
# unbounded. It is known that if the absolute value of a complex value in the
# sequence is greater than 2, then the sequence is unbounded. The Mandelbrot set
# consists of the c value such that the sequence is bounded. For example, 0 and i
# are in the Mandelbrot set.
# The count(c) function (lines 23–28) computes Z1,Z2,...,Z60 If none of their
# absolute values exceeds 2, we assume c is in the Mandelbrot set. Of course,
# there could always be an error, but 60 (COUNT_LIMIT) iterations usually are
# enough. Once we find that the sequence is unbounded, the method returns the
# iteration count (line 28). The method returns COUNT_LIMIT if the sequence is
# bounded (line 30).
# The loop in lines 6–20 examines each point (x, y) for -2 < x < 2 and -2 < y < 2
# with interval 0.01 to see if its corresponding complex number c = x + yi
# is in the Mandelbrot set (line 9). If so, paint the point red (line 11).
# If not, set a color that is dependent on its iteration count (line 14). Note that the
# point is painted in a square with width 5 and height 5. All the points are scaled
# and mapped to a grid of 400x400 pixels (lines 17–18).

from tkinter import *  # Import tkinter


# Convert a decimal to a hex as a string
def toHex(decimalValue):
    hex = ""

    while decimalValue != 0:
        hexValue = decimalValue % 16
        hex = toHexChar(hexValue) + hex
        decimalValue = decimalValue // 16

    if len(hex) < 2:
        hex = "0" + hex

    return hex


# Convert an integer to a single hex digit in a character
def toHexChar(hexValue):
    if hexValue <= 9 and hexValue >= 0:
        return chr(hexValue + ord('0'))
    else:  # hexValue <= 15 && hexValue >= 10
        return chr(hexValue - 10 + ord('A'))


COUNT_LIMIT = 60


# Paint a Mandelbrot image in the canvas
def paint():
    x = -2.0
    while x < 2.0:
        y = -2.0
        while y < 2.0:
            c = count(complex(x, y))
            if c == COUNT_LIMIT:
                color = "red"  # c is in a Mandelbrot set
            else:
                color = "#" + toHex(c * 37 % 256) + toHex(
                    c * 58 % 256) + toHex(c * 159 % 256)

            # print(color)
            # Fill a tiny rectangle with the specified color
            canvas.create_rectangle(x * 100 + 200, y * 100 + 200,
                                    x * 100 + 200 + 5, y * 100 + 200 + 5, fill=color)
            y += 0.05
        x += 0.05


# Returns the iteration count
def count(c):
    z = complex(0, 0)  # z0

    for i in range(COUNT_LIMIT):
        z = z * z + c  # Get z1, z2, ...
        if abs(z) > 2: return i  # The sequence is unbounded

    return COUNT_LIMIT  # Indicate a bounded sequence


window = Tk()  # Create a window
window.title("Mandelbrot fractal")  # Set a title

width = 400  # Width of the canvas
height = 400  # Height of the canvas
canvas = Canvas(window, width=width, height=height)
canvas.pack()

Button(window, text="Display", command=paint).pack()

window.mainloop()  # Create an event loop
