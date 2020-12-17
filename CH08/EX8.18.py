# 8.18 (Geometry: The Circle2D class) Define the Circle2D class that contains:
# ■ Two private float data fields named x and y that specify the center of the circle
# with get/set methods.
# ■ A private data field radius with get/set methods.
# ■ A constructor that creates a circle with the specified x, y, and radius. The
# default values are all 0.
# ■ A method getArea() that returns the area of the circle.
# ■ A method getPerimeter() that returns the perimeter of the circle.
# ■ A method containsPoint(x, y) that returns True if the specified point (x,
# y) is inside this circle (see Figure 8.10a).
# ■ A method contains(circle2D) that returns True if the specified circle is
# inside this circle (see Figure 8.10b).
# ■ A method overlaps(circle2D) that returns True if the specified circle
# overlaps with this circle (see Figure 8.10c).
# ■ Implement the __contains__(another) method that returns True if this
# circle is contained in another circle.
# ■ Implement the __cmp__, __lt__, __le__, __eq__, __ne__, __gt__,
# __ge__ methods that compare two circles based on their radius.
# Draw the UML diagram for the class, and then implement the class. Write a test
# program that prompts the user to enter two circles with x- and y-coordinates and the
# radius, creates two Circle2D objects c1 and c2, displays their areas and perimeters,
# and displays the result of c1.containsPoint(c2.getX(), c2.getY()),
# c1.contains(c2), and c1.overlaps(c2).
import math


class Circle2D:
    def __init__(self, x=0, y=0, radius=0):
        self.__x__ = x
        self.__y__ = y
        self.__r__ = radius

    def getX(self):
        return self.__x__

    def getY(self):
        return self.__y__

    def getRadius(self):
        return self.__r__

    def setX(self, x):
        self.__x__ = x

    def setY(self, y):
        self.__y__ = y

    def setRadius(self, radius):
        self.__r__ = radius

    def getArea(self):
        return math.pi * self.getRadius() ** 2

    def getPerimeter(self):
        return math.pi * 2 * self.getRadius()

    def containsPoint(self, x, y):
        dis = math.sqrt((self.getX() - x) ** 2 + (self.getY() - y) ** 2)
        return True if dis <= self.getRadius() else False

    def contains(self, circle):
        dis = math.sqrt((self.getX() - circle.getX()) ** 2 + (self.getY() - circle.getY()) ** 2)
        return True if self.getRadius() >= dis + circle.getRadius() else False

    def overlaps(self, circle):
        dis = math.sqrt((self.getX() - circle.getX()) ** 2 + (self.getY() - circle.getY()) ** 2)
        return True if dis <= self.getRadius() + circle.getRadius() else False

    def __contains__(self, circle):
        return circle.contains(self)

    def __eq__(self, circle):
        return True if self.getRadius() == circle.getRadius() else False

    def __ne__(self, circle):
        return True if self.getRadius() != circle.getRadius() else False

    def __cmp__(self, circle):
        if self.getRadius() > circle.getRadius():
            return 1
        elif self.getRadius() < circle.getRadius():
            return -1
        else:
            return 0

    def __lt__(self, circle):
        return self.getRadius() < circle.getRadius()

    def __gt__(self, circle):
        return self.getRadius() > circle.getRadius()

    def __ge__(self, circle):
        return self.getRadius() >= circle.getRadius()

    def __le__(self, circle):
        return self.getRadius() <= circle.getRadius()


def main():
    x1, y1, r1 = eval(input("Enter x1, y1, radius1: "))
    x2, y2, r2 = eval(input("Enter x1, y1, radius2: "))
    c1 = Circle2D(x1, y1, r1)
    c2 = Circle2D(x2, y2, r2)
    print("Area for c1 is", c1.getArea())
    print("Perimeter for c1", c1.getPerimeter())
    print("Area for c2 is", c2.getArea())
    print("Perimeter for c2", c2.getPerimeter())
    print("c1 contains the center of c2?", c1.containsPoint(c2.getX(), c2.getY()))
    print("c1 contains c2?", c1.contains(c2))
    print("c1 overlaps c2?", c1.overlaps(c2))

main()