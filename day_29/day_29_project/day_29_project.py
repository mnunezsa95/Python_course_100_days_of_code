# ---------------------------------- My Password Manager Project --------------------------------- #

from tkinter import *

# -------------------------------------- PASSWORD GENERATOR -------------------------------------- #


# ----------------------------------------- SAVE PASSWORD ---------------------------------------- #
def save():
    open("password.txt", "a")


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
email_username_label = Label(text="Email/Username:")
email_username_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)
email_username_entry = Entry(width=35)
email_username_entry.insert(0, "mnunezsa95@gmail.com")
email_username_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=20)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_btn = Button(text="Generate PW", width=10)
generate_password_btn.grid(row=3, column=2)
add_button = Button(text="Add", width=33, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
