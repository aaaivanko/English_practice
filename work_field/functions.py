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
        print(f"Month and number in Ukrainian language:"
              f" {MONTHS_UA[random_month_number].title()} - {random_month_number}")
        # receive answer from user
        user_answer = input("Please write this month on english or press q to quit: ")
        # if user want to exit break the program
        if user_answer == 'q':
            break
        # check for correct answer
        elif user_answer.lower() == MONTHS_ENG[random_month_number].lower():
            print("Well done! You were correct!\n"
                  f"{MONTHS_ENG[random_month_number].title()} == {MONTHS_UA[random_month_number].title()} "
                  f"{random_month_number}\n"
                  f"Play again? - press a if not press q")
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


def ua_language_practice():
    """Checking month knowledge in English language."""
    while True:
        # retrieve random number
        random_month_number = retrieve_random_month()
        print(f"Month and number in English language:"
              f" {MONTHS_ENG[random_month_number].title()} - {random_month_number}")
        # receive answer from user
        user_answer = input("Please write this month on ukrainian or press q to quit: ")
        # if user want to exit break the program
        if user_answer == 'q':
            break
        # check for correct answer
        elif user_answer.lower() == MONTHS_UA[random_month_number].lower():
            print("Well done! You were correct!\n"
                  f"{MONTHS_UA[random_month_number].title()} == {MONTHS_ENG[random_month_number].title()} "
                  f"{random_month_number}\n"
                  f"Play again? - press a if not press q")
            repeat_game = input('Play again?: ')
            if repeat_game == 'q':
                break
            else:
                continue
        # check for not correct answer
        elif user_answer.lower() != MONTHS_UA[random_month_number].lower():
            print(f"Sorry, you were not correct."
                  f"The correct answer is: {MONTHS_UA[random_month_number].title()}\n"
                  f"Bare that in mind and next time try harder!")
            repeat_game = input('Play again? q - no a - yes: ')
            if repeat_game == 'q':
                break
            else:
                continue
