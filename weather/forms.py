from weather.models import City
from django.forms import ModelForm, TextInput


class City(ModelForm):
    class Meta:
        model = City
        fields = ['name']

