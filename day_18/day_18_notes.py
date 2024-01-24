# ------------------------------------------------------------------------------------------------ #
#                       Using Documentation & Graphical User Interfaces (GUI)                      #
# ------------------------------------------------------------------------------------------------ #


#### The Turtle Library

# Turtle Graphics Documentation: https://docs.python.org/3/library/turtle.html
from turtle import Turtle, Screen

timmy = Turtle()  # create new turlte object
timmy.shape("turtle")  # add shape to turtle
timmy.color("red")  # change color

# * Challenge 1: draw a square
# for _ in range(4):
#     timmy.forward(100)
#     timmy.left(90)


# * Challenge 2: Draw dashed lines
for _ in range(15):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()

# * Challenge 3:

screen = Screen()
screen.exitonclick()
