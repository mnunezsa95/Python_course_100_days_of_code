# ------------------------------------------------------------------------------------------------ #
#                     API Keys, API Authentication and Environmental Variables                     #
# ------------------------------------------------------------------------------------------------ #

# ----------------------------------- API Keys & Authentication ---------------------------------- #
# API Keys are used to authorize or deny access and track usage
import requests
from twilio.rest import Client
from dotenv import dotenv_values

config = dotenv_values(".env")

BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"
OWM_API_KEY = config["OWM_API_KEY"]
MY_LAT = 42.3671218
MY_LNG = -71.0407708
TWILIO_ACCOUNT_SID = config["TWILIO_ACCOUNT_SID"]
TWILIO_AUTH_TOKEN = config["TWILIO_AUTH_TOKEN"]
VIRTUAL_TWILIO_NUMBER = config["VIRTUAL_TWILIO_NUMBER"]
VERIFIED_NUMBER = config["VERIFIED_NUMBER"]

weather_params = {"lat": MY_LAT, "lon": MY_LNG, "appid": OWM_API_KEY, "cnt": 4}

forcast_response = requests.get(url=BASE_URL, params=weather_params)
forcast_response.raise_for_status()
weather_data = forcast_response.json()


will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 600:
        will_rain = True

if will_rain:
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body="It will rain! Bring an umbrella ☂️",
        from_=VIRTUAL_TWILIO_NUMBER,
        to=VERIFIED_NUMBER,
    )
    print(message.status)
