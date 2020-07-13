import requests
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import render
from .models import City
from .forms import CityForm

def index(request):
    appid = '04df3bd974e178dfde66e1f7428c5a7b'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    d = City.objects.all()
    d.delete()

    if(request.method == 'POST'):
            form = CityForm(request.POST)
            form.save()

    form = CityForm()


    cities = City.objects.all()

    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        if res.get("main"):
            city_info = {
                'city': city.name,
                'temp': res["main"]["temp"],
                'icon': res["weather"][0]["icon"],
                'speed': res["wind"]["speed"],
                'humidity': res["main"]["humidity"],
                'error': False,
            }
        else:
            return render(request, 'weather/error.html')

        all_cities.append(city_info)

    context = {'all_info': all_cities, 'form':form}

    return render(request, 'weather/index.html', context)
