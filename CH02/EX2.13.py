# (Split digits) Write a program that prompts the user to enter a four-digit integer
# and displays the number in reverse order.
num = int(input("Enter an integer: "))
n1 = num % 10
num //= 10
n2 = num % 10
num //= 10
n3 = num % 10
num //= 10
n4 = num
print(n4)
print(n3)
print(n2)
print(n1)
