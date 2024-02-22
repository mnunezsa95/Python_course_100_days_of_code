# ------------------------------------------------------------------------------------------------ #
#                            API Post, Put and Delete Requests & Headers                           #
# ------------------------------------------------------------------------------------------------ #

# ------------------------------ HTTP Post, Put and Delete Requests ------------------------------ #
# Post requests are made using requests.post()
# Put requests are made using requests.put()
# Delete requests are made using request.delete()

# ---------------------------------------- Request Headers --------------------------------------- #
# Request headers are sent by the client to the server & contain information and instructions related to the requested resource


# ------------------------------------- Using a Post Request ------------------------------------- #
# Pixela Documentation: https://docs.pixe.la/
# Requests Library Documentation: https://requests.readthedocs.io/en/latest/api/

import requests
from dotenv import dotenv_values
import datetime as dt

config = dotenv_values(".env")  # import .env files

# Endpoint for Creating Account
PIXELA_SIGNUP_ENDPOINT = "https://pixe.la/v1/users"

# Define token & username
PIXELA_TOKEN = config["PIXELA_TOKEN"]
PIXELA_USERNAME = config["PIXELA_USERNAME"]

# Endpoint for creating graph
PIXELA_GRAPH_ENDPOINT = f"https://pixe.la/v1/users/{PIXELA_USERNAME}/graphs"
GRAPHID = "graph1"

# Endpoint for adding pixel
PIXELA_CREATION_ENDPOINT = (
    f"https://pixe.la/v1/users/{PIXELA_USERNAME}/graphs/{GRAPHID}"
)

today = dt.datetime.now()  # today's date
yesterday = dt.datetime(year=2024, month=2, day=21)

PIXEL_HEADERS = {"X-USER-TOKEN": PIXELA_TOKEN}


# User URL --> "https://pixe.la/@marlonnunezdev"
# Graph1 URL --> "https://pixe.la/v1/users/marlonnunezdev/graphs/graph1.html"

# Setting up Pixela Account
"""
user_parameters = {
    "token": PIXELA_TOKEN,
    "username": PIXELA_USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
pixela_response = requests.post(url=PIXELA_SIGNUP_ENDPOINT, json=user_parameters)
"""


# Creating a Graph
"""
# The request headers
graph_headers = {"X-USER-TOKEN": PIXELA_TOKEN}

# Creating a graph definition
graph_parameters = {
    "id": GraphID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

graph_response = requests.post(
    url=PIXELA_GRAPH_ENDPOINT, json=graph_parameters, headers=graph_headers
)
print(graph_response)
"""

# Posting a pixel on the graph
"""
today_date_formatted = today.strftime("%Y%m%d")

pixel_parameters = {
    "date": today_date_formatted,
    "quantity": "5",
}
pixel_response = requests.post(
    url=PIXELA_CREATION_ENDPOINT, json=pixel_parameters, headers=PIXEL_HEADERS
)
print(pixel_response)
"""

# ------------------------------------ Using the put() Method ------------------------------------ #

# Updating a Pixel on a Graph
"""
yesterday_date_formatted = yesterday.strftime("%Y%m%d")

update_pixel_parameters = {"quantity": "15"}
update_pixel_response = requests.put(
    url=f"{PIXELA_CREATION_ENDPOINT}/{yesterday_date_formatted}",
    json=update_pixel_parameters,
    headers=PIXEL_HEADERS,
)
print(update_pixel_response)
"""

# ----------------------------------- Using the delete() Method ---------------------------------- #

# Deleting a Pixel on a Graph
"""
today_date_formatted = today.strftime("%Y%m%d")
delete_pixel_response = requests.delete(
    url=f"{PIXELA_CREATION_ENDPOINT}/{today_date_formatted}",
    headers=PIXEL_HEADERS,
)
print(delete_pixel_response)
"""
