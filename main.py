"""
Made by Ryan Wilson
https://github.com/onlinePB
"""
from userInput import *
from income import *

incomeMethods = []
expenses = []
running = True

while running:

    # ========== COLLECT INCOME METHODS
    collectingIncomeMethods = True
    print("\n===[ INCOME METHODS ]===")
    while collectingIncomeMethods:
        incomeName = str(input("Enter the name of this income method:\n"))
        incomeAmount = UserInput.getFloat("Enter the amount you make per month through this method:\n")
        incomeMethods.append(Income(incomeName, incomeAmount))

        if not UserInput.yesOrNo("Do you want to add another income method?\n[Y]es or [N]o: "):
            collectingIncomeMethods = False

    # ========== COLLECT EXPENSES
    collectingExpenses = True
    print("\n===[ EXPENSES ]===")
    while collectingExpenses:
        expenseName = str(input("Enter the name of this expense:\n"))
        expenseAmount = -UserInput.getFloat("Enter the amount you spent per month on this expense:\n")
        expenses.append(Income(expenseName, expenseAmount))

        if not UserInput.yesOrNo("Do you want to add another expense?\n[Y]es or [N]o: "):
            collectingExpenses = False
