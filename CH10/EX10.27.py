# 10.27 (Pattern recognition: four consecutive equal numbers) Write the following function
# that tests whether the list has four consecutive numbers with the same value:
# def isConsecutiveFour(values):
# Write a test program that prompts the user to enter a series of integers and reports
# whether the series contains four consecutive numbers with the same value.

def isConsecutiveFour(values):
    if len(values) != len(set(values)):  # there are duplicates
        return False
    diff = values[0] - values[1]
    for i in range(len(values) - 1):
        if values[i] - values[i + 1] != diff:
            return False
    return True


values = [int(x) for x in input("Enter numbers: ").split()]
print(isConsecutiveFour(values))
