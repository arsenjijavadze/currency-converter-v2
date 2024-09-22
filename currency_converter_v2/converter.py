def convert(original_currency, result_currency, amount, exchange_rates):
    original_currency_value = exchange_rates[original_currency]
    result_currency_value = exchange_rates[result_currency]
    coefficient = result_currency_value / original_currency_value

    return amount * coefficient
