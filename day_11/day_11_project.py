# ------------------------------------------------------------------------------------------------ #
#                                          BlackJack Game                                          #
# ------------------------------------------------------------------------------------------------ #

from functools import reduce
from day_11_project_art import logo
import random

user_cards = []
computer_cards = []
is_game_over = False


def calculate_score(card_list):
    """Take a list of cards and return the score calculated from the cards"""
    result = reduce(lambda x, y: x + y, card_list)
    if result == 21 and len(card_list) == 2:
        return 0
    elif result > 21 and 11 in card_list:
        card_list.remove(11)
        card_list.append(1)
    return result


def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())


while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, current score is {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")
    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        should_continue = input("Do you want to draw another card? Type 'y' or 'n'. ")
        if should_continue == "y":
            user_cards.append(deal_card())
        else:
            is_game_over = True

while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
