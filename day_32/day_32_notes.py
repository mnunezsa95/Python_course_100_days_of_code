# ------------------------------------------------------------------------------------------------ #
#                                       Email SMTP & datetime                                      #
# ------------------------------------------------------------------------------------------------ #

# ----------------------------------- Sending Emails using SMTP ---------------------------------- #

import smtplib
import dotenv

credentials = dotenv.dotenv_values()
MY_EMAIL = credentials["SMTP_USERNAME"]
PASSWORD = credentials["SMTP_PASSWORD"]
SEND_ADDRESS = credentials["SMTP_SEND_ADDRESS"]

with smtplib.SMTP("smtp.gmail.com") as connection:  # creating a connection to gmail
    connection.starttls()  # securing connection to email server
    connection.login(user=MY_EMAIL, password=PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=SEND_ADDRESS,
        msg="Subject:Hello, Marlon!\n\nThis is the body of my email",
    )


# --------------------------------- Working with datetime module --------------------------------- #
### Getting the current date
import datetime as dt

now = dt.datetime.now()  # Retrieves current date/time
print(now)

year = now.year  # accessing the year attribute
month = now.month  # accessing the month attribute
print(year)
print(month)

if year == 2020:
    print("Wear a facemask")

day_of_week = now.weekday()  # Returns the day of week (as a number)
print(day_of_week)  # computers count from 0 (Monday), so 3 is Thursday


### Creating a specific datetime
date_of_birth = dt.datetime(year=1995, month=10, day=31)
print(date_of_birth)

# ----------------------- Challenge 1 - Send Motivational Quotes on Mondays ---------------------- #
import random

current_date = dt.datetime.now()
weekday = current_date.weekday()


if weekday == 0:
    with open("day_32/quotes.txt") as quote_file:  # opening the txt file
        all_quotes = quote_file.readlines()  # create a list with items of txt file
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="marlonnunez.dev@gmail.com",
            msg=f"Subject:Monday Motivation\n\n{quote}",
        )
