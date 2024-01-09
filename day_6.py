
# ------------------------------------------------------------------------------------------------ #
#                           Python Functions, While Loops and Indentation                          #
# ------------------------------------------------------------------------------------------------ #

### Functions
# Built-in functions: https://docs.python.org/3/library/functions.html
print("Hello") # print() function
len("Hello") # len() function
range(0, 10) # range() function

# Creating functions
#--def is a keyword used to define a function
#--functions should be named
#--parentheses are used to pass in inputs
#--colon is used to end the definition

def my_function():
    print("Hello")
    print("Bye")

my_function() # calling the function

### Indentation
# Python Styling Guide: https://peps.python.org/pep-0008/
sky = ""
def my_function2(): 
    if sky == "clear": # the function block's code should be indented
        print("blue") # the conditional block's code should be indented
    elif sky == "cloudy":
        print("grey")
    print("day") # this print() statement is part of the function block but not conditional block
print("Weather") # this print() statement is not part of the function block

