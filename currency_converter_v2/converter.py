from typing import Dict


def convert(
    original_currency: str,
    result_currency: str,
    amount: float,
    exchange_rates: Dict[str, float],
) -> float:
    original_currency_value = exchange_rates[original_currency]
    result_currency_value = exchange_rates[result_currency]
    coefficient = result_currency_value / original_currency_value

    return amount * coefficient
