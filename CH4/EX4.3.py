# (Algebra: solve 2*2 linear equations) You can use Cramer’s rule to solve the
# following 2*2 system of linear equation:
# Write a program that prompts the user to enter a, b, c, d, e, and f and display the
# result. If ad – bc is 0, report that The equation has no solution.

a, b, c, d, e, f = eval(input("Enter a, b, c, d, e, f: "))

if a * d - b * c == 0:
    print("The equation has no solution")
else:
    x = (e * d - b * f) / (a * d - b * c)
    y = (a * f - e * c) / (a * d - b * c)
    print("x is", format(x, "0.1f"), "y is", format(y, "0.1f"))
