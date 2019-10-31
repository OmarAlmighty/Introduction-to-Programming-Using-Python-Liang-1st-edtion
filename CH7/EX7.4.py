# (The Fan class) Design a class named Fan to represent a fan. The class contains:
# ■ Three constants named SLOW, MEDIUM, and FAST with the values 1, 2, and 3 to
# denote the fan speed.
# ■ A private int data field named speed that specifies the speed of the fan.
# ■ A private bool data field named on that specifies whether the fan is on (the
# default is False).
# ■ A private float data field named radius that specifies the radius of the fan.
# ■ A private string data field named color that specifies the color of the fan.
# ■ The accessor and mutator methods for all four data fields.
# ■ A constructor that creates a fan with the specified speed (default SLOW), radius
# (default 5), color (default blue), and on (default False).
# Draw the UML diagram for the class and then implement the class. Write a test
# program that creates two Fan objects. For the first object, assign the maximum
# speed, radius 10, color yellow, and turn it on. Assign medium speed, radius 5,
# color blue, and turn it off for the second object. Display each object’s speed,
# radius, color, and on properties.
from CH7.Fan import Fan

f1 = Fan(Fan.FAST, 10, "Yellow", True)
f2 = Fan(Fan.MEDIUM, 5, "Blue", False)

print("Fan1:\n", "\tSpeed:", f1.getSpeed(), "\n\tRadius:", f1.getRadius(),
      "\n\tColor:", f1.getColor(), "\n\tIs on:", f1.isOn(), "\n")
print("Fan2:\n", "\tSpeed:", f2.getSpeed(), "\n\tRadius:", f2.getRadius(),
      "\n\tColor:", f2.getColor(), "\n\tIs on:", f2.isOn(), "\n")
