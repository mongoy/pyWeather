from weather.models import City
from django.forms import ModelForm, TextInput


class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        #заменяем строку шаблона < input type = "text" id = "city" class ="form-control" name="city" placeholder="Введите город" >
        widgets = {'name': TextInput(attrs={
            'class': 'form-control',
            'name': 'city',
            'id': 'city',
            'placeholder': 'Введите город'
        })}

