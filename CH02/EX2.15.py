# (Geometry: area of a hexagon) Write a program that prompts the user to enter the
# side of a hexagon and displays its area. The formula for computing the area of a
# hexagon is Area = where s is the length of a side.

side = eval(input("Enter the side: "))
area = (3 * 3 ** 0.5 * side ** 2) / 2
print("The area of the hexagon is", area)
