# (Health application: BMI ) Revise Listing 4.6, ComputeBMI.py, to let users enter
# their weight in pounds and their height in feet and inches. For example, if a person
# is 5 feet and 10 inches, you will enter 5 for feet and 10 for inches.

KILOGRAMS_PER_POUND = 0.45359237
METERS_PER_INCH = 0.0254

weight = eval(input("Enter weight in pounds: "))
feet = eval(input("Enter feet: "))
inches = eval(input("Enter inches: "))

weightInKilograms = weight * KILOGRAMS_PER_POUND
totalHeightInches = feet * 12 + inches
heightInMeters = totalHeightInches * METERS_PER_INCH

bmi = weightInKilograms / (heightInMeters * heightInMeters)

print("BMI is", bmi)
if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")
