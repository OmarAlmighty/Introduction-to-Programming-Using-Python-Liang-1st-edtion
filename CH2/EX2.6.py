# (Sum the digits in an integer) Write a program that reads an integer between 0 and
# 1000 and adds all the digits in the integer. For example, if an integer is 932, the
# sum of all its digits is 14. (Hint: Use the % operator to extract digits, and use the //
# operator to remove the extracted digit. For instance, 932 % 10 = 2 and 932 //
# 10 = 93.)
num = eval(input("Enter a number between 0 and 1000: "))
num1 = num % 10
num //= 10
num2 = num % 10
num //= 10
num3 = num
print("The sum of the digits is", (num1 + num2 + num3))
