from rest_framework import serializers
from br_med_app.models import CurrencyRate


class CurrencyRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyRate
        fields = ("date", "base_currency", "target_currency", "exchange_rate")
