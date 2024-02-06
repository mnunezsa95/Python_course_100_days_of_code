# ---------------------------------- My Password Manager Project --------------------------------- #
import pyperclip
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle

# -------------------------------------- PASSWORD GENERATOR -------------------------------------- #
# Password Generator Project


def generate_password():
    password_entry.delete(0, END)
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbol = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbol + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    print(f"Your password is: {password}")
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ----------------------------------------- SAVE PASSWORD ---------------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        is_empty = messagebox.showinfo(
            title="Oops", message="Please don't leave any fields empty"
        )
    else:
        is_ok = messagebox.askokcancel(
            title=website,
            message=f"These are the details entered:\n \nWebsite: {website}\nEmail: {email}\nPassword: {password}\n \nIs it ok to save?",
        )
        if is_ok:
            with open("sensitive_info/password_28.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ------------------------------------------- UI SETUP ------------------------------------------- #

# Window
window = Tk()
window.title("Password Manager")
window.config(padx=25, pady=50)

# Canvas
canvas = Canvas(width=200, height=200)
password_img = PhotoImage(file="day_29/day_29_project/password.png")
canvas.create_image(100, 100, image=password_img)
canvas.grid(row=0, column=1)

# Label
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)
email_entry = Entry(width=35)
email_entry.insert(0, "mnunezsa95@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=20)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_btn = Button(text="Generate PW", width=10, command=generate_password)
generate_password_btn.grid(row=3, column=2)
add_button = Button(text="Add", width=33, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
