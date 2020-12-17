# (Sort three integers) Write a program that prompts the user to enter three integers
# and displays them in increasing order.
import math

a, b, c = eval(input("Enter a, b, c: "))
A, B, C = False, False, False
s = ""

if a <= b and a <= c:
    s += str(a) + ", "
    if b < c:
        s += str(b) + ", "
        C = True
    else:
        s += str(c) + ", "
        B = True
elif b <= a and b <= c:
    s += str(b) + ", "
    if a < c:
        s += str(a) + ", "
        C = True
    else:
        s += str(c) + ", "
        A = True
elif c <= a and c <= b:
    s += str(c) + ", "
    if b < a:
        s += str(b) + ", "
        A = True
    else:
        s += str(a) + ", "
        B = True

if A:
    s += str(a)
if B:
    s += str(b)
if C:
    s += str(c)

print(s)
