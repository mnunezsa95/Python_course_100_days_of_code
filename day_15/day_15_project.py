# ------------------------------------------------------------------------------------------------ #
#                                      Coffee Machine Project                                      #
# ------------------------------------------------------------------------------------------------ #
import os

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 500,
    "milk": 300,
    "coffee": 150,
}

# Global variables
profit = 0 # holds the profit made by the machine
is_on = True # boolean to signify if machine is on

def cls():
    """Clears the terminal"""
    os.system("cls" if os.name == "nt" else "clear")

def print_report():
    """Prints a report of the resources"""
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money: ${profit}")

def check_resources(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient"""
    for item in order_ingredients: # loop through order_ingredients
        if order_ingredients[item] > resources[item]: # check if the amount is greater than resources dict with same key
            print(f"Sorry there is not enough {item}.")
            return False # evaluate to False
    return True # otherwise evaluate to True

def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins: ")
    total = int(input("How many quarters?: ")) * .25
    total += int(input("How many dimes?: ")) * .10
    total += int(input("How many nickels?: ")) * .05
    total += int(input("How many pennies?: ")) * .01
    return total

def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if drink_cost > money_received:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")

cls() # clear terminal
while is_on:
    prompt_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if prompt_choice == "off": # Check if user entered "off"
        print("Turning off...")
        print("Off")
        is_on = False
    elif prompt_choice == "report": # Check if user entered "report"
        print_report() # print the report
    else:
        drink = MENU[prompt_choice] # assign the prompt_choice to drink variable
        if check_resources(drink["ingredients"]): # check resources
            payment = process_coins() # assign the total coins processed to payment
            if is_transaction_successful(payment, drink["cost"]): # Check if transaction is successful
                make_coffee(prompt_choice, drink["ingredients"])

