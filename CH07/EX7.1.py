# 7.1 (The Rectangle class) Following the example of the Circle class in Section
# 7.2, design a class named Rectangle to represent a rectangle. The class
# contains:
# ■ Two data fields named width and height.
# ■ A constructor that creates a rectangle with the specified width and height.
# The default values are 1 and 2 for the width and height, respectively.
# ■ A method named getArea() that returns the area of this rectangle.
# ■ A method named getPerimeter() that returns the perimeter.
# Draw the UML diagram for the class, and then implement the class. Write a test
# program that creates two Rectangle objects—one with width 4 and height 40
# and the other with width 3.5 and height 35.7. Display the width, height, area,
# and perimeter of each rectangle in this order.
from CH7.Rectangle import Rectangle

rect1 = Rectangle(4, 40)
rect2 = Rectangle(3.5, 35.7)
area1 = rect1.getArea()
area2 = rect2.getArea()
per1 = rect1.getPerimeter()
per2 = rect2.getPerimeter()

print("Rectangle1:\n\tWidth =", rect1.width, "\n\tHeight =", rect1.height,
      "\n\tArea =", area1, "\n\tPerimeter =", per1)

print("Rectangle2:\n\tWidth =", rect2.width, "\n\tHeight =", rect2.height,
      "\n\tArea =", area2, "\n\tPerimeter =", per2)
