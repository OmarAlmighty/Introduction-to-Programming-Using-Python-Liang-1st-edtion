# 12.3 (Game: ATM machine) Use the Account class created in Exercise 7.3 to simulate
# an ATM machine. Create ten accounts in a list with the ids 0, 1, ..., 9, and an initial
# balance of $100. The system prompts the user to enter an id. If the id is entered
# incorrectly, ask the user to enter a correct id. Once an id is accepted, the main
# menu is displayed as shown in the sample run. You can enter a choice of 1 for
# viewing the current balance, 2 for withdrawing money, 3 for depositing money,
# and 4 for exiting the main menu. Once you exit, the system will prompt for an id
# again. So, once the system starts, it won’t stop.

class Account:
    def __init__(self, id=0, balance=100, annualIntersetRate=0):
        self.__id = id
        self.__balance = balance
        self.__annualIntersetRate = annualIntersetRate

    def getId(self):
        return self.__id

    def getBalance(self):
        return self.__balance

    def getAnnualIntersetRate(self):
        return self.__annualIntersetRate

    def setId(self, id):
        self.__id = id

    def setBalance(self, balance):
        self.__balance = balance

    def setAnnualIntersetRate(self, annualIntersetRate):
        self.__annualIntersetRate = annualIntersetRate

    def getMonthlyInterestRate(self):
        return (self.__annualIntersetRate / 12) / 100

    def getMonthlyInterest(self):
        return self.__balance * self.getMonthlyInterestRate()

    def deposit(self, balance):
        self.__balance += balance

    def withdraw(self, amount):
        self.__balance -= amount


def main():
    accounts = []
    for i in range(10):
        ac = Account(i)
        accounts.append(ac)

    id = eval(input("Enter an account id: "))

    while (True):
        if 0 <= id <= 9:
            print("Main menu")
            print("1: check balance\n2: withdraw\n3: deposit\n4: exit")

            choice = int(input(""))
            if choice == 1:
                print("The balance is", accounts[id].getBalance(),"\n")
            elif choice == 2:
                amount = eval(input("Enter an amount to withdraw: \n"))
                accounts[id].withdraw(amount)
            elif choice == 3:
                amount = eval(input("Enter an amount to deposit: \n"))
                accounts[id].deposit(amount)
            elif choice == 4:
                break
        else:
            print("Enter a correct ID")

main()