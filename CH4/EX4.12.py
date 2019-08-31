# 4.12 (Check a number) Write a program that prompts the user to enter an integer and
# checks whether the number is divisible by both 5 and 6, divisible by 5 or 6, or just
# one of them (but not both).

n = int(input("Enter an integer: "))

print("Is", n, " divisible by 5 and 6?", n % 5 == 0 and n % 6 == 0)
print("Is", n, "divisible by 5 or 6?", n % 5 == 0 or n % 6 == 0)
print("Is", n, "divisible by 5 or 6, but not both?", (n % 5 == 0 and n % 6 != 0) or (n % 5 != 0 and n % 6 == 0))
