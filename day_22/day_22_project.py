# ------------------------------------------------------------------------------------------------ #
#                                Build Pong: The Famous Arcade Game                                #
# ------------------------------------------------------------------------------------------------ #

"""
Steps
1) Create the screen
2) Create and mnove a paddle
3) Create another paddle
4) Create the ball and make it move
5) Detect collision with the wall and bounce
6) Detect collision with paddle
7) Detect when paddle misses
8) Keep score
"""

from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.title("World Famous Pong Game")
screen.tracer(0)
screen.setup(width=800, height=600)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()

screen.listen()

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

screen.exitonclick()
