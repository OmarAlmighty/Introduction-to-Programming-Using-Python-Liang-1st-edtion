# *6.17 (The MyTriangle module) Create a module named MyTriangle that contains
# the following two functions:
# # Returns true if the sum of any two sides is
# # greater than the third side.
# def isValid(side1, side2, side3):
# # Returns the area of the triangle.
# def area(side1, side2, side3):
# Write a test program that reads three sides for a triangle and computes the area if the
# input is valid. Otherwise, it displays that the input is invalid. The formula for computing
# the area of a triangle is given in Exercise 2.14.
from CH6Module import MyFunctions

s1, s2, s3 = eval(input("Enter three sides in double: "))

if MyFunctions.isValid(s1, s2, s3):
    print("The area of the triangle is", MyFunctions.area(s1, s2, s3))
else:
    print("Input is invalid")
