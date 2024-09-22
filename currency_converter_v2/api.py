import requests
import os
import freecurrencyapi
from dotenv import load_dotenv

load_dotenv()


API_KEY = os.getenv("CURRENCY_API_KEY")
client = freecurrencyapi.Client(API_KEY)


def get_actual_currencies():
    result = client.currencies(currencies=["EUR", "USD", "CNY"])
    return result["data"]


def get_exchange_rates():
    url = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"
    response = requests.get(url)
    return response.json()["data"]
