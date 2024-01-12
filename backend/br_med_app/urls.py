from django.urls import path, include
from .views import get_data
from .api.viewsets import CurrencyRateAPIView
from rest_framework import routers

app_name = "br_med_app"

# router = routers.DefaultRouter()

# # Register the CurrencyRateViewSet for the currency rates API
# router.register(r"currency-rates", CurrencyRateAPIView.as_view(), basename="currency-rates")

urlpatterns = [
    path('currency-rates/', CurrencyRateAPIView.as_view(), name='currency-rates'),
]
