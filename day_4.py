# ------------------------------------------------------------------------------------------------ #
#                         Section 4: Day 4 - Randomization and Python Lists                        #
# ------------------------------------------------------------------------------------------------ #

### Random Module
import random # the random module needs to be impprted

random_integer = random.randint(1, 10) # randint() creates a random number between a and b (including a and b)
print(random_integer)

random_float = random.random() # random() creates a random float number between 0 and 1 (not including 1)
print(random_float)

# multiplication is used to creating larger random floating point numbers and integers
number_between_zero_and_five = random_float * 5
print(number_between_zero_and_five)

### Lists
'''
- A list is a data structure (a way to organize data)
- Lists allow for storing of multiple data points
- Syntax:
--- Values are separated by commas between square brackets
'''

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
print(states_of_america[0]) # items in a list can be accessed by using their index
print(states_of_america[2])
print(states_of_america[-2]) # negative indexes are used to access items from right to left (end of list)

states_of_america[1] = "Pencilvania" # items can be accessed and altered using the index
states_of_america.append("Marlonland") # append() will add an item at the end of a list
states_of_america.extend(["Pennyland", "Harperland"])
print(len(states_of_america)) # len() returns the length of a list
print(states_of_america)

### IndexErrors
'''
IndexErrors: list index out of range 
---Usually happens when an index that does not exist is used
'''

# Nested Lists
fruits = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables =  ["Tomatoes", "Celery", "Potatoes"]
dirty_dozen = [fruits, vegetables]

print(dirty_dozen)

