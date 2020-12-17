# 4.20 (Science: wind-chill temperature) Exercise 2.9 gives a formula to compute the
# wind-chill temperature. The formula is valid for temperatures in the range
# between and 41°F and for wind speed greater than or equal to 2. Write a
# program that prompts the user to enter a temperature and a wind speed. The program
# displays the wind-chill temperature if the input is valid; otherwise, it displays
# a message indicating whether the temperature and/or wind speed is invalid.

temp, windSpeed = eval(input("Enter temperature in Fahrenheit and wind speed: "))

if (temp < -58 or temp > 41) or (windSpeed < 2):
    print("The temperature and/or wind speed is invalid.")
else:
    windChill = 35.74 + 0.6215 * temp - 35.75 * windSpeed ** 0.16 + 0.4275 * temp * windSpeed ** 0.16
    print("The wind chill temprature is", format(windChill, "0.2f"))
