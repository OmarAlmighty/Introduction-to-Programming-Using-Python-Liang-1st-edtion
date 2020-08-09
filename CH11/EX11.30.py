# 11.30 (Algebra: solve linear equations) Write a function that solves the following
# system of linear equations:
# a00x + a01y = b0        x =b0a11 - b1a01 / a00a11 - a01a10
# a10x + a11y = b1        y =b1a00 - b0a10 / a00a11 - a01a10
# The function header is:
# def linearEquation(a, b):
# The function returns None if a00a11 - a01a10 is 0; otherwise, it returns the
# solution for x and y in a list. Write a test program that prompts the user to enter
# a00, a01, a10, a11, b0 and b1 and displays the result. If a00a11 - a01a10 is 0, report
# that The equation has no solution.

def main():
    a, b, c, d, e, f = eval(input("Enter a00, a01, a10, a11, b0, b1: "))
    A = [[a, b], [c, d]]
    B = [e, f]

    result = linearEquation(A, B)

    if result == None:
        print("The equation has no solution")
    else:
        print("x is", result[0], "and y is", result[1])


def linearEquation(a, b):
    determinant = a[0][0] * a[1][1] - a[0][1] * a[1][0]

    if determinant == 0:
        return None
    else:
        result = []
        x = (b[0] * a[1][1] - b[1] * a[0][1]) / determinant
        y = (b[1] * a[0][0] - b[0] * a[1][0]) / determinant
        result.append(x)
        result.append(y)
        return result


main()