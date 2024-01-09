# ------------------------------------------------------------------------------------------------ #
#                                          Reeborg's World                                         #
# ------------------------------------------------------------------------------------------------ #
# Reeborg's World Maze Challenge: http://tinyurl.com/s42m2w6j

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()