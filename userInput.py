"""
This class will handle input validation on the user's input.
"""

class userInput:

    @staticmethod
    """
    This method takes in a yes or no question, will loop until the user enters
    a correct value, and then returns that value.
    """
    def yesOrNo(question):

        while True:
            # Asks the question
            try:
                userAnswer = str(input(question)).lower()

            # Checks that the input is valid
            except ValueError:
                print("Invalid input! Please enter [Y]es or [N]o!\n")
                continue

            if userAnswer != "yes" and userAnswer != "y" and userAnswer != "no" and userAnswer != "n":
                print("Invalid input! Please enter [Y]es or [N]o!\n")
                continue

            # Returns the user's input
            else:
                return userAnswer