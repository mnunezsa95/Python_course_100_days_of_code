# ------------------------------------------------------------------------------------------------ #
#                                     Tkinter, *args, **kwargs                                     #
# ------------------------------------------------------------------------------------------------ #

# -------------------------------------------- Tkinter ------------------------------------------- #
# Tkinter
# - Tkinter can be used to make Graphical User Interface (GUI)
# - Tkinter is already installed in Python

import tkinter


def button_clicked():  # callback function
    print("I got clicked")
    new_text = input.get()
    my_label["text"] = new_text  # accessing & changing the text property


### Creating a window
window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)  # Adding padding to the edges of program

###* Creating a label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold", "italic"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)  # Adding padding to a specific widget

###* Creating a button
# command tells button to listen for the callback function
button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = tkinter.Button(text="New Button")
new_button.grid(column=2, row=0)

###* Creating an Entry
input = tkinter.Entry(width=10)
input.get()  # Returns the input as a string
input.grid(column=3, row=2)


window.mainloop()


# ------------------------------ Advanced Arguments (Default Values) ----------------------------- #
### Arguments with Default Values
# - Default parameter values can be declared in the function
# - This allows the function to ALWAYS have a default value incase one isn't provided
# -- This can be changed when calling the function


# -------------------------------- Unlimited Positional Arguments -------------------------------- #
#### Unlimited Positional Arguments (*args)
# - *args is passed into the function's parameter to allow for unlimited positional arguments
# - *args is of type 'tuple'
# - *args can be accessed using bracket notation (since `*args*` is a tuple)


def add(*args):  # the asterik (*) tells python to accept any number of args
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(1, 2, 3, 4))


# ---------------------------------- Unlimited Keyword Arguments --------------------------------- #
#### Unlimited Keyword Arguments (**kwargs)
# - **kwargs is passed into the function's parameter to allow for unlimited keyword arguments
# - **kwargs is of type 'dict'
# - **kwargs can be accessed using bracket notation (since *args is a dict)


def calculate(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)
    print(kwargs["add"])


calculate(add=3, multiply=5)


### Creating classes with **kwargs
class Car:
    def __init(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.color = kwargs.get("seats")


my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)


### Quiz Question: Default Args, *args, **kwargs
def all_aboard(a, *args, **kw):
    print(a, args, kw)


all_aboard(4, 7, 3, 0, x=10, y=64)  # 4, (7, 3, 0) {"x": 10, "y": 64}
