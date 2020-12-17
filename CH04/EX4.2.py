# (Game: add three numbers) The program in Listing 4.1 generates two integers and
# prompts the user to enter the sum of these two integers. Revise the program to generate
# three single-digit integers and prompt the user to enter the sum of these three
# integers.
import random

n1, n2, n3 = random.randint(0, 9), random.randint(0, 9), random.randint(0, 9)

print("What is", str(n1), "+", str(n2), "+", str(n3), "?")
res = eval(input())
print(str(n1), "+", str(n2), "+", str(n3), "=", res, "is", (res == (n1 + n2 + n3)))
