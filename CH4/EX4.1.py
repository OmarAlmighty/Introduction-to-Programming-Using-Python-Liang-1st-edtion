# (Algebra: solve quadratic equations) The two roots of a quadratic equation, for
# example, can be obtained using the following formula:
# is called the discriminant of the quadratic equation. If it is positive, the
# equation has two real roots. If it is zero, the equation has one root. If it is negative,
# the equation has no real roots.
# Write a program that prompts the user to enter values for a, b, and c and displays
# the result based on the discriminant. If the discriminant is positive, display two
# roots. If the discriminant is 0, display one root. Otherwise, display The equation
# has no real roots.
import math

a, b, c = eval(input("Enter a, b, c: "))

discriminant = math.pow(b, 2) - 4 * a * c

if discriminant > 0:
    r1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    r2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    print("The roots are", format(r1, "0.6f"), format(r2, "0.6f"))
elif discriminant == 0:
    r1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    print("The root is", format(r1, "0.6f"))
else:
    print("The equation has no real roots")
