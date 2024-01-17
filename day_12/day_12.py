# ------------------------------------------------------------------------------------------------ #
#                                               Scope                                              #
# ------------------------------------------------------------------------------------------------ #

# The
### Scope ###
# -scope is like a tree in your yard vs a tree on sidewalk;
# --tree in yard can only be accessed by you
# --tree on sidewalk can be accessed by anyone

enemies = 1  # setting enemies to 1


def increase_enemies():
    enemies = 2  # increasing enemies to 2
    print(f"enemies inside function: {enemies}")  # will print a value of 2 for enemies


increase_enemies()
print(f"enemies outside function: {enemies}")  # will print a value of 1 for enemies


### Local Scope ###
# -local scope exists within functions
def drink_potion():
    potion_strength = 2
    print(potion_strength)


drink_potion()  # will print a value of 2 for enemies

# This will lead to a NameError because 'potion_strength' only exists in the function
# print(potion_strength)


### Global Scope ###
# -Global scope is accessible by all functions (exists in the global space)
player_health = 10


def drink_potion2():
    potion_strength = 2
    print(player_health)  # will print a value of 10 for 'player_health'


drink_potion2()


### Namespace ###
# -Anything assigned to a variable has a namespace
# -The namespace is valid in certain scopes

### Block Scope ###
# -Python DOES NOT have block scope
enemies2 = ["zombie", "skeleton", "alien"]
game_level = 3
if game_level < 5:
    new_enemy = enemies2[0]  # create new_enemy variable inside the if statement

print(new_enemy)  # new_enemy is printed because Python does not have block scope
# if the 'if statement' were inside a function, new_enemy would NOT be able to be accessed b/c it would have local scope


### Modifying a Global Variable ###
# -SHOULD NOT call local variables and global variables the same thing
enemies3 = 1  # a global variable


#! TRY NOT to modify global scope
def increase_enemies():
    global enemies3  # the 'global' keyword designates the fn to look at global scope
    enemies3 += 1  # changing the global variable
    print(f"enemies inside function: {enemies3}")  # prints "2"


increase_enemies()
print(f"enemies outside function: {enemies3}")  # prints "1"


#! Instead try to use return statements
def increase_enemies2():
    return enemies3 + 1  # returning the global variable with a change


enemies3 = increase_enemies2()  # assigning the return of the function to enemies3


### Python Constants and Global Scope ###
# - Global constants are variables declared that will never be changed
# - Naming convention for global variables: all uppercase, separated by underscores
PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "#yu_angela"
