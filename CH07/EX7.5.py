# 7.5 (Geometry: n-sided regular polygon) An n-sided regular polygon’s sides all have
# the same length and all of its angles have the same degree (i.e., the polygon is
# both equilateral and equiangular). Design a class named RegularPolygon that
# contains:
# ■ A private int data field named n that defines the number of sides in the polygon.
# ■ A private float data field named side that stores the length of the side.
# ■ A private float data field named x that defines the x-coordinate of the center of
# the polygon with default value 0.
# ■ A private float data field named y that defines the y-coordinate of the center of
# the polygon with default value 0.
# ■ A constructor that creates a regular polygon with the specified n (default 3),
# side (default 1), x (default 0), and y (default 0).
# ■ The accessor and mutator methods for all data fields.
# ■ The method getPerimeter() that returns the perimeter of the polygon.
# ■ The method getArea() that returns the area of the polygon. The formula for
# computing the area of a regular polygon is
# Draw the UML diagram for the class, and then implement the class. Write a test program
# that creates three RegularPolygon objects, created using RegularPolygon(),
# using RegularPolygon(6, 4) and RegularPolygon(10, 4, 5.6, 7.8). For
# each object, display its perimeter and area.
from CH7.RegularPolygon import RegularPolygon

p1 = RegularPolygon()
p2 = RegularPolygon(6, 4)
p3 = RegularPolygon(10, 4, 5.6, 7.8)
print("Regular Polygon1:\n", "\tArea:", p1.getArea(), "\n\tPerimeter:", p1.getPerimeter(), "\n")
print("Regular Polygon2:\n", "\tArea:", p2.getArea(), "\n\tPerimeter:", p2.getPerimeter(), "\n")
print("Regular Polygon3:\n", "\tArea:", p3.getArea(), "\n\tPerimeter:", p3.getPerimeter(), "\n")
