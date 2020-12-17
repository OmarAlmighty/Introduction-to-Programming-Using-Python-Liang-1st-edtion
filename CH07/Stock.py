class Stock:
    def __init__(self, symbol, name, previousClosingPrice, currentPrice):
        self.__symbol = symbol
        self.__name = name
        self.__previousClosingPrice = previousClosingPrice
        self.__currentPrice = currentPrice

    def getStockName(self):
        return self.__name

    def getStockSymbol(self):
        return self.__symbol

    def getPreviousStockPrice(self):
        return self.__previousClosingPrice

    def setPreviousStockPrice(self, previousClosingPrice):
        self.__previousClosingPrice = previousClosingPrice

    def getStockCurrentPrice(self):
        return self.__currentPrice

    def setStockCurrentPrice(self, currentPrice):
        self.__currentPrice = currentPrice
