from django.db import models


# Create your models here.
class CurrencyRate(models.Model):
    date = models.DateField()
    base_currency = models.CharField(max_length=3, default="USD")
    target_currency = models.CharField(max_length=3)
    exchange_rate = models.DecimalField(max_digits=10, decimal_places=6)

    def __str__(self):
        return f"{self.date} - {self.base_currency}/{self.target_currency}: {self.exchange_rate}"
