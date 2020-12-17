# 5.3 (Conversion from kilograms to pounds) Write a program that displays the following
# table (note that 1 kilogram is 2.2 pounds):
# Kilograms Pounds
# 1 2.2
# 3 6.6
# ...
# 197 433.4
# 199 437.8

KILOGRAM_TO_POUND = 2.2
print("Kilograms", format("Pounds", "8s"))
for i in range(1, 200,2):
    pound = i * KILOGRAM_TO_POUND
    print(i, format(pound, "11.1f"))
