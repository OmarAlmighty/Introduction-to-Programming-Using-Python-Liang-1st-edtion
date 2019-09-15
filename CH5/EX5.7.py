# 5.7 (Use trigonometric functions) Print the following table to display the sin value
# and cos value of degrees from 0 to 360 with increments of 10 degrees. Round the
# value to keep four digits after the decimal point.
# Degree Sin Cos
# 0 0.0000 1.0000
# 10 0.1736 0.9848
# ...
# 350 -0.1736 0.9848
# 360 0.0000 1.0000
import math

print(format("Degree","10s"), format("Sin", "8s"), "Cos")
#
for i in range(0, 361, 10):
    sin = math.sin(math.radians(i))
    cos = math.cos(math.radians(i))
    print(format(i,"3.0f"),format(sin,"13.4f"),format(cos,"8.4f"))
