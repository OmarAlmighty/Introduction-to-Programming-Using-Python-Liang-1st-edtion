# 8.16 (Business: check ISBN-13) ISBN-13 is a new standard for identifying books. It
# uses 13 digits: d1d2d3d4d5d6d7d8d9d10d11d12d13. The last digit, is a checksum,
# which is calculated from the other digits using the following formula:
# 10 - (d1 + 3d2 + d3 + 3d4 + d5 + 3d6 + d7 + 3d8 + d9 + 3d10 + d11 + 3d12) % 10
# If the checksum is 10, replace it with 0. Your program should read the input as a
# string.

digits = input("Enter the first 12 digits of an ISBN-13 as a string: ")

checksum = 0
for i in range(12):
    checksum += int(digits[i]) * (1 if i % 2 == 0 else 3)

checksum = 10 - checksum % 10
if checksum == 10:
    digits +=  '0'
else:
    digits += str(checksum)

print("The ISBN-13 number is", digits)
