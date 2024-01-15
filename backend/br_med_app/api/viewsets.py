import time
from datetime import timedelta, datetime, date
from rest_framework import status
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CurrencyRateSerializer
from br_med_app.models import CurrencyRate
from .utils import get_api_data, insert_data_into_db

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class CurrencyRateViewSet(viewsets.ModelViewSet):
    http_method_names = ["get"]
    queryset = CurrencyRate.objects.all()
    serializer_class = CurrencyRateSerializer


class CurrencyRateAPIView(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                "start_date",
                openapi.IN_QUERY,
                description="Start date",
                type=openapi.TYPE_STRING,
            ),
            openapi.Parameter(
                "end_date",
                openapi.IN_QUERY,
                description="End date",
                type=openapi.TYPE_STRING,
            ),
            openapi.Parameter(
                "target_currency",
                openapi.IN_QUERY,
                description="The currency to check the changes.",
                type=openapi.TYPE_STRING,
            ),
        ]
    )
    def get(self, request, *args, **kwargs):
        start_date = self.request.query_params.get("start_date")
        end_date = self.request.query_params.get("end_date")
        target_currency = self.request.query_params.get("target_currency")

        if start_date and end_date and target_currency:
            start_date_obj = datetime.strptime(start_date, "%Y-%m-%d").date()
            end_date_obj = datetime.strptime(end_date, "%Y-%m-%d").date()

            num_days = (end_date_obj - start_date_obj).days + 1

            if num_days > 5:
                return Response(
                    {"message": "Date range exceeds the limit of 5 days"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            for i in range(num_days):
                current_date_str = (start_date_obj + timedelta(days=i)).strftime(
                    "%Y-%m-%d"
                )

                if CurrencyRate.objects.filter(
                    date=current_date_str, target_currency=target_currency
                ).exists():
                    continue

                api_data = get_api_data(current_date_str, target_currency)
                insert_data_into_db(api_data, target_currency)

            queryset = CurrencyRate.objects.filter(
                date__range=[start_date, end_date], target_currency=target_currency
            )

            return Response(
                CurrencyRateSerializer(queryset, many=True).data,
                status=status.HTTP_200_OK,
            )

        return Response(
            {"message": "Invalid parameters"}, status=status.HTTP_400_BAD_REQUEST
        )
