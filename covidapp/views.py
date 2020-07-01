from django.shortcuts import render
import requests
import json


# Create your views here.


def index(request):
    total_count = requests.get('https://api.kawalcorona.com/')
    countrywise_count = total_count.json()
    india_response = requests.get('http://covid-19india-api.herokuapp.com/all')
    # transfor the response to json objects
    india_count = india_response.json()
    return render(request, 'index.html', {'countrywise_count': countrywise_count, 'india_count': india_count})
