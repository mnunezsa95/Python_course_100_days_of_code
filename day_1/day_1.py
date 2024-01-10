# ------------------------------------------------------------------------------------------------ #
#                Section 1: Day 1 - Working with variables in Python to manage data                #
# ------------------------------------------------------------------------------------------------ #

### print() function
print("Hello, World!") # print() function prints to the console
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')") # Using different types of outside quotes to print the inner quotes

### String manipulation
print("Hello, World!\nHello, World!\nHello, World!") # \n breaks a new line

### String concatenation
print("Hello" + "Marlon") # + will add two strings together
print("Hello" + " Marlon") # manually adding a space

### input() function
input("What is your name? ") # input() function allows for user input in the terminal
print("Hello " + input("What is your name? ") + "!") # Nesting input() inside of print()

### Variables
name = input("What is your name?") # assigning the result of the input to a var
print(name) # var can be accessed later on
name2 = "Jack" # assigning a value to name2
name2 = "Angela" # reassigning name2 to a different value
print(name2)

### Rules for naming variables
# 1) Make name specific
# 2) Separate words using an underscore (_)
# 3) Numbers can ONLY be at the end (var cannot start w/ a num)
# 4) Do not use reserved words
