from django.shortcuts import render
import requests
import json


# Create your views here.


def index(request):
    total_count = requests.get('https://api.kawalcorona.com/')
    countrywise_count = total_count.json()
    return render(request, 'index.html', {'countrywise_count': countrywise_count})
