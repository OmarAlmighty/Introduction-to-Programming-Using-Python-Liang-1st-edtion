# 5.1 (Count positive and negative numbers and compute the average of numbers)
# Write a program that reads an unspecified number of integers, determines
# how many positive and negative values have been read, and computes the total
# and average of the input values (not counting zeros). Your program ends with the
# input 0. Display the average as a floating-point number.

avg = 0
postives = 0
negativies = 0
total = 0
n = int(input("Enter an integer, the input ends if it is 0: "))

if n == 0:
    print("You didn't enter any number")
else:
    while n != 0:
        if n > 0:
            postives += 1
        else:
            negativies += 1
        total += n
        avg = total / (postives + negativies)
        n = int(input("Enter an integer, the input ends if it is 0: "))

    print("The number of positives is", postives)
    print("The number of negatives is", negativies)
    print("The total is", total)
    print("The average is", avg)
