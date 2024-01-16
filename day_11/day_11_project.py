# ------------------------------------------------------------------------------------------------ #
#                                          BlackJack Game                                          #
# ------------------------------------------------------------------------------------------------ #

from day_11_project_art import logo
import random

user_cards = []
computer_cards = []


def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
