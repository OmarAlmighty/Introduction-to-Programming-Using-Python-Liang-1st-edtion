# 7.2 (The Stock class) Design a class named Stock to represent a company’s stock
# that contains:
# ■ A private string data field named symbol for the stock’s symbol.
# ■ A private string data field named name for the stock’s name.
# ■ A private float data field named previousClosingPrice that stores the stock
# price for the previous day.
# ■ A private float data field named currentPrice that stores the stock price for
# the current time.
# ■ A constructor that creates a stock with the specified symbol, name, previous
# price, and current price.
# ■ A get method for returning the stock name.
# ■ A get method for returning the stock symbol.
# ■ Get and set methods for getting/setting the stock’s previous price.
# ■ Get and set methods for getting/setting the stock’s current price.
# ■ A method named getChangePercent() that returns the percentage changed
# from previousClosingPrice to currentPrice.
# Draw the UML diagram for the class, and then implement the class. Write a test
# program that creates a Stock object with the stock symbol INTC, the name Intel
# Corporation, the previous closing price of 20.5, and the new current price
# of 20.35, and display the price - change percentage.
from CH7.Stock import Stock

stock = Stock('INTC', 'Intel corporation', 20.5, 20.35)

previousPrice = stock.getPreviousStockPrice()
currentPrice = stock.getStockCurrentPrice()

change = format((currentPrice - previousPrice) * 100 / previousPrice, "5.2f") + "%"

print("Stock Name:", stock.getStockName(), "\nChanged price Percentage="
      , change)
