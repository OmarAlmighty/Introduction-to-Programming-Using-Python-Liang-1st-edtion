# 5.8 (Use the math.sqrt function) Write a program that prints the following table
# using the sqrt function in the math module.
# Number Square Root
# 0 0.0000
# 2 1.4142
# ...
# 18 5.2426
# 20 5.4721
import math

print(format("Number", "12s"), "Square Root")

for i in range(0, 21, 2):
    print(format(i, "2.0f"), format(math.sqrt(i), "16.4f"))
