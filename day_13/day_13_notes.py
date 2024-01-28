# ------------------------------------------------------------------------------------------------ #
#                        Debugging: How to Find and Fix Errors in your Code                        #
# ------------------------------------------------------------------------------------------------ #


### Steps to Identifying Bugs
# 1- Describe the problem
# -- What is the for loop doing? --> Iterating from number 1 to 19
# -- When is the function meant to print "you got it"? --> When i = 20
# -- What assumptions are making about i = 20? i will never be reached


# Error: "You got it" does not print()
def my_function():
    for i in range(1, 21):  # Fix: change 20 to 21; the range() fn omits the upper-bound
        if i == 20:
            print("You got it")


my_function()

# 2- Reproduce the Bug
from random import randint

# Error: This code sometimes works, sometimes it doesn't
dice_imgs = ["1", "2", "3", "4", "5", "6"]
dice_num = randint(0, 5)  # Fix: change the randint parameters from 1, 6 to 0, 5
print(dice_imgs[dice_num])  # 0,5 will align with the index of dice_num


# 3 - Play Computer
# Error: if input is 1994, it doesn't print "You are a millennial" or "You are Gen Z."
year = int(input("What's your year of birth? "))
if year > 1980 and year < 1994:
    print("You are a millennial.")
elif year >= 1994:  # Fix: > 1994 to >= 1994
    print("You are Gen Z.")

# 4 - Fix the Errors
# Error: Throws an IndentationError, TypeError, age is not printing
age = int(input("How old are you? "))  # Fix: convert input to int()
if age > 18:
    # add the f-string
    print(f"You can drive at age {age}")  # Fix: indent this line ();

# 5 - Print is your friend
# Error: total_words always prints as 0
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
# Fix: change equality operator to assign operator
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)


# 6 - Use a Debugger
# Error: only one value (26) is printed instead of 6
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)  # move the append() line inside the loop
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])

# 7 - Take a break
# - Give the brain some time to rest

# 8 - Ask someone
# - Get a fresh set of eyes

# 9 - Run often
# - Run the code frequently (DO NOT wait until done)

# 10 - Ask StackOverflow
# - Take StackOverflow to ask important questions
