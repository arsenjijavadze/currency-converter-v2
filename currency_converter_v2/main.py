from converter import convert
from api import get_actual_currencies, get_exchange_rates

currencies_data = get_actual_currencies()

if currencies_data:
    currencies = currencies_data
    print("Available currencies:")
    for code, info in currencies.items():
        print(f"- {code}: {info['name']} ({info['symbol']})")
else:
    print("Failed to retrieve currencies")
    exit()


exchange_rates = get_exchange_rates()


print("Welcome to the Currency Converter")
print("""
Instructions:
1. Enter the source currency (e.g., USD)
2. Enter the target currency (e.g., EUR)
3. Enter the amount of source currency (e.g., 100)

Available currencies:
""")

original_currency = input("1. Enter the source currency: ").upper()
if original_currency not in currencies:
    print("Invalid source currency")
    exit()

result_currency = input("2. Enter the target currency: ").upper()
if result_currency not in currencies:
    print("Invalid targer currency")
    exit()

try:
    original_amount = float(input("3. Enter the amount of source currency: "))
except ValueError:
    print("Invalid amount")
    exit()

# TODO: Handle errors (nonexistent currency + non-numeric amount)
# TODO: Handle not only integers
# NOTE: Consider handling negative numbers

result_amount = convert(
    original_currency, result_currency, original_amount, exchange_rates
)

print(f"{original_amount} {original_currency} = {result_amount} {result_currency}")
