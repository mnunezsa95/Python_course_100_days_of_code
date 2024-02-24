# ------------------------------------------------------------------------------------------------ #
#                                     Workout Tracking Project                                     #
# ------------------------------------------------------------------------------------------------ #

import requests
import datetime as dt
from dotenv import dotenv_values

config = dotenv_values()
NUTRITIONIX_APP_ID = config["NUTRITIONIX_APP_ID"]
NUTRITIONIX_API_KEY = config["NUTRITIONIX_API_KEY"]
SHEET_BEARER_TOKEN = config["SHEET_BEARER_TOKEN"]

# CONSTANTS
WEIGHT_LB = 228
HEIGHT_IN = 72
AGE = 28
# CALCULATED CONSTANTS
WEIGHT_KG = WEIGHT_LB * 2.20462
HEIGHT_CM = HEIGHT_IN * 2.54

# WORKOUT
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = (
    "https://api.sheety.co/9099fccd4adfdf33347a434694cc30e9/myWorkouts/workouts"
)
exercise_text = input("Tell me which exercises you did: ")

exercise_parameters = {
    "query": exercise_text,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}
exercise_headers = {"x-app-id": NUTRITIONIX_APP_ID, "x-app-key": NUTRITIONIX_API_KEY}

exercise_response = requests.post(
    url=exercise_endpoint, json=exercise_parameters, headers=exercise_headers
)
exercise_data = exercise_response.json()
print(exercise_data)

# SHEETY
today_date = dt.datetime.now().strftime("%m/%d/%Y")
today_time = dt.datetime.now().strftime("%X")


for exercise in exercise_data["exercises"]:
    sheet_headers = {f"Authorization": SHEET_BEARER_TOKEN}
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": today_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    sheet_response = requests.post(
        sheet_endpoint, json=sheet_inputs, headers=sheet_headers
    )

    print(sheet_response.text)
