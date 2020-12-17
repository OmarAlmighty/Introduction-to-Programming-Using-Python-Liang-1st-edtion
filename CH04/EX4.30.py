# 4.30 (Current time) Revise Programming Exercise 2.18 to display the hour using a 12-
# hour clock.
import time

offest = eval(input("Enter the time zone offset to GMT: "))
currentTime = time.time()
totalSeconds = int(currentTime)
currentSecond = totalSeconds % 60
totalMinutes = totalSeconds // 60
currentMintute = totalMinutes % 60
totalHours = totalMinutes // 60
currentHour = totalHours % 24
currentHour += offest

if currentHour > 12:
    currentHour %= 12
    print("The current time is", currentHour, ":", currentMintute, ":", currentSecond, "PM")
else:
    print("The current time is", currentHour, ":", currentMintute, ":", currentSecond, "AM")
