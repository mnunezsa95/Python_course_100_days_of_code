# ------------------------------------------------------------------------------------------------ #
#                       Using Documentation & Graphical User Interfaces (GUI)                      #
# ------------------------------------------------------------------------------------------------ #


#### The Turtle Library

# Turtle Graphics Documentation: https://docs.python.org/3/library/turtle.html
from turtle import Turtle, Screen
import turtle as t

timmy = Turtle()  # create new turlte object
timmy.shape("turtle")  # add shape to turtle
timmy.color("red")  # change color

# * Challenge 1: draw a square
# for _ in range(4):
#     timmy.forward(100)
#     timmy.left(90)


# * Challenge 2: Draw dashed lines
# for _ in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()


# * Challenge 3: Drawing different figures
# import random

# colors = [
#     "CornflowerBlue",
#     "DarkOrchid",
#     "IndianRed",
#     "DeepSkyBlue",
#     "LightSeaGreen",
#     "wheat",
#     "SlateGray",
#     "SeaGreen",
# ]


# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         timmy.color(random.choice(colors))
#         timmy.forward(100)
#         timmy.right(angle)


# for shape_side_n in range(3, 11):
#     draw_shape(shape_side_n)


# * Challenge 4: Draw a random walk
# * Challenge 5: Creating a random RGB color
# import random

# t.colormode(255)
# directions = [0, 90, 180, 270]


# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = r = random.randint(0, 255)
#     return (r, g, b)


# for _ in range(200):
#     timmy.pensize(10)
#     timmy.speed(8)
#     timmy.color(random_color())
#     timmy.forward(30)
#     timmy.setheading(random.choice(directions))


# * Challenge 6: Draw a Spirograph
import random

t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = r = random.randint(0, 255)
    return (r, g, b)


timmy.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)


draw_spirograph(5)

# Show screen
screen = Screen()
screen.exitonclick()
