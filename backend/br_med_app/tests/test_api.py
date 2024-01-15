from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from br_med_app.models import CurrencyRate
from br_med_app.api.serializers import CurrencyRateSerializer


class CurrencyRatesAPITest(APITestCase):
    def setUp(self):
        self.url = "/api/currency-rates/"
        self.list_url = reverse("br_med_app:list-currency-rates-list")
        CurrencyRate.objects.create(
            date="2023-01-09",
            base_currency="USD",
            target_currency="EUR",
            exchange_rate=1.2,
        )
        CurrencyRate.objects.create(
            date="2023-01-10",
            base_currency="USD",
            target_currency="EUR",
            exchange_rate=1.3,
        )

    def test_currency_rates_endpoint(self):
        start_date = "2023-01-09"
        end_date = "2023-01-13"
        target_currency = "BRL"
        response = self.client.get(
            self.url,
            {
                "start_date": start_date,
                "end_date": end_date,
                "target_currency": target_currency,
            },
        )

        response_data = response.json()
        self.assertEqual(len(response_data), 5)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertIn("date", response_data[0])
        self.assertIn("base_currency", response_data[0])
        self.assertIn("target_currency", response_data[0])
        self.assertIn("exchange_rate", response_data[0])

    def test_error_message(self):
        response = self.client.get(
            self.url,
            {
                "start_date": "2023-01-09",
                "end_date": "2023-01-14",
                "target_currency": "EUR",
            },
        )
        response_data = response.json()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response_data["message"], "Date range exceeds the limit of 5 days"
        )

    def test_list_currency_rates(self):
        response = self.client.get(self.list_url)
        serialized_data = CurrencyRateSerializer(
            CurrencyRate.objects.all(), many=True
        ).data
        self.assertEqual(len(response.data), 4)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["results"], serialized_data)
