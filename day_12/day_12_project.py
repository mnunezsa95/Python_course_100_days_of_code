# ------------------------------------------------------------------------------------------------ #
#                                     The Number Guessing Game                                     #
# ------------------------------------------------------------------------------------------------ #

from day_12_project_art import logo
import random
import os

# Global Constant
EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5


def cls():
    """Clears the terminal"""
    os.system("cls" if os.name == "nt" else "clear")


def check_answer(user_guess, answer, num_attempts):
    """Checks answer against guess. Returns the number of turns remaining"""
    if user_guess > answer:
        print("Too high.")
        return num_attempts - 1
    elif user_guess < answer:
        print("Too low.")
        return num_attempts - 1
    else:
        print(f"You got it! The number was {answer}")


def set_difficulty():
    """Sets the difficulty level. Returns the number of attempts based on difficulty level selected"""
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        return EASY_LEVEL_ATTEMPTS
    else:
        return HARD_LEVEL_ATTEMPTS


def play_game():
    cls()
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100")
    answer = random.randint(1, 100)
    num_attempts = set_difficulty()
    guess = 0
    while guess != answer:
        print(f"You have {num_attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        num_attempts = check_answer(
            user_guess=guess, answer=answer, num_attempts=num_attempts
        )
        if num_attempts == 0:
            print()
            print("You've run out of guesses. You lose")
            return
        elif guess != answer and num_attempts > 0:
            print("Guess again")
            print()


play_game()
