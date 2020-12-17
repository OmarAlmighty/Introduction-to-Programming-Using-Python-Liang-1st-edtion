# 14.2 (Count occurrences of numbers) Write a program that reads an unspecified number
# of integers and finds the ones that have the most occurrences. For example, if
# you enter 2 3 40 3 5 4 –3 3 3 2 0, the number 3 occurs most often. Enter all numbers
# in one line. If not one but several numbers have the most occurrences, all of
# them should be reported. For example, since 9 and 3 appear twice in the list 9 30
# 3 9 3 2 4, both occurrences should be reported.

nums = input("Enter numbers in one line: ").split()

nums_dict = {}

for n in nums:
    if n in nums_dict:
        nums_dict[n] += 1
    else:
        nums_dict[n] = 0

pairs = list(nums_dict.items())
nums = [[x, y] for (y, x) in pairs]
nums.sort(reverse=True)

print(nums[0][1], end=' ')

for i in range(1, len(nums)):
    if nums[i][0] == nums[0][0]:
        print(nums[i][1], end=' ')
    else:
        print()
        break
