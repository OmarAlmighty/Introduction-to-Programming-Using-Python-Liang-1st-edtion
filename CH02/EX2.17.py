# (Health application: compute BMI) Body mass index (BMI) is a measure of health
# based on weight. It can be calculated by taking your weight in kilograms and
# dividing it by the square of your height in meters. Write a program that prompts
# the user to enter a weight in pounds and height in inches and displays the BMI.
# Note that one pound is 0.45359237 kilograms and one inch is 0.0254 meters.
weight = eval(input("Enter weight in pounds:"))
height = eval(input("Enter height in inches:"))
weight = weight *0.45359237
height = height *0.0254
bmi = weight / height**2
print("BMI is",bmi)