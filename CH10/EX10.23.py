# 10.23 (Algebra: solve quadratic equations) Write a function for solving a quadratic
# equation using the following header:
# def solveQuadratic(eqn, roots):
# The coefficients of a quadratic equation ax^2+ bx+c =0 are passed to the list
# eqn and the noncomplex roots are stored in roots. The function returns the
# number of roots. See Programming Exercise 4.1 on how to solve a quadratic
# equation.
# Write a program that prompts the user to enter values for a, b, and c and displays
# the number of roots and all noncomplex roots.
import math


def solveQuadratic(eqn, roots):
    a = eqn[0]
    b = eqn[1]
    c = eqn[2]

    discriminant = math.pow(b, 2) - 4 * a * c

    if discriminant > 0:
        r1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        r2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        roots.append(r1)
        roots.append(r2)
    elif discriminant == 0:
        r1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        roots.append(r1)

    return len(roots)


a, b, c = eval(input("Enter a, b, c: "))
eqn = [a, b, c]
roots = []

n = solveQuadratic(eqn, roots)
print("The number of roots:", n)
print("The roots:", roots)
