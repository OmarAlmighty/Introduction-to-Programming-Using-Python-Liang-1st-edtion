# 6.34 (Geometry: area of a regular polygon) Rewrite Exercise 3.5 using the following
# function to return the area of a regular polygon:
# def area(n, side):
import math


def area(n, side):
    return (n * side ** 2) / (4 * math.tan(math.pi / n))


def main():
    print("The area of the polygon is",
          area(int(input("Enter the number of sides: ")), eval(input("Enter the side: "))))

main()