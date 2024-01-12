from rest_framework import status
from django.urls import reverse

from django.core.management import call_command
from io import StringIO

from rest_framework.test import APITestCase

from br_med_app.models import CurrencyRate


class TestAPI(APITestCase):
    """
    Test API endpoints and requests.
    """

    def setUp(self):
        pass
