# ------------------------------------------------------------------------------------------------ #
#                                          Pomodoro Timer                                          #
# ------------------------------------------------------------------------------------------------ #

from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ------------------------------------------ TIMER RESET ----------------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0


# ---------------------------------------- TIMER MECHANISM --------------------------------------- #
def start_timer():  # calls the count_down() fn
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title.config(text="Short Break", fg=PINK)
    else:
        count_down(work_sec)
        title.config(text="Work", fg=GREEN)


# -------------------------------------- COUNTDOWN MECHANISM ------------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(
            1000, count_down, count - 1
        )  # executes a fn after a time delay
    else:
        count_down(work_sec)
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(0, work_sessions):
            marks += "✔"
        check_marks.config(text=marks)


# ------------------------------------------- UI SETUP ------------------------------------------- #
window = Tk()  # create instance of Tk() class (as window)
window.title("Pomodoro Timer")  # Change title of window
window.config(padx=100, pady=50, background=YELLOW)  # add padding to window

title = Label(text="Timer", font=(FONT_NAME, 50, "bold"), bg=YELLOW, fg=GREEN)
title.grid(row=1, column=2)

canvas = Canvas(
    width=200, height=234, bg=YELLOW, highlightthickness=0
)  # creating a canvas
tomato_img = PhotoImage(file="day_28/day_28_project/tomato.png")  # creating an img
canvas.create_image(100, 112, image=tomato_img)  # add an image to the canvas
timer_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(row=2, column=2)  # adding the canvas to the window


start_button = Button(
    text="Start", command=start_timer, highlightthickness=0, highlightbackground=YELLOW
)
start_button.grid(row=3, column=1)

reset_button = Button(
    text="Reset", command=reset_timer, highlightthickness=0, highlightbackground=YELLOW
)

reset_button.grid(row=3, column=3)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(row=4, column=2)

# ----------------------------------------- WINDOW POPUP ----------------------------------------- #
window.mainloop()  # Get window to show up
