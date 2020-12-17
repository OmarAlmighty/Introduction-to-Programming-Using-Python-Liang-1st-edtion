# 6.33 (Geometry: area of a pentagon) Rewrite Exercise 3.4 using the following function
# to return the area of a pentagon:
# def area(s):
import math


def area(s):
    return (5 * s**2) / (4 * math.tan(math.pi / 5))

def main():
    print("The area of the pentagon is", area(eval(input("Enter the side: "))))


main()