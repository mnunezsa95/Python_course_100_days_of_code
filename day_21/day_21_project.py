# ------------------------------------------------------------------------------------------------ #
#                                            Snake Game                                            #
# ------------------------------------------------------------------------------------------------ #

"""
Steps to create the snake game
1) Create a snake body
2) Move the snake
3) Create snake food
4) Detect collision with food
5) Create a scoreboard
6) Detect collision with wall
7) Detect collision with tail
"""

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Setting up screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game!")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Snake move automatically
game_is_one = True
while game_is_one:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect collision with food
    if snake.head.distance(food) < 15:
        print("food acquired; score increase")
        food.refresh()
        snake.extend_tail()
        print("tail extended by 1")
        scoreboard.increase_score()

    # Detect collision with wall.
    if (
        snake.head.xcor() > 280
        or snake.head.xcor() < -280
        or snake.head.ycor() > 280
        or snake.head.ycor() < -280
    ):
        scoreboard.reset_scoreboard()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            snake.reset()

screen.exitonclick()
