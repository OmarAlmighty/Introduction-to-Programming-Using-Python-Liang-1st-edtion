# 6.9 (Conversions between feet and meters) Write a module that contains the following
# two functions:
# # Converts from feet to meters
# def footToMeter(foot):
# # Converts from meters to feet
# def meterToFoot(meter):
# The formulas for the conversion are:
# foot = meter / 0.305
# meter = 0.305 * foot
# Write a test program that invokes these functions to display the following tables:
# Feet Meters | Meters Feet
# 1.0 0.305 | 20.0 66.574
# 2.0 0.610 | 26.0 81.967
# ...
# 9.0 2.745 | 60.0 196.721
# 10.0 3.050 | 66.0 213.115
from CH6Module import MyFunctions

print("Feet\t\tMeters  |  Meters\t\tFeet")
feet = 1
meter = 20
for i in range(1, 11):
    print(format(feet, ".1f"), format(" ", "8s"), format(MyFunctions.footToMeter(feet), ".3f"), end="\t|")
    print(format(" ", "2s"), format(meter, ".1f"), format(" ", "4s"),
          format(MyFunctions.meterToFoot(meter), ".3f"))
    feet += 1
    meter += 6
