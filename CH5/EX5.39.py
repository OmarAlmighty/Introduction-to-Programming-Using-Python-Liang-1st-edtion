# 5.39 (Financial application: find the sales amount) You have just started a sales job in a
# department store. Your pay consists of a base salary plus a commission. The base
# salary is $5,000. The following scheme shows how to determine the commission rate:
# Your goal is to earn $30,000 a year. Write a program that finds out the minimum
# amount of sales you have to generate in order to make $30,000.

salesAmount = 1.01
commission = 0
while commission < 5000:
    if salesAmount > 10000:
        commission = 5000 * 1.08 + 5000 * 1.1 + (salesAmount - 10000) * 1.12

    elif salesAmount >= 5001:
        commission = 5000 * 1.08 + (salesAmount - 5000) * 1.10

    else:
        commission = salesAmount * 1.08
        salesAmount += 1.01
print(salesAmount)
