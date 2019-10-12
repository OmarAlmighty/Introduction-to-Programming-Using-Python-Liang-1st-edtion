# 6.25 (Emirp) An emirp ( prime spelled backward) is a nonpalindromic prime number
# whose reversal is also a prime. For example, both 17 and 71 are prime numbers, so
# 17 and 71 are emirps. Write a program that displays the first 100 emirps. Display
# 10 numbers per line and align the numbers properly,

from CH6Module import MyFunctions

counter = 1
x = 2
while counter < 101:
    if MyFunctions.isPrime(x) and MyFunctions.isPrime(MyFunctions.reverse(x)):
        if counter % 10 != 0:
            print(x, end='  ')
        else:
            print(x)
        counter += 1
    x += 1