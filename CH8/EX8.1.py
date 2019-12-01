# 8.1 (Check SSN) Write a program that prompts the user to enter a Social Security
# number in the format ddd-dd-dddd, where d is a digit. The program displays
# Valid SSN for a correct Social Security number or Invalid SSN otherwise.

ssn = input("Enter your social security number (ddd-dd-dddd): ")
s1 = ssn[0:3]
s2 = ssn[4:6]
s3 = ssn[7:11]

if (len(s1)+len(s2)+len(s3) == 9) and s1.isdigit() and s2.isdigit() and s3.isdigit():
    print("SSN is valid")
else:
    print("SSN is not valid")
