from django.urls import path, include
from rest_framework import routers
from .api.viewsets import CurrencyRateAPIView, CurrencyRateViewSet

app_name = "br_med_app"

router = routers.DefaultRouter()

router.register(
    r"list-currency-rates", CurrencyRateViewSet, basename="list-currency-rates"
)

urlpatterns = [
    path("", include(router.urls)),
    path("currency-rates/", CurrencyRateAPIView.as_view(), name="currency-rates"),
]
