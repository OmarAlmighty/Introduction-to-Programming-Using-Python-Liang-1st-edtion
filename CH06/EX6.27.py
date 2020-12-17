# 6.27 (Twin primes) Twin primes are a pair of prime numbers that differ by 2. For example,
# 3 and 5, 5 and 7, and 11 and 13 are twin primes. Write a program to find all
# twin primes less than 1,000. Display the output as follows:
# (3, 5)
# (5, 7)...

from CH6Module import MyFunctions

x = 3
while x < 1000:
    if MyFunctions.isPrime(x) and MyFunctions.isPrime(x + 2):
        print("(" + str(x) + ", " + str(x + 2) + ")")

    x += 1
