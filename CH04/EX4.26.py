# 4.26 (Palindrome number) Write a program that prompts the user to enter a three-digit
# integer and determines whether it is a palindrome number.
# A number is a palindromeif it reads the same from right to left and from left to right.

num = int(input("Enter a three-digit integer: "))
N = num
n1 = num // 100
num %= 100
n2 = num // 10
num %= 10
n3 = num

if n1 == n3:
    print(str(N),"is a palindrome")
else:
    print(str(N), "is not a palindrome")