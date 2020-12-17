# 8.14 (Financial: credit card number validation) Rewrite Exercise 6.29 using a string
# input for a credit card number.


def main():
    number = input("Enter a credit card number as a string: ").strip()

    if isValid(number):
        print(number + " is valid")
    else:
        print(number + " is invalid")


# Return true if the card number is valid
def isValid(number):
    return (number.startswith("4") or number.startswith("5") or
            number.startswith("6") or number.startswith("37")) and \
           (sumOfDoubleEvenPlace(number) + sumOfOddPlace(number)) % 10 == 0


# Get the result from Step 2
def sumOfDoubleEvenPlace(cardNumber):
    result = 0

    for i in range(len(cardNumber) - 2, -1, - 2):
        result += getDigit(int(cardNumber[i]) * 2)

    return result


# Return this number if it is a single digit, otherwise, return
# the sum of the two digits
def getDigit(number):
    return number % 10 + (number // 10 % 10)


# Return sum of odd place digits in number
def sumOfOddPlace(cardNumber):
    result = 0

    for i in range(len(cardNumber) - 1, -1, -2):
        result += int(cardNumber[i])

    return result


main()
