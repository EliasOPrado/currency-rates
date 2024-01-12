from django.shortcuts import render, HttpResponse

# Create your views here.
import requests


def fetch_currency_rates():
    url = "https://api.vatcomply.com/rates"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None


def get_data(request):
    return render(request, "base.html")
