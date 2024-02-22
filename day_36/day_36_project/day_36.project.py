import requests
from dotenv import dotenv_values
from twilio.rest import Client

config = dotenv_values(".env")

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query?"
STOCK_API_KEY = config["STOCK_API_KEY"]
STOCK_FUNCTION = "TIME_SERIES_DAILY"

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = config["NEWS_API_KEY"]

VIRTUAL_TWILIO_NUMBER = config["VIRTUAL_TWILIO_NUMBER"]
VERIFIED_NUMBER = config["VERIFIED_NUMBER"]
TWILIO_ACCOUNT_SID = config["TWILIO_ACCOUNT_SID"]
TWILIO_AUTH_TOKEN = config["TWILIO_AUTH_TOKEN"]

stock_parameters = {
    "function": STOCK_FUNCTION,
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

news_parameters = {
    "apiKey": NEWS_API_KEY,
    "q": COMPANY_NAME,
    "searchIn": "title",
    "language": "en",
}

stock_response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
stock_data = stock_response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in stock_data.items()]

yesterday_closing_price = data_list[0]["4. close"]
day_before_yesterday_closing_price = data_list[1]["4. close"]

price_difference = float(yesterday_closing_price) - float(
    day_before_yesterday_closing_price
)

up_down = None
if price_difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

diff_percent = round((price_difference / float(yesterday_closing_price)) * 100)

if abs(diff_percent) > 1:
    news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    news_articles = news_response.json()["articles"]
    three_articles = news_articles[:3]

    formatted_articles = [
        f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}"
        for article in three_articles
    ]
    print(formatted_articles)

    twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    for article in formatted_articles:
        message = twilio_client.messages.create(
            body=article, from_=VIRTUAL_TWILIO_NUMBER, to=VERIFIED_NUMBER
        )
