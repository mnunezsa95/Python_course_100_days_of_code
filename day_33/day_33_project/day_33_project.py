# ------------------------------------------------------------------------------------------------ #
#                                   ISS Overhead Notifier Project                                  #
# ------------------------------------------------------------------------------------------------ #

import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 42.360081
MY_LONG = -71.058884
MY_EMAIL = "mnunezsadev@gmail.com"
MY_PASSWORD = "ppgclzvacfissewq"


# ISS Position
def is_iss_overhead():
    iss_res = requests.get("http://api.open-notify.org/iss-now.json")
    iss_res.raise_for_status()
    data = iss_res.json()
    iss_lat = float(data["iss_position"]["latitude"])
    iss_lng = float(data["iss_position"]["longitude"])

    if MY_LAT - 5 <= iss_lat <= MY_LAT + 5 and MY_LONG - 5 <= iss_lng <= MY_LONG + 5:
        return True


# Sunrise & sunset time in local area
def is_night():
    parameters = {"lat": MY_LAT, "lng": MY_LONG, "formatted": 0}
    res = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    res.raise_for_status()
    rise_set_data = res.json()

    s_rise_time = int(rise_set_data["results"]["sunrise"].split("T")[1].split(":")[0])
    s_set_time = int(rise_set_data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour  # Time now

    if time_now >= s_set_time and time_now <= s_rise_time:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="marlonnunez.dev@gmail.com"
                "Subject: ISS is Overhead\n\n The ISS is above you overhead",
            )
