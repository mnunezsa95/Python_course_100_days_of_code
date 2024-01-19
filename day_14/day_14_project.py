# ------------------------------------------------------------------------------------------------ #
#                                          Higher or Lower                                         #
# ------------------------------------------------------------------------------------------------ #

import random
import os
from day_14_project_art import logo, vs
from day_14_project_data import data

# system function to clear()
def cls():
    """Clears the terminal"""
    os.system("cls" if os.name == "nt" else "clear")

# Generate a random account from the game data.
def get_random_account():
    return random.choice(data)

# Format account data into printable format.
def format_person(person, position):
    print(f"Compare {position}: {person["name"]}, a(n) {person["description"]}, from {person["country"]}")

# Check if user is correct
def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"     

def play_game():
    cls()
    print(logo) # Print logo
    score = 0 # Generate score variable
    should_game_continue = True # variable for loop
    person_a = get_random_account()
    person_b = get_random_account()
    
    while should_game_continue:
    # Generate people & follower
        person_a = person_b
        person_b = get_random_account()
        
        while person_a == person_b:
            person_b = get_random_account()
            
        format_person(person_a, "A")
        print(vs)
        format_person(person_b, "B")
        
        
        user_guess = input("Who has more followers? Type 'A' or 'B': ").lower() # Ask user for a guess.
        person_a_followers = person_a["follower_count"]
        person_b_followers = person_b["follower_count"]
        is_correct = check_answer(user_guess, person_a_followers ,person_b_followers)
        
        cls()
        print(logo) # Print logo
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            should_game_continue = False

        # Make game repeatable.
        # Make B become the next A.
        # Clear screen between rounds.

play_game()
