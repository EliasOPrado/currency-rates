import time
from datetime import datetime, timedelta
import requests
from br_med_app.models import CurrencyRate
from decimal import Decimal


def insert_data_into_db(api_data, target_currency):
    # Check if api_data is a list and has at least one dictionary
    if isinstance(api_data, list) and api_data:
        # Get the first dictionary from the list
        api_data_dict = api_data[0]

        # Extract values from api_data_dict
        date = api_data_dict.get("date")
        base_currency = api_data_dict.get("base")
        rates = api_data_dict.get("rates", {})

        # Check if data for the target_currency exists in rates
        if isinstance(rates, dict) and target_currency in rates:
            exchange_rate = Decimal(rates[target_currency])

            # Create or update the CurrencyRate object
            currency_rate, created = CurrencyRate.objects.update_or_create(
                date=date,
                base_currency=base_currency,
                target_currency=target_currency,
                defaults={"exchange_rate": exchange_rate},
            )

            return currency_rate
        else:
            # Handle the case when the target_currency is not present in rates or rates is not a dictionary
            return None
    else:
        # Handle the case when api_data is not a list or is an empty list
        return None


def get_api_data(single_date, target_currency):
    base_url = "https://api.vatcomply.com/rates"

    # Make API request for the specified date with cache-control headers
    params = {"date": single_date, "base": "USD"}
    headers = {"Cache-Control": "no-cache", "Pragma": "no-cache"}

    response = requests.get(base_url, params=params, headers=headers)
    api_data = response.json()

    # Check if the target_currency data is present in the response
    if target_currency in api_data.get("rates", {}):
        return [api_data]  # Return a list with a single API response

    return []
