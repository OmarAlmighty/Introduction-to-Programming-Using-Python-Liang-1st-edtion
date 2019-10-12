# 6.29 (Financial: credit card number validation) Credit card numbers follow certain
# patterns: It must have between 13 and 16 digits, and the number must start with:
# ■ 4 for Visa cards
# ■ 5 for MasterCard credit cards
# ■ 37 for American Express cards
# ■ 6 for Discover cards
# In 1954, Hans Luhn of IBM proposed an algorithm for validating credit card numbers.
# The algorithm is useful to determine whether a card number is entered correctly
# or whether a credit card is scanned correctly by a scanner. Credit card
# numbers are generated following this validity check, commonly known as the
# Luhn check or the Mod 10 check, which can be described as follows (for illustration,
# consider the card number 4388576018402626):
# Return True if the card number is valid

def isValid(number):
    if getSize(number) >= 13 and getSize(number) <= 16:
        if prefixMatched(number, 4) or prefixMatched(number, 5) or \
                prefixMatched(number, 6) or getPrefix(number, 2) == 37:
            return True if (sumOfDoubleEvenPlace(number) +
                            sumOfOddPlace(number)) % 10 == 0 else False


def sumOfDoubleEvenPlace(number):
    numberList = []
    oddPlaceNumberList = []
    for i in range(len(list(str(number)))):
        numberList.append(int(list(str(number))[i]))
    numberList.reverse()
    for j in range(1, len(numberList), 2):
        oddPlaceNumberList.append(numberList[j])
    doubleOddPlaceNumber = [i * 2 for i in oddPlaceNumberList]
    digitOddPlaceNumber = [getDigit(i) for i in doubleOddPlaceNumber]
    return sum(digitOddPlaceNumber)


# Return this number if it is a digit, otherwise, return
# the sum of the digits
def getDigit(number):
    numberList = []
    for i in range(len(list(str(number)))):
        numberList.append(int(list(str(number))[i]))
    return sum(numberList)


# Return sum of odd place digits in number
def sumOfOddPlace(number):
    numberList = []
    totalNumber = 0
    for i in range(len(list(str(number)))):
        numberList.append(int(list(str(number))[i]))
    numberList.reverse()
    for j in range(0, len(numberList), 2):
        totalNumber += numberList[j]
    return totalNumber


# Return true if the digit d is a prefix for number
def prefixMatched(number, d):
    return True if int(str(number)[0]) == d else False


# Return the number of digits in d
def getSize(number):
    return len(str(number))


# Return the first k number of digits from number. If the
# number of digits in number is less than k, return number
def getPrefix(number, k):
    if len(str(number)) <= k:
        return number
    else:
        return int(str(number)[0:k])


def main():
    num = eval(input("Enter credit card number: "))
    print(isValid(num))


main()
