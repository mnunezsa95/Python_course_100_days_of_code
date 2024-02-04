# ------------------------------------------------------------------------------------------------ #
#                                     Tkinter, *args, **kwargs                                     #
# ------------------------------------------------------------------------------------------------ #

# -------------------------------------------- Tkinter ------------------------------------------- #
# Tkinter
# - Tkinter can be used to make Graphical User Interface (GUI)
# - Tkinter is already installed in Python

import tkinter

### Creating a window
window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

### Creating a label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold", "italic"))
my_label.pack(side="left")


window.mainloop()


# ------------------------------ Advanced Arguments (Default Values) ----------------------------- #
### Arguments with Default Values
# - Default parameter values can be declared in the function
# - This allows the function to ALWAYS have a default value incase one isn't provided
# -- This can be changed when calling the function


# -------------------------------------- Unlimited Arguments ------------------------------------- #
#### Unlimited Arguments (`*args`)
# - *args is passed into the function's parameter to allow for unlimited arguments


def add(*args):  # the asterik (*) tells python to accept any number of args
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(1, 2, 3, 4))
