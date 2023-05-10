from django.shortcuts import render
import requests

from apps.weather.models import City
from apps.weather.forms import CityForm

# Create your views here.
def index(req):

    if(req.method == 'POST'):
        form = CityForm(req.POST)
        form.save()
        
    form = CityForm()

    apiKey = '353e8e3a4f46a538bb1b2075c0d7d5ff'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + apiKey

    cities = City.objects.all()

    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city':city.name,
            'temp':res['main']['temp'],
            'icon':res['weather'][0]['icon']
        }

        all_cities.append(city_info)

    context = {
        'all_info':all_cities,
        'form':form,
    }

    return render(req, 'index.html', context)