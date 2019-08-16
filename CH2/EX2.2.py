# (Compute the volume of a cylinder) Write a program that reads in the radius and
# length of a cylinder and computes the area and volume using the following formulas:
# area = radius * radius * π
# volume = area * length

PI = 3.1415

rad, len = eval(input("Enter the radius and length of a cylinder:"))
area = rad * rad * PI
vol = area * len
print("The area is", area)
print("Thr volume is", vol)
