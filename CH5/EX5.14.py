# 5.14 (Find the smallest n such that n2 12,000) Use a while loop to find the smallest
# integer n such that n2 is greater than 12,000.

n = 1
while True:
    if n ** 2 > 12000:
        break
    n += 1

print("The smallest integer n such that n^2 > 12,000 is", n)
