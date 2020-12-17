# 6.2 (Sum the digits in an integer) Write a function that computes the sum of the digits
# in an integer. Use the following function header:
# def sumDigits(n):
# For example, sumDigits(234) returns 9 (Hint: Use the % operator
# to extract digits, and the // operator to remove the extracted digit. For instance, to
# extract 4 from 234, use 234 % 10 To remove 4 from 234, use 234 // 10
# Use a loop to repeatedly extract and remove the digits until all the digits
# are extracted.) Write a test program that prompts the user to enter an integer and
# displays the sum of all its digits.

def sumDigits(n):
    sum = 0
    while n > 0:
        n1 = n % 10
        sum += n1
        n = n // 10

    return sum


n = eval(input("Enter an integer: "))
print("The sum of the digits is", sumDigits(n))
