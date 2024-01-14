from rest_framework import status
from rest_framework.test import APITestCase


class CurrencyRatesAPITest(APITestCase):
    def setUp(self):
        self.url = '/api/currency-rates/' 

    def test_currency_rates_endpoint(self):
        start_date = '2023-01-09'
        end_date = '2023-01-13'
        target_currency = 'BRL'
        # Make the API request
        response = self.client.get(self.url, {
            'start_date': start_date,
            'end_date': end_date,
            'target_currency': target_currency
        })

        response_data = response.json()
        self.assertEqual(len(response_data), 5)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertIn('date', response_data[0])
        self.assertIn('base_currency', response_data[0])
        self.assertIn('target_currency', response_data[0])
        self.assertIn('exchange_rate', response_data[0])

    def test_error_message(self):
        response = self.client.get(self.url, {
            'start_date': '2023-01-09',
            'end_date': '2023-01-14',
            'target_currency': 'EUR'
        })
        response_data = response.json()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response_data['message'], 'Date range exceeds the limit of 5 days')