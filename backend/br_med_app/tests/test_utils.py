from django.test import TestCase
from django.utils import timezone
from datetime import date
from decimal import Decimal
from unittest.mock import patch
from br_med_app.models import CurrencyRate
from br_med_app.api.utils import insert_data_into_db, get_api_data


class CurrencyRateTest(TestCase):
    @patch("requests.get")
    def test_get_api_data(self, mock_requests_get):
        mock_response = {"rates": {"BRL": 5.4}, "base": "USD", "date": "2023-01-15"}
        mock_requests_get.return_value.json.return_value = mock_response

        api_data = get_api_data("2023-01-15", "BRL")
        self.assertEqual(api_data, [mock_response])

    def test_insert_data_into_db(self):
        api_data = [{"date": "2023-01-15", "base": "USD", "rates": {"BRL": 5.4}}]

        currency_rate = insert_data_into_db(api_data, "BRL")

        retrieved_currency_rate = CurrencyRate.objects.get(
            date="2023-01-15", target_currency="BRL"
        )

        self.assertEqual(currency_rate, retrieved_currency_rate)
        self.assertEqual(retrieved_currency_rate.date, date(2023, 1, 15))
        self.assertEqual(retrieved_currency_rate.base_currency, "USD")
        self.assertEqual(retrieved_currency_rate.target_currency, "BRL")
        self.assertEqual(retrieved_currency_rate.exchange_rate, Decimal("5.4"))
