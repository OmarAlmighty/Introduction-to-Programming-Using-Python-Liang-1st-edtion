# 6.8 (Conversions between Celsius and Fahrenheit) Write a module that contains the
# following two functions:
# # Converts from Celsius to Fahrenheit
# def celsiusToFahrenheit(celsius):
# # Converts from Fahrenheit to Celsius
# def fahrenheitToCelsius(fahrenheit):
# The formulas for the conversion are:
# celsius = (5 / 9) * (fahrenheit – 32)
# fahrenheit = (9 / 5) * celsius + 32
# Write a test program that invokes these functions to display the following tables:
# Celsius Fahrenheit | Fahrenheit Celsius
# 40.0 104.0 | 120.0 48.89
# 39.0 102.2 | 110.0 43.33
# ...
# 32.0 89.6 | 40.0 4.44
# 31.0 87.8 | 30.0 -1.11
from CH6Module import MyFunctions

print("Celsius\t\tFahrenheit  |  Fahrenheit\t\tCelsius")
celsuis = 40
fahr = 120
for i in range(1, 11):
    print(format(celsuis, ".2f"), format(" ", "8s"), format(MyFunctions.celsiusToFahrenheit(celsuis), ".2f"), end="\t|")
    print(format(" ", "3s"), format(fahr, ".2f"), format(" ", "8s"),
          format(MyFunctions.fahrenheitToCelsius(fahr), "-.2f"))
    celsuis -= 1
    fahr -= 10
