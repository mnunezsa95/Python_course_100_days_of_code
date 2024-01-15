# ------------------------------------------------------------------------------------------------ #
#                                           Blind Auction                                          #
# ------------------------------------------------------------------------------------------------ #

import os
from day_9_project_art import logo


def cls():
    os.system("cls" if os.name == "nt" else "clear")


auction_bids = {}
is_auction_finished = False
highest_bid = 0
winner = ""

print(logo)
print("Welcome to the the secret auction program.")

while not is_auction_finished:
    name = input("What is your name?: ")
    user_bid = int(input("What's your bid? "))
    auction_bids[name] = user_bid
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. ")
    if should_continue == "no":
        is_auction_finished = True
        for bidder in auction_bids:
            if auction_bids[bidder] > highest_bid:
                highest_bid = auction_bids[bidder]
                winner = bidder
        print(f"The winner of the auction is {winner} with a bid of ${highest_bid}.")
    elif should_continue == "yes":
        cls()
