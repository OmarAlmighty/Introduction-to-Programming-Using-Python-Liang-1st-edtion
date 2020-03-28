# 10.6 (Revise Listing 5.13, PrimeNumber.py) Listing 5.13 determines whether a number
# n is prime by checking whether 2, 3, 4, 5, 6, ..., n/2 is a divisor for n. If a divisor
# is found, n is not prime. A more efficient approach is to check whether any of the
# prime numbers less than or equal to can divide n evenly. If not, n is prime.
# Rewrite Listing 5.13 to display the first 50 prime numbers using this approach.
# You need to use a list to store the prime numbers and later use them to check
# whether they are possible divisors for n.

import math

primes = []

count = 0
number = 2
print("The first 50 prime numbers are \n")

while count < 50:
    isPrime = True
    i = 0
    while i < count and primes[i] <= math.sqrt(number):
        if number % primes[i] == 0:
            isPrime = False
            break

        i += 1

    if isPrime:
        primes.append(number)
        count += 1

        if count % 10 == 0:
            print(number)
        else:
            print(number, end=" ")

    number += 1