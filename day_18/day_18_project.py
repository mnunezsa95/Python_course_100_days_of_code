# ------------------------------------------------------------------------------------------------ #
#                                     The Hirst Paining Project                                    #
# ------------------------------------------------------------------------------------------------ #
import colorgram  # Documentation: https://pypi.org/project/colorgram.py/
import turtle as t  # Documentation: https://docs.python.org/3/library/turtle.html
import random

# ! Comment out so it color extraction does not run every time
# rgb_colors = []
# colors = colorgram.extract("day_18/image.jpg", 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))

color_list = [
    (202, 164, 110),
    (236, 239, 243),
    (149, 75, 50),
    (222, 201, 136),
    (53, 93, 123),
    (170, 154, 41),
    (138, 31, 20),
    (134, 163, 184),
    (197, 92, 73),
    (47, 121, 86),
    (73, 43, 35),
    (145, 178, 149),
    (14, 98, 70),
    (232, 176, 165),
    (160, 142, 158),
    (54, 45, 50),
    (101, 75, 77),
    (183, 205, 171),
    (36, 60, 74),
    (19, 86, 89),
    (82, 148, 129),
    (147, 17, 19),
    (27, 68, 102),
    (12, 70, 64),
    (107, 127, 153),
    (176, 192, 208),
    (168, 99, 102),
]

circle = t.Turtle()  # create instance of Turtle() class
t.colormode(255)  # change color mode to rgb

circle.speed("fastest")  # increase speed
circle.hideturtle()  # hide pointer
circle.penup()  # remove pen lines
circle.setheading(225)  # set initial heading
circle.forward(330)  # move forward
circle.setheading(0)  # reset the heading (turn right)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    circle.dot(20, random.choice(color_list))
    circle.forward(50)
    if dot_count % 10 == 0:  # if dot_count ends in a mutliple of 10 (10, 20, 30)
        # this code re-orients on next row
        circle.setheading(90)
        circle.forward(50)
        circle.setheading(180)
        circle.forward(500)
        circle.setheading(0)

screen = t.Screen()
screen.exitonclick()
