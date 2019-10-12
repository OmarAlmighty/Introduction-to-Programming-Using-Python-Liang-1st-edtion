# 6.3 (Palindrome integer) Write the functions with the following headers:
# # Return the reversal of an integer, e.g. reverse(456) returns
# # 654
# def reverse(number):
# # Return true if number is a palindrome
# def isPalindrome(number):
# Use the reverse function to implement isPalindrome. A number is a palindrome
# if its reversal is the same as itself. Write a test program that prompts the
# user to enter an integer and reports whether the integer is a palindrome.

# Return the reversal of an integer, e.g. reverse(456) returns
# 654
def reverse(number):
    num = ""
    while number > 0:
        n1 = number % 10
        num = num + str(n1)
        number = number // 10

    return int(num)


# Return true if number is a palindrome
def isPalindrome(number):
    revNumber = reverse(number)
    return True if revNumber == number else False


num = eval(input("Enter a number: "))
print(isPalindrome(num))
