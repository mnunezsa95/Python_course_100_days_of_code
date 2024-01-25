# ------------------------------------------------------------------------------------------------ #
#                            Instances, State and Higher Order Functions                           #
# ------------------------------------------------------------------------------------------------ #

### Event Listeners & Higher Order Functions (HOFs)
# - Event listeners are functions that 'listen' for an event to happen in order to trigger a callback function
# - HOFs are functions that work with other functions (take functions as inputs or return functions)

from turtle import Screen, Turtle


### Example 1: Using HOFs
def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def turn_left():
    tim.left(10)


def turn_right():
    tim.right(10)


def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear_drawing, "c")
screen.exitonclick()


### Object State and Instances
# - Objects created from the same class are considered to be different instances
# -- Instances have state independent of the class
tommy = Turtle()
johnny = Turtle()
