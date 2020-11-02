# 13.11 (The Triangle class) Modify the Triangle class in Programming Exercise 12.1
# to throw a RuntimeError exception if the three given sides cannot form a
# triangle.

import math


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
            raise RuntimeError()

    def isLegal(self):
        return self.__side1 + self.__side2 > self.__side3 and \
               self.__side2 + self.__side3 > self.__side1 and \
               self.__side1 + self.__side3 > self.__side2

    def getSide1(self):
        return self.__side1

    def setSide1(self, side1):
        self.__side1 = side1

    def getSide2(self):
        return self.__side2

    def setSide2(self, side2):
        self.__side2 = side2

    def getSide3(self):
        return self.__side3

    def setSide3(self, side3):
        self.__side3 = side3

    def getArea(self):
        s = (self.__side1 + self.__side2 + self.__side3) / 2
        area = math.sqrt(s * (s - self.__side1) * (s - self.__side2) * (s - self.__side3))
        return area

    def getPerimeter(self):
        return self.__side1 + self.__side2 + self.__side3

    def __str__(self):
        return super().__str__() + " Triangle: side1 = " + str(self.__side1) + " side2 = " + \
               str(self.__side2) + " side3 = " + str(self.__side3)


def main():
    try:
        s1, s2, s3 = eval(input("Enter three sides of a Triangle: "))
        color = input("Enter color of a triangle: ")
        isFilled = bool(int(input("Is the triangle filled? (1 or 0): ")))

        trngl = Triangle(s1, s2, s3, color, isFilled)
        print("Triangle's area is:", trngl.getArea())
        print("Triangle's perimeter is:", trngl.getPerimeter())
        print(trngl)
    except RuntimeError:
        print("Cannot form a triangle")


main()
