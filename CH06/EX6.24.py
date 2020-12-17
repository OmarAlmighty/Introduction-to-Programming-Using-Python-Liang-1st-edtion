# 6.24 (Palindromic prime) A palindromic prime is a prime number that is also palindromic.
# For example, 131 is a prime and also a palindromic prime, as are 313 and
# 757. Write a program that displays the first 100 palindromic prime numbers. Display
# 10 numbers per line and align the numbers properly,

from CH6Module import MyFunctions

counter = 1
x = 2
while counter < 101:
    if MyFunctions.isPrime(x) and MyFunctions.isPalindrome(x):
        if counter % 10 != 0:
            print(x, end='  ')
        else:
            print(x)
        counter += 1
    x += 1

