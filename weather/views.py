import time
#import pytz
import requests
from django.conf import settings
from django.shortcuts import render
from datetime import datetime
from django.utils.timezone import pytz, now
from weather.forms import CityForm
from weather.models import City


def index(request):
    API_ID = 'b4ade3e9f47c260f170c8ee12da73bb0'  # ключ с сайта https://openweathermap.org
    url = 'https://api.openweathermap.org/data/2.5/weather?q={},ru&units=metric&lang=ru&APPID=' + API_ID

    if(request.method == 'POST'):
        form = CityForm(request.POST)#данные от пользователя
        form.save()#сохранить данные в БД

    form = CityForm()# очистка формы

    cityes = City.objects.all()#выбираем все объекты из базы
    all_cityes = []

    for city in cityes:

        try:
            res = requests.get(url.format(city.name_en)).json()# запрос на сервер получение JSON файла
            # выделяем необходимую информацию из url
            city_info = {
                'city': city.name, #название города
                'dt': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(res["dt"])),  # дата и время
                'temp': res["main"]["temp"], #температура
                'icon': res["weather"][0]["icon"],#код иконки погоды
                'description': res['weather'][0]['description']# состояние погоды
                 }
            print("city :", city_info)
        except Exception as e:
             print("Exception (find):", e)

        all_cityes.append(city_info)
        #print(all_cityes[0])

    # контекст для передачи в шаблон
    context = {'all_info': all_cityes, 'form': form}
    # #print(res.text)

    return render(request, 'weather/index.html', context)
