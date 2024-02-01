# ------------------------------------------------------------------------------------------------ #
#                                          U.S States Game                                         #
# ------------------------------------------------------------------------------------------------ #
import turtle
import pandas
import os


image = "day_25/day_25_project/blank_states_img.gif"
df_states = pandas.read_csv("day_25/day_25_project/50_states.csv")


def cls():
    os.system("cls" if os.name == "nt" else "clear")


cls()
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(image)
turtle.shape(image)

guessed_states = []

while len(guessed_states) < 51:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="What's antoher state's name?",
    ).title()

    all_states = df_states.state.to_list()  # creating a list of states

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        state_data = df_states[df_states.state == answer_state]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        t.write(state_data.state.item())
