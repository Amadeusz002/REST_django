from django.shortcuts import render
import rest_framework
from django.shortcuts import render
from .models import City, Pvgis
from .forms import CityForm, pvgisForm
from rest_framework.request import Request
from .serializers import CitySerializer
from rest_framework.response import Response
import requests
import asyncio


# Create your views here.

def index(request: Request):
    asyncio.set_event_loop(asyncio.new_event_loop())
    loop = asyncio.get_event_loop()

    serializer_class = CitySerializer

    url_current = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=09b52539c46bfaeac6577c3c6f70eb29'
    url_forecast = 'https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=current,minutely,hourly,alerts&appid=09b52539c46bfaeac6577c3c6f70eb29'

    pvgis = 'https://re.jrc.ec.europa.eu/api/seriescalc?lat={}&lon={}&startyear={}&endyear={}&aspect={}&angle={}pvcalculation=1&pvtechchoice={}&peakpower={}&loss={}'

    if request.method == 'POST':
        form2 = pvgisForm(request.POST)
        form2.save()

    form2 = pvgisForm()
    pvg1 = Pvgis.objects.all()

    weather_data = []

    for pvg in pvg1:
        url_current = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=09b52539c46bfaeac6577c3c6f70eb29'
        current = requests.get(url_current.format(pvg)).json()
        print(current)
        lat = current['coord']['lat']
        lon = current['coord']['lon']
        forecast = requests.get(url_forecast.format(lat, lon)).json()
        city_weather = {
            'city': pvg.name,
            'temperature': current['main']['temp'],
            'description': current['weather'][0]['description'],
            'icon': current['weather'][0]['icon'],
        }

        weather_data.append(city_weather)

    context = {'weather_data': weather_data, 'form': form2}
    return render(request, 'myapp/dashboard.html', context)
