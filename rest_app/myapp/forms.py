from django.forms import ModelForm, TextInput
from .models import City, Pvgis


class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        # widgets = {'name': TextInput(attrs={'class': 'input', 'placeholder': 'City Name'})}


class pvgisForm(ModelForm):
    class Meta:
        model = Pvgis
        fields = ['city', 'start_year', 'end_year', 'lon', 'lat', 'slope', 'azimuth', 'technology', 'peakPower', 'loss']
        widgets = {'city': TextInput(attrs={'class': 'input', 'placeholder': 'City Name'}),
                   'start_year': TextInput(attrs={'class': 'input', 'placeholder': 'Start year'}),
                   'end_year': TextInput(attrs={'class': 'input', 'placeholder': 'End year'}),
                   'lon': TextInput(attrs={'class': 'input', 'placeholder': 'Longitude'}),
                   'lat': TextInput(attrs={'class': 'input', 'placeholder': 'Latitude'}),
                   'slope': TextInput(attrs={'class': 'input', 'placeholder': 'Slope'}),
                   'azimuth': TextInput(attrs={'class': 'input', 'placeholder': 'Azimuth'}),
                   'technology': TextInput(attrs={'class': 'input', 'placeholder': 'Technology'}),
                   'peakPower': TextInput(attrs={'class': 'input', 'placeholder': 'Peak power'}),
                   'loss': TextInput(attrs={'class': 'input', 'placeholder': 'Power loss'}),
                   }
