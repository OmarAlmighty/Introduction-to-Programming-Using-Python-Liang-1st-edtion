# 8.21 (Math: The Complex class) Python has the complex class for performing complex
# number arithmetic. In this exercise, you will design and implement your own
# Complex class. Note that the complex class in Python is named in lowercase, but
# our custom Complex class is named with C in uppercase.
# A complex number is a number of the form where a and b are real numbers
# and iis The numbers a and b are known as the real part and the imaginary
# part of the complex number, respectively. You can perform addition, subtraction,
# multiplication, and division for complex numbers using the following formulas:
# (a + bi) + (c + di) = (a + c) + (b + d)i
# a + bi - (c + di) = (a - c) + (b - d )i
# (a + bi) * (c + di ) = (ac - bd ) + (bc + ad )i
# (a + bi)/(c + di ) = (ac + bd˛ ˛)/(c2 + d2) + (bc - ad )i/(c2 + d2)
# You can also obtain the absolute value for a complex number using the following
# formula:
# (A complex number can be interpreted as a point on a plane by identifying the (a,b)
# values as the coordinates of the point. The absolute value of the complex number
# corresponds to the distance of the point to the origin, as shown in Figure 8.12.)
# Design a class named Complex for representing complex numbers and the methods
# __add__, __sub__, __mul__, __truediv__, and __abs__ for performing
# complex-number operations, and override the __str__ method by
# returning a string representation for a complex number. The __str__ method
# returns (a + bi) as a string. If b is 0, it simply returns a.
# Provide a constructor Complex(a, b) to create a complex number with
# the default value of 0 for a and b. Also provide the getRealPart() and
# getImaginaryPart() methods for returning the real and imaginary parts of the
# complex number, respectively.
# Write a test program that prompts the user to enter two complex numbers and displays
# the result of their addition, subtraction, multiplication, and division.
import math


class Complex(object):
    def __init__(self, real, imag=0.0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        r1 = self.real + other.real
        i1 = self.imag + other.imag
        ans = Complex(r1, i1)
        return ans

    def __sub__(self, other):
        r1 = self.real - other.real
        i1 = self.imag - other.imag
        ans = Complex(r1, i1)
        return ans

    def __mul__(self, other):
        r1 = self.real * other.real
        r2 = self.imag * other.imag
        ex1 = r1 - r2
        i1 = self.real * other.imag
        i2 = self.imag * other.real
        ex2 = i1 + i2
        c = Complex(ex1, ex2)
        return c

    def __truediv__(self, other):
        r1 = self.real * other.real
        r2 = self.imag * other.imag
        denom = other.real ** 2 + other.imag ** 2
        n1 = int((r1 + r2) / denom)
        i1 = self.real * other.imag * (-1)
        i2 = self.imag * other.real
        n2 = int((i1 + i2) / denom)
        c = Complex(n1, n2)
        return c

    def __abs__(self):
        return math.sqrt(self.real ** 2 + self.imag ** 2)

    def __neg__(self):  # defines -c (c is Complex)
        return Complex(-self.real, -self.imag)

    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        ans = '( ' + str(self.real) + ' + ' + str(self.imag) + 'i' + ' )'
        return ans


def main():
    r1, i1 = eval(input("Enter the first complex number: "))
    r2, i2 = eval(input("Enter the second complex number: "))
    c1 = Complex(r1, i1)
    c2 = Complex(r2, i2)
    print(c1, '+', c2, '=', c1 + c2)
    print(c1, '-', c2, '=', c1 - c2)
    print(c1, '*', c2, '=', c1 * c2)
    print(c1, '/', c2, '=', c1 / c2)
    print('|', c1, '|', '=', c1.__abs__())


main()
