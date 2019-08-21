# (Reverse number) Write a program that prompts the user to enter a four-digit integer
# and displays the number in reverse order.

num = eval(input("Enter an integer: "))
n1 = num % 10
num = num // 10
n2 = num % 10
num = num // 10
n3 = num % 10
num = num // 10
n4 = num
print(n1, end='')
print(n2, end='')
print(n3, end='')
print(n4, end='')

