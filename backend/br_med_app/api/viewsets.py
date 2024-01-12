from rest_framework import viewsets
from .serializers import CurrencyRateSerializer
from br_med_app.models import CurrencyRate


class CurrencyRateViewSet(viewsets.ModelViewSet):
    queryset = CurrencyRate.objects.all()
    serializer_class = CurrencyRateSerializer

    def get_queryset(self):
        # Get start and end dates from query parameters
        # /api/currency-rates/?start_date=YYYY-MM-DD&end_date=YYYY-MM-DD
        start_date = self.request.query_params.get("start_date")
        end_date = self.request.query_params.get("end_date")
        target_currency = self.request.query_params.get("target_currency")

        if start_date and end_date and target_currency:
            queryset = CurrencyRate.objects.filter(
                date__range=[start_date, end_date], 
                target_currency=target_currency
            )
            return queryset
        else:
            return self.queryset
