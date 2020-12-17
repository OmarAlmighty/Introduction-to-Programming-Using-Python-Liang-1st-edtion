# 7.7 (Algebra: linear equations) Design a class named LinearEquation for a
# system of linear equations:
# The class contains:
# ax + by = e     cx + dy = f
# x =ed - bf / ad - bc
# y = af - ec /ad - bc
# ■ The private data fields a, b, c, d, e, and f with get methods.
# ■ A constructor with the arguments for a, b, c, d, e, and f.
# ■ Six get methods for a, b, c, d, e, and f.
# ■ A method named isSolvable() that returns true if is not 0.
# ■ The methods getX() and getY() that return the solution for the equation.
# Draw the UML diagram for the class, and then implement the class. Write a test
# program that prompts the user to enter a, b, c, d, e, and f and displays the result.
# If ad - bc is 0, report that “The equation has no solution.”
from CH7.LinearEquation import LinearEquation

a, b, c, d, e, f = eval(input("Enter a,b,c,d,e,f: "))
eq = LinearEquation(a, b, c, d, e, f)
if (eq.isSolvable()):
    print("X:", eq.getX(), "\tY:", eq.getY())
else:
    print("The equation is not solvable!")
