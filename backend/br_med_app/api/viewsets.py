from rest_framework import viewsets
from .serializers import CurrencyRateSerializer
from br_med_app.models import CurrencyRate

class CurrencyRateViewSet(viewsets.ModelViewSet):
    queryset = CurrencyRate.objects.all()
    serializer_class = CurrencyRateSerializer