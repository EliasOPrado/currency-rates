from django.urls import path
from .api.viewsets import CurrencyRateAPIView

app_name = "br_med_app"

urlpatterns = [
    path("currency-rates/", CurrencyRateAPIView.as_view(), name="currency-rates"),
]
