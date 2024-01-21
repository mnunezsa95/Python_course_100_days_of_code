# ------------------------------------------------------------------------------------------------ #
#                                    Object Oriented Programming                                   #
# ------------------------------------------------------------------------------------------------ #

### Procedural Programming
# - Procedural Programming is when one procedure (functions) lead to another procedure

### Object Oriented Programming
# - Allows for complex tasks to be separated into separate modules
# - Allows modules to become reusable
# - Allows code to become scalable

### OOP Classes and Objects
# - Attributes & methods
# -- Attributes -> a variable attached to particular object
# -- Method -> a function attached to a particular object
# - Classes can be used to generate several instances of an object

# * Creating an object from a class
# car = CarBlueprint()  # classes use use Pascal case
# car.speed  # accessing an attribute from the car object (car object is modeled from CarBlueprint)
# car.stop() # accessing a method from the car object (car object is modeled from CarBlueprint)


### Example: Using the Turtle() class
"""
from turtle import Turtle, Screen  # importing a module named Turtle

timmy = Turtle()  # creating an instance of the Turtle() class
timmy.shape("turtle")  # shape() is a method on the Turtle() class
timmy.color("coral")  # color() is a method on the Turtle() class
timmy.forward(100)  # forward() is a method on the Turtle() class

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()  # accessing a method on the screen() class
"""

### Adding Python Packages
# - Documentation for PrettyTable: https://pypi.org/project/prettytable/

from prettytable import PrettyTable  # importing PrettyTable class

table = PrettyTable()  # creating a table
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])  # adding column
table.add_column("Pokemon Type", ["Electric", "Water", "Fire"])  # adding column
table.align = "l"  # changing table alignment
table = table.get_string(sortby="Pokemon Type")
print(table)
