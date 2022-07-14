from functions import en_language_practice, ua_language_practice


class Word:
    """This class will check how well do you know months on English."""

    def __init__(self):
        """Initializing two languages which we will use in checker."""
        self.language = ['English', 'Ukrainian']

    def choose_language(self):
        print("Hello, there.\nWhat language do you want to practice?:\nPress 0 for English\nPress 1 for Ukraine")
        user_answer = input(':')
        if user_answer == '0':
            print(f"You choose {self.language[0]}\n"
                  f"Lets start the test")
            # start function for english language practice
            en_language_practice()

        elif user_answer == '1':
            print(f"You choose {self.language[1]}")
            # start function for ukrainian language practice
            ua_language_practice()
        else:
            print("Sorry, but you choose the wrong number.\n"
                  "Please repeat again!")
