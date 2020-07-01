import requests
from django.shortcuts import render

def index(request):
    appid = '04df3bd974e178dfde66e1f7428c5a7b'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=' + appid

    city = 'London'
    res = requests.get(url.format(city))
    print(res.text)

    return render(request, 'weather/index.html')
