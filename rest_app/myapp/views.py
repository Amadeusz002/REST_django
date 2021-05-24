from django.shortcuts import render
from .models import Pvgis
from .forms import pvgisForm
from rest_framework.request import Request
import requests
import statistics


def truncate(f, n):
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return '.'.join([i, (d + '0' * n)[:n]])


def index(request: Request):
    url_current = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=09b52539c46bfaeac6577c3c6f70eb29'
    url_forecast = 'https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=current,minutely,hourly,alerts&units=metric&appid=09b52539c46bfaeac6577c3c6f70eb29'

    url_pvgis = 'https://re.jrc.ec.europa.eu/api/seriescalc?lat={}&lon={}&startyear={}&endyear={}&aspect={}&angle={}&pvcalculation=1&pvtechchoice={}&peakpower={}&loss={}&outputformat=json'

    if request.method == 'POST':
        form2 = pvgisForm(request.POST)
        form2.save()

    form2 = pvgisForm()
    pvg1 = Pvgis.objects.all()

    data = []

    for pvg in pvg1:
        current = requests.get(url_current.format(pvg.city)).json()

        lat = current['coord']['lat']
        lon = current['coord']['lon']
        forecast = requests.get(url_forecast.format(lat, lon)).json()
        temp = {'day': [],
                'morn': [],
                'eve': []}
        for i in forecast['daily']:
            temp['day'].append(i['temp']['day'])
            temp['morn'].append(i['temp']['morn'])
            temp['eve'].append(i['temp']['eve'])

        mean_day = statistics.mean(temp['day'])
        mean_morn = statistics.mean(temp['morn'])
        mean_eve = statistics.mean(temp['eve'])
        mean_day = truncate(mean_day, 2)
        mean_morn = truncate(mean_morn, 2)
        mean_eve = truncate(mean_eve, 2)
        pvgis = requests.get(url_pvgis.format(pvg.lat, pvg.lon, pvg.start_year, pvg.end_year, pvg.azimuth, pvg.slope,
                                              pvg.technology, pvg.peakPower, pvg.loss)).json()

        mean_pvgis = {
            'irridiance': [],
            'power': [],
            'wind': [],

        }
        for pv in pvgis['outputs']['hourly']:
            mean_pvgis['irridiance'].append(pv['G(i)'])
            mean_pvgis['power'].append(pv['P'])
            mean_pvgis['wind'].append(pv['WS10m'])

        pvgis_irr = truncate(statistics.mean(mean_pvgis['irridiance']), 2)
        pvgis_pow = truncate(statistics.mean(mean_pvgis['power']), 2)
        pvgis_wind = truncate(statistics.mean(mean_pvgis['wind']), 2)

        dict = {
            'city': pvg.city,
            'temperature': current['main']['temp'],
            'description': current['weather'][0]['description'],
            'icon': current['weather'][0]['icon'],
            'mean_day': mean_day,
            'mean_morn': mean_morn,
            'mean_eve': mean_eve,
            'mean_irr': pvgis_irr,
            'mean_pow': pvgis_pow,
            'mean_wind': pvgis_wind,
            'start_year': pvg.start_year,
            'end_year': pvg.end_year
        }

        data.append(dict)

    context = {'data': data, 'form': form2}
    return render(request, 'myapp/dashboard.html', context)
