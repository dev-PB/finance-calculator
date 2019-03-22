"""
This class will handle input validation on the user's input.
"""


class UserInput:

    """
    This method takes in a yes or no question, will loop until the user enters
    a correct value, and then returns true or false for yes or no.
    """
    @staticmethod
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

            # Returns true if yes, or false if no
            else:
                if userAnswer == "yes" or userAnswer == "y":
                    return True
                else:
                    return False