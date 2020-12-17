# 5.15 (Find the largest n such that n3 12,000) Use a while loop to find the largest
# integer n such that n3 is less than 12,000.

n = 12000
while True:
    if n ** 3 < 12000:
        break
    n -= 1

print("the largest n such that n^3 < 12,000 is", n)
