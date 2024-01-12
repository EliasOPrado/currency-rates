from django.core.management.base import BaseCommand
from br_med_app.models import CurrencyRate
import requests
from datetime import datetime, timedelta


class Command(BaseCommand):
    help = "Popula o banco de dados com dados de taxa de câmbio para o último ano"

    def handle(self, *args, **kwargs):
        base_currency = "USD"
        target_currencies = ["BRL", "EUR", "JPY"]

        # Cria um intervalo de datas para o último ano
        end_date = datetime.now()
        start_date = end_date - timedelta(days=365)

        current_date = start_date

        while current_date <= end_date:
            # Verifica se os dados já existem no banco de dados
            existing_data = CurrencyRate.objects.filter(
                date=current_date, base_currency=base_currency
            )

            if not existing_data.exists():
                url = f"https://api.vatcomply.com/rates?date={current_date.strftime('%Y-%m-%d')}&base={base_currency}"

                response = requests.get(url)
                if response.status_code == 200:
                    data = response.json()

                    for target_currency in target_currencies:
                        exchange_rate = data["rates"].get(target_currency)
                        if exchange_rate is not None:
                            CurrencyRate.objects.create(
                                date=current_date,
                                base_currency=base_currency,
                                target_currency=target_currency,
                                exchange_rate=exchange_rate,
                            )

                            self.stdout.write(
                                self.style.SUCCESS(
                                    f"Successfully inserted data for {target_currency} on {current_date}"
                                )
                            )
                        else:
                            self.stdout.write(
                                self.style.WARNING(
                                    f"Data for {target_currency} not available on {current_date}"
                                )
                            )
                else:
                    self.stdout.write(
                        self.style.ERROR(
                            f"Failed to fetch data from the API for {current_date}. Status code: {response.status_code}"
                        )
                    )
            else:
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Data for {base_currency} on {current_date} already exists in the database"
                    )
                )

            current_date += timedelta(days=1)
