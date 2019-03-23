"""
Made by Ryan Wilson
https://github.com/onlinePB
"""
from userInput import *
from income import *
from fileHandler import *
import csv


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

    # ========== GET TOTALS
    incomeTotal = 0
    expenseTotal = 0

    for method in incomeMethods:
        incomeTotal += method.getAmountMonthly()

    for expense in expenses:
        expenseTotal += expense.getAmountMonthly()

    # ========== GET PERCENTAGES
    incomePercentages = []
    expensePercentages = []

    for method in incomeMethods:
        incomePercentages.append((method.getAmountMonthly() / incomeTotal)*100)

    for expense in expenses:
        expensePercentages.append((expense.getAmountMonthly() / expenseTotal*100))

    # ========== FORMAT FOR CSV
    incomeData = [["Income Method", "Amount", "Percentage"]]
    expenseData = [["Expense", "Amount", "Percentage"]]
    for i in range(len(incomeMethods)):
        incomeData.append([incomeMethods[i].getName(), incomeMethods[i].getAmountMonthly(), str(incomePercentages[i]) + "%"])

    incomeData.append(["Total:", incomeTotal, "100%"])
    incomeData.append(["", "", ""])
    for i in range(len(expenses)):
        expenseData.append([expenses[i].getName(), expenses[i].getAmountMonthly(), str(expensePercentages[i]) + "%"])
    expenseData.append(["Total:", expenseTotal, "100%"])

    FileHandler.export("output", incomeData + expenseData)