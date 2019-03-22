"""
Made by Ryan Wilson
https://github.com/onlinePB
"""
from userInput import *
from income import *

incomeMethods = []
running = True

while running:

    # ========== COLLECT INCOME METHODS
    collectingIncomeMethods = True
    print("===[ INCOME METHODS ]===")
    while collectingIncomeMethods:
        incomeName = str(input("Enter the name of this income method:\n"))
        incomeAmount = UserInput.getFloat("Enter the amount you make per month through this method:\n")
        incomeMethods.append(Income(incomeName, incomeAmount))

        if not UserInput.yesOrNo("Do you want to add another income method?\n[Y]es or [N]o: "):
            collectingIncomeMethods = False
