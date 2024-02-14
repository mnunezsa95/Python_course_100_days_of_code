# ------------------------------------------------------------------------------------------------ #
#                                      Flash Card App Project                                      #
# ------------------------------------------------------------------------------------------------ #
from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("day_31/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("day_31/data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(5000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


def is_knwon():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("day_31/data/words_to_learn.csv", index=False)
    next_card()


# Window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# Canvas
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="day_31/images/card_front.png")
card_back_img = PhotoImage(file="day_31/images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(
    400, 150, text="", font=("Ariel", 40, "italic"), fill="black"
)
card_word = canvas.create_text(
    400, 263, text="", font=("Ariel", 60, "bold"), fill="black"
)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
cross_image = PhotoImage(file="day_31/images/wrong.png")
unknown_button = Button(
    image=cross_image,
    highlightthickness=0,
    highlightbackground=BACKGROUND_COLOR,
    height=95,
    width=95,
    command=next_card,
).grid(row=1, column=0)

check_image = PhotoImage(file="day_31/images/right.png")
known_button = Button(
    image=check_image,
    highlightthickness=0,
    highlightbackground=BACKGROUND_COLOR,
    height=95,
    width=95,
    command=is_knwon,
).grid(row=1, column=1)


next_card()

# Mainloop
window.mainloop()
