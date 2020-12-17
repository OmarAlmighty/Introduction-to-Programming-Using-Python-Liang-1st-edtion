# 5.4 (Conversion from miles to kilometers) Write a program that displays the following
# table (note that 1 mile is 1.609 kilometers):
# Miles Kilometers
# 1 1.609
# 2 3.218
# ...
# 9 15.481
# 10 16.090

MILES_TO_KILOMETRE = 1.609
print("Mile", format("Kilometre", "8s"))
for i in range(1, 11):
    kilometre = i * MILES_TO_KILOMETRE
    print(i, format(kilometre, "11.3f"))
