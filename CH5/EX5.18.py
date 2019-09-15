# 5.18 (Find the factors of an integer) Write a program that reads an integer and displays
# all its smallest factors, also known as prime factors. For example, if the input integer
# is 120, the output should be as follows:
# 2, 2, 2, 3, 5

num = int(input("Enter an integer: "))
halfNum = num // 2
while num > 2:
    if num % halfNum == 0:
        print(str(num // halfNum), end='')
        num = halfNum
        halfNum = num // 2
        if num > 2:
            print(", ", end='')
    else:
        halfNum -= 1
