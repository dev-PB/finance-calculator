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
                print("\nInvalid input! Please enter [Y]es or [N]o!")
                continue

            if userAnswer != "yes" and userAnswer != "y" and userAnswer != "no" and userAnswer != "n":
                print("\nInvalid input! Please enter [Y]es or [N]o!")
                continue

            # Returns true if yes, or false if no
            else:
                if userAnswer == "yes" or userAnswer == "y":
                    return True
                else:
                    return False


    """
    This method will ask the user for a float value, check that their input is
    a float value, and then return that value if it is
    """
    @staticmethod
    def getFloat(question):
        while True:
            try:
                userAnswer = float(input(question))

            except ValueError:
                print("\nInvalid input! Please enter a correct number!")
                continue

            else:
                return userAnswer

    """
    This method will take in a filename, check that it doesnt contain any reserved
    characters, and then returns it
    """
    @staticmethod
    def getFileName(question):
        while True:
            try:
                userAnswer = str(input(question))

            except ValueError:
                print("\nInvalid input! Please enter a correct filename!")
                continue

            if ":" in userAnswer or "/" in userAnswer or "\\" in userAnswer or ">" in userAnswer or "<" in userAnswer or "*" in userAnswer or '"' in userAnswer or "?" in userAnswer or "|" in userAnswer:
                print('\nInvalid input! You can\'t have /, \\, >, <, *, ?, ", : or | in a filename!')
                continue

            else:
                return userAnswer
