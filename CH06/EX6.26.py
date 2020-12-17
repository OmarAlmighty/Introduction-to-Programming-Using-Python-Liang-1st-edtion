# 6.26 (Mersenne prime) A prime number is called a Mersenne prime if it can be written
# in the form for some positive integer p. Write a program that finds all
# Mersenne primes with and displays the output as follows:
# p 2^p - 1
# 2 3
# 3 7
# 5 31
# ...
from CH6Module import MyFunctions

print("P", "   ", "2^p - 1")
for p in range(2, 31 + 1):
    i = 2 ** p - 1

    # Display each number in five positions
    if MyFunctions.isPrime(i):
        print(str(p) + "\t\t" + str(i))
