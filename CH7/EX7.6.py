# 7.6 (Algebra: quadratic equations) Design a class named QuadraticEquation for a
# quadratic equation The class contains:
# ■ The private data fields a, b, and c that represent three coefficients.
# ■ A constructor for the arguments for a, b, and c.
# ■ Three get methods for a, b, and c.
# ■ A method named getDiscriminant() that returns the discriminant, which is
# ■ The methods named getRoot1() and getRoot2() for returning the two roots
# of the equation using these formulas:
# These methods are useful only if the discriminant is nonnegative. Let these methods
# return 0 if the discriminant is negative.
# Draw the UML diagram for the class, and then implement the class. Write a test
# program that prompts the user to enter values for a, b, and c and displays the result
# based on the discriminant. If the discriminant is positive, display the two roots. If
# the discriminant is 0, display the one root. Otherwise, display “The equation has
# no roots."
from CH7.QuadraticEquation import QuadraticEquation

a, b, c = eval(input("Enter a, b, c: "))
eq = QuadraticEquation(a, b, c)
disc = eq.getDiscriminant()
if disc < 0:
    print("The equation has no roots")
elif disc == 0:
    print("The root is", eq.getRoot1())
else:
    print("The roots are", eq.getRoot1(), "and", eq.getRoot2())