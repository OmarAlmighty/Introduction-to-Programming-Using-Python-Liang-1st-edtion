# 10.12 (Compute GCD) Write a function that returns the greatest common divisor
# (GCD) of integers in a list. Use the following function header:
# def gcd(numbers):
# Write a test program that prompts the user to enter five numbers, invokes the
# function to find the GCD of these numbers, and displays the GCD.

def gcd(numbers):
    gcd = min(numbers)
    i = 0
    while True:
        if numbers[i] % gcd != 0:
            gcd-=1
            i = 0
        else: i+=1
        if i == len(numbers):
            break
    return gcd

def main():
    lst = input("Enter numbers: ").split()
    lst = [int(x) for x in lst]
    print(gcd(lst))

main()