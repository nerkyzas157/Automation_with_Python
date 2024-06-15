import requests  # type: ignore
import smtplib
from datetime import date, timedelta

STOCK = "NVDA"
COMPANY_NAME = "NVIDIA"
AV_API_KEY = "alphavantage API key"
NEWS_API_KEY = "newsapi API key"

# SMTP credentials:
MY_EMAIL = "email@gmail.com"
APP_PASS = "xxxx xxxx xxxx xxxx"

# Set a dynamic variable for yesterday's date
yesterday = str(date.today() - timedelta(days=1))

# Calling Alphavantage to extract the data
stocks_response = requests.get(
    url=f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={AV_API_KEY}"
)
stocks_response.raise_for_status()
stock_data = stocks_response.json()

# Investigating data for any major changes
open = float(stock_data["Time Series (Daily)"][yesterday]["1. open"])
close = float(stock_data["Time Series (Daily)"][yesterday]["4. close"])
result = round((close - open) / open * 100, 2)
if abs(result) > 5:
    # Gathering related news articles
    news_response = requests.get(
        url=f"https://newsapi.org/v2/everything?language=en&q={COMPANY_NAME}+stock&qInTitle={COMPANY_NAME}&from={yesterday}&sortBy=relevancy&apiKey={NEWS_API_KEY}"
    )
    news_response.raise_for_status()
    news_data = news_response.json()
    headline = f"\"{news_data["articles"][0]["source"]["name"]}\" says: {news_data["articles"][0]["title"]}."
    description = f"Description: {news_data["articles"][0]["description"]}"
    if result > 0:
        emoji = "🔺"
    else:
        emoji = "🔻"
    label = f"{STOCK}: {emoji}{abs(result)}%"
    # Sending an email
    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=MY_EMAIL, password=APP_PASS)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs="email@gmail.com",
        msg=f"{label}\n\n{headline}\n{description}.",
    )
