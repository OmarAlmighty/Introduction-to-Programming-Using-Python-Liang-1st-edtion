# 8.17 (The Point class) Design a class named Point to represent a point with x- and ycoordinates.
# The class contains:
# ■ Two private data fields x and y that represent the coordinates with get methods.
# ■ A constructor that constructs a point with specified coordinates with default
# point (0, 0).
# ■ A method named distance that returns the distance from this point to another
# point of the Point type.
# ■ A method named isNearBy(p1) that returns true if point p1 is close to this
# point. Two points are close if their distance is less than 5.
# ■ Implement the __str__ method to return a string in the form (x, y).
# Draw the UML diagram for the class, and then implement the class. Write a test
# program that prompts the user to enter two points, displays the distance between
# them, and indicates whether they are near each other.
import math


class Point:
    def __init__(self, x=0, y=0):
        self.__x__ = x
        self.__y__ = y

    def getX(self):
        return self.__x__

    def getY(self):
        return self.__y__

    def distance(self, point):
        dis = math.sqrt((self.__x__ - point.getX()) ** 2 + (self.__y__ - point.getY()) ** 2)
        return dis

    def isNearBy(self, point):
        d = self.distance(point)
        return True if d < 5 else False

    def __str__(self):
        return '( ' + str(self.__x__) + ',' + str(self.__y__) + ' )'


def main():
    x1, y1, x2, y2 = eval(input("Enter two points x1, y1, x2, y2: "))
    p1 = Point(x1, y1)
    p2 = Point(x2, y2)
    print("The distance between the two points is", p1.distance(p2))
    if p1.isNearBy(p2):
        print("The two points are near each other")
    else:
        print("The two points are not near each other")

main()