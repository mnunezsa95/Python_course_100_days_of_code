import requests as req
import lxml
import smtplib
from bs4 import BeautifulSoup
from pprint import pprint
import dotenv

credentials = dotenv.dotenv_values()
USERNAME = credentials["SMTP_USERNAME"]
PASSWORD = credentials["SMTP_PASSWORD"]
SEND_ADDRESS = credentials["SMTP_SEND_ADDRESS"]
URL = input("Enter the url of the item: ")
# "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

response = req.get(
    url=URL,
    headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
    },
)

soup = BeautifulSoup(response.text, "lxml")
price = float(soup.find(class_="aok-offscreen").getText().lstrip().split(" ")[0][1:])
item_name = soup.find(class_="a-size-large product-title-word-break").getText().strip()
target_price = int(input("What is your target price: "))

if price < target_price:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=USERNAME, password=PASSWORD)
        connection.sendmail(
            from_addr=USERNAME,
            to_addrs=SEND_ADDRESS,
            msg=f"Subject:Amazon Price Alert!\n\n{item_name} is now ${price}!\n{URL}".encode(
                "utf-8"
            ),
        )
