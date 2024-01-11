# ------------------------------------------------------------------------------------------------ #
#                                        Function Parameters                                       #
# ------------------------------------------------------------------------------------------------ #

# Functions with inputs
# --Functions are helpful for performing repetitive actions
# --Parameters are variables used when defining the function
# --Arguments are the values of the data used when the function is called

# functions begin with the def keyword
# parameters allow for the param to be passed into function for use
def greet(name, birth_country, current_city):
    print(f"My name is {name}.")
    print(f"I am from {birth_country}.")
    print(f"I live in {current_city}.")


# calling the function with the arguments
greet("Marlon", "Costa Rica", "Boston")

# Positional and Keyword Arguments
# --Positional arguments are arguments passed in order to the parameters when calling the function
# --Keyword arguments are arguments assigned to the parameter name when calling the function

# Using keyword arguments


def greet_with_keyword_arguments(name, birth_country, current_city):
    print(f"My name is {name}.")
    print(f"I am from {birth_country}.")
    print(f"I live in {current_city}.")


greet(current_city="Boston", name="Harper", birth_country="USA")

# Example 1: Prime Number Checker


def prime_checker(number):  # function for checking if a number is prime
    is_prime = True  # variable initialized as true
    for i in range(2, number):  # looping to every number between 2 and 'number'
        if number % i == 0:  # if the number is divisible by any number starting from 2
            is_prime = False  # set is_prime to false
    if is_prime:  # if is_prime is true, print a statement
        print("It's a prime number.")
    else:  # if is_prime is false, print a statement
        print("It's not a prime number.")


prime_checker(4)  # Output: It's not a prime number.
prime_checker(5)  # Output: It's a prime number.
