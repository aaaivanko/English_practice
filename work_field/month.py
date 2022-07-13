from random import randint
from constants import MONTHS_ENG, MONTHS_UA


def retrieve_random_month():
    """Generate random number from 1 to 12."""

    random_number = randint(1, 12)
    return random_number


def en_language_practice():
    """Checking month knowledge in English language."""
    while True:
        # retrieve random number
        random_month_number = retrieve_random_month()
        print(f"Month ua:{MONTHS_UA[random_month_number].title()}   {random_month_number}")
        # receive answer from user
        user_answer = input("Please write this month on english or pess q to quit: ")
        # if user want to exit break the program
        if user_answer == 'q':
            break
        # check for correct answer
        elif user_answer.lower() == MONTHS_ENG[random_month_number].lower():
            print("Well done! You were correct! Play again? - press a if not press q")
            repeat_game = input('Play again?: ')
            if repeat_game == 'q':
                break
            else:
                continue
        # check for not correct answer
        elif user_answer.lower() != MONTHS_ENG[random_month_number].lower():
            print(f"Sorry, you were not correct."
                  f"The correct answer is: {MONTHS_ENG[random_month_number].title()}\n"
                  f"Bare that in mind and next time try harder!")
            repeat_game = input('Play again? q - no a - yes: ')
            if repeat_game == 'q':
                break
            else:
                continue


class Word:
    """This class will check how well do you know months on English."""

    def __init__(self):
        """Initializing two languages which we will use in checker."""
        self.language = ['English', 'Ukrainian']

    def choose_language(self):
        print("What language do you want to practice?: 0 - en 1 - ua")
        user_answer = input(': ')
        if user_answer == '0':
            print(f"You choose {self.language[0]}\n"
                  f"Lets start the test")
            en_language_practice()

        elif user_answer == '1':
            print(f"You choose {self.language[1]}")
        else:
            print("Sorry, but you choose the wrong number.\n"
                  "Please repeat again!")


new_word = Word()

new_word.choose_language()



