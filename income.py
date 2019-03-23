"""
Made by Ryan Wilson
https://github.com/onlinePB

This class describes a method of income and has two fields:
Name - the name of the income method (i.e. wages)
amountMonthly - the amount of money made per month through this income method
"""


class Income:

    """
    Initialises an Income object
    """
    def __init__(self, name="not set", amountMonthly=0.00):
        self.name = name
        self.amountMonthly = amountMonthly

    # This method returns the Income method's name
    def getName(self):
        return self.name

    # This method returns the amount earned through this income method monthly
    def getAmountMonthly(self):
        return self.amountMonthly

    # This method returns a string for testing
    def toString(self):
        return "Income{name: " + str(self.name) + ", amountMonthly: " + str(self.amountMonthly) + "}"