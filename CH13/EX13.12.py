# 13.12 (The TriangleError class) Define an exception class named TriangleError
# that extends RuntimeError. The TriangleError class contains the private
# data fields side1, side2, and side3 with accessor methods for the three
# sides of a triangle. Modify the Triangle class in Exercise 12.1 to throw a
# TriangleError exception if the three given sides cannot form a triangle.

import math


class TriangleError(RuntimeError):
    def __init__(self, side1, side2, side3):
        super().__init__()
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3

    def getSide1(self):
        return self.__side1

    def getSide2(self):
        return self.__side2

    def getSide3(self):
        return self.__side3


class GeometricObject:
    def __init__(self, color="green", filled=True):
        self.__color = color
        self.__filled = filled

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

    def isFilled(self):
        return self.__filled

    def setFilled(self, filled):
        self.__filled = filled

    def __str__(self):
        return "color: " + self.__color + \
               " and filled: " + str(self.__filled)


class Triangle(GeometricObject):
    def __init__(self, side1=1.0, side2=1.0, side3=1.0, color="green", isFilld=True):
        super().__init__(color, isFilld)
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3
        if not self.isLegal():
            raise TriangleError(side1, side2, side3)

    def isLegal(self):
        return self.__side1 + self.__side2 > self.__side3 and \
            self.__side2 + self.__side3 > self.__side1 and \
            self.__side1 + self.__side3 > self.__side2

    def getSide1(self):
        return self.side1

    def setSide1(self, side1):
        self.side1 = side1

    def getSide2(self):
        return self.side2

    def setSide2(self, side2):
        self.side2 = side2

    def getSide3(self):
        return self.side3

    def setSide3(self, side3):
        self.side3 = side3

    def getArea(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        area = math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
        return area

    def getPerimeter(self):
        return self.side1 + self.side2 + self.side3

    def __str__(self):
        return super().__str__() + " Triangle: side1 = " + str(self.side1) + " side2 = " + \
               str(self.side2) + " side3 = " + str(self.side3)


def main():
    try:
        s1, s2, s3 = eval(input("Enter three sides of a Triangle: "))
        color = input("Enter color of a triangle: ")
        isFilled = bool(int(input("Is the triangle filled? (1 or 0): ")))

        trngl = Triangle(s1, s2, s3, color, isFilled)
        print("Triangle's area is:", trngl.getArea())
        print("Triangle's perimeter is:", trngl.getPerimeter())
        print(trngl)
    except TriangleError:
        print("Cannot form a triangle from this input")


main()
