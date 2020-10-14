# 12.1 (The Triangle class) Design a class named Triangle that extends the
# GeometricObject class. The Triangle class contains:
# ■ Three float data fields named side1, side2, and side3 to denote the three
# sides of the triangle.
# ■ A constructor that creates a triangle with the specified side1, side2, and
# side3 with default values 1.0.
# ■ The accessor methods for all three data fields.
# ■ A method named getArea() that returns the area of this triangle.
# ■ A method named getPerimeter() that returns the perimeter of this triangle.
# ■ A method named __str__() that returns a string description for the triangle.
# For the formula to compute the area of a triangle, see Exercise 2.14. The
# __str__() method is implemented as follows:
# return "Triangle: side1 = " + str(side1) + " side2 = " +
# str(side2) + " side3 = " + str(side3)
# Draw the UML diagrams for the classes Triangle and GeometricObject.
# Implement the Triangle class. Write a test program that prompts the user to
# enter the three sides of the triangle, a color, and 1 or 0 to indicate whether the triangle
# is filled. The program should create a Triangle object with these sides and
# set the color and filled properties using the input. The program should display the
# triangle’s area, perimeter, color, and True or False to indicate whether the triangle
# is filled or not.
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
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def getSide1(self):
        return self.side1

    def setSide1(self, side1):
        self.side1 = side1

    def getSide2(self):
        return self.side2

    def setSide2(self, side2):
        self.side1 = side2

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
    s1, s2, s3 = eval(input("Enter three sides of a Triangle: "))
    color = input("Enter color of a triangle: ")
    isFilled = bool(int(input("Is the triangle filled? (1 or 0): ")))

    trngl = Triangle(s1, s2, s3, color, isFilled)
    print("Triangle's area is:", trngl.getArea())
    print("Triangle's perimeter is:", trngl.getPerimeter())
    print(trngl)


main()
