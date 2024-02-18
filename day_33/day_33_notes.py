# ------------------------------------------------------------------------------------------------ #
#                                  API Endpoints & API Parameters                                  #
# ------------------------------------------------------------------------------------------------ #

# ---------------------- What are Application Programming Interfaces (APIs)? --------------------- #
"""
An API is a set of commands, functions, protocols, and objects that programmers can use to create 
software or interact with an external system

An API serves as a barrier between our program and an external system

Our program sends requests & the external system sends back a response
"""

# ----------------------------------------- API Endpoints ---------------------------------------- #
"""
An API endpoint is the address for the API
An API Request is a request made to the API endpoint 
If successful the request is approved, and data is sent to the user

A majority of data is transferred in JSON (JavaScript Object Notation) format
"""

# --------------------------------------- Working with APIs -------------------------------------- #
import requests

# Fetching data from ISS API
res = requests.get(url="http://api.open-notify.org/iss-now.json")
print(res.status_code)

# Checking status code & raising exceptions for different codes
if res.status_code == 404:
    raise Exception("That resource does not exist.")
elif res.status_code == 401:
    raise Exception("You are not authorized to access this data.")

# Using the requests library to raise exceptions if request is unsuccessful
res.raise_for_status()

# Getting data from response
data = res.json()
print(data)

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
iss_position = (longitude, latitude)
print(iss_position)

# --------------------------------- Kanye Random Quote Generator --------------------------------- #
# from tkinter import *
# import requests


# def get_quote():
#     response = requests.get(url="https://api.kanye.rest")
#     response.raise_for_status()
#     ye_data = response.json()
#     ye_quote = ye_data["quote"]
#     canvas.itemconfig(quote_text, text=ye_quote)


# window = Tk()
# window.title("Kanye Says...")
# window.config(padx=50, pady=50)

# canvas = Canvas(width=300, height=414)
# background_img = PhotoImage(file="day_33/background.png")
# canvas.create_image(150, 207, image=background_img)
# quote_text = canvas.create_text(
#     150,
#     207,
#     text="Kanye Quote Goes HERE",
#     width=250,
#     font=("Arial", 30, "bold"),
#     fill="white",
# )
# canvas.grid(row=0, column=0)

# kanye_img = PhotoImage(file="day_33/kanye.png")
# kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
# kanye_button.grid(row=1, column=0)
# window.mainloop()

# ---------------------------------------- API Parameters ---------------------------------------- #
"""
API Parameters --> allows us to give an input when making a request to get different types of data
"""

from datetime import datetime

MY_LAT = 42.360081
MY_LONG = -71.058884

# Using parameters in API call to get specific data
parameters = {"lat": MY_LAT, "lng": MY_LONG, "formatted": 0}
sunrise_sunset_response = requests.get(
    url="https://api.sunrise-sunset.org/json", params=parameters
)
sunrise_sunset_response.raise_for_status()
sunrise_sunset_data = sunrise_sunset_response.json()
