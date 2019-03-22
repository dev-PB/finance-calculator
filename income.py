"""
This class describes a method of income and has two fields:
Name - the name of the income method (i.e. wages)
amountMonthly - the amount of money made per month through this income method
"""


class Income:

    def __init__(self, name="not set", amountMonthly=0.00):
        self.name = name
        self.amountMonthly = amountMonthly

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getAmountMonthly(self):
        return self.amountMonthly

    def setAmountMonthly(self, newAmount):
        amountMonthly = newAmount

    def toString(self):
        return "Income{name: " + str(self.name) + ", amountMonthly: " + str(self.amountMonthly) + "}"