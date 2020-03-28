# 10.24 (Math: combinations) Write a program that prompts the user to enter 10 integers
# and displays all the combinations of picking two numbers from the 10.

nums = []
for i in range(10):
    nums.append(eval(input("Enter a number:")))

for i in range(len(nums)):
    for j in range(len(nums)):
        print("(", nums[i], nums[j], ")", end="     ")
        if j % 5 == 0:
            print()
