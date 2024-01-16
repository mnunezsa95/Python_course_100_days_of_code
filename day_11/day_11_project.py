# ------------------------------------------------------------------------------------------------ #
#                                          BlackJack Game                                          #
# ------------------------------------------------------------------------------------------------ #

from functools import reduce
from day_11_project_art import logo
import random
import os


def cls():
    """Clears the terminal"""
    os.system("cls" if os.name == "nt" else "clear")


def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(card_list):
    """Take a list of cards and return the score calculated from the cards"""
    result = reduce(lambda x, y: x + y, card_list)
    if result == 21 and len(card_list) == 2:
        return 0
    elif result > 21 and 11 in card_list:
        card_list.remove(11)
        card_list.append(1)
    return result


def compare(user_score, computer_score):
    """Takes in the user score and computer score and returns a winner"""
    if user_score == computer_score:
        return "It's a draw! 🤝"
    elif computer_score == 0:
        return "The dealer hit blackjack, you lose! 😭"
    elif user_score == 0:
        return "You hit blackjack, you win! 💰"
    elif user_score > 21:
        return "You busted, the dealer wins! 😭"
    elif computer_score > 21:
        return "Dealer busted, you win! 💰"
    elif computer_score > user_score:
        return "Dealer wins! 😭"
    else:
        return "You win! 💰"


def play_blackjack():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score is {user_score}")
        print(f"Dealer's first card: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            should_continue = input(
                "Do you want to draw another card? Type 'y' or 'n'. "
            )
            if should_continue == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # While the score is less than 17 or dealer has blackjack, will draw another card
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"The dealer's hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of blackjack? Type 'y' or 'n'. ") == "y":
    cls()
    play_blackjack()
