from django.urls import path, include
from .views import get_data
from .api.viewsets import CurrencyRateViewSet
from rest_framework import routers

app_name = "br_med_app"

router = routers.DefaultRouter()

# Register the CurrencyRateViewSet for the currency rates API
router.register(r"currency-rates", CurrencyRateViewSet, basename="currency-rates")

urlpatterns = [
    path("", include(router.urls)),
]