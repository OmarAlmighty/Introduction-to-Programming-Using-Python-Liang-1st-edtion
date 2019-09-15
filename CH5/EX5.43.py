# 5.43 (Math: combinations) Write a program that displays all possible combinations for
# picking two numbers from integers 1 to 7. Also display the total number of combinations.

count = 0
for i in range(1, 8):
    for j in range(i+1, 8):
        print(i, " ", j)
        count += 1

print("The total number of all combinations is", count)
