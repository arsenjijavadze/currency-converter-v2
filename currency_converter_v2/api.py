import requests
import os
import freecurrencyapi
from dotenv import load_dotenv
from typing import Dict, Any

load_dotenv()


API_KEY = os.getenv("CURRENCY_API_KEY", "")
client = freecurrencyapi.Client(API_KEY)


def get_actual_currencies() -> Dict[str, Dict[str, Any]]:
    result: Dict[str, Any] = client.currencies(currencies=["EUR", "USD", "CNY"])
    return result["data"]


def get_exchange_rates() -> Dict[str, float]:
    url: str = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"
    response = requests.get(url)
    return response.json()["data"]
