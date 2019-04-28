import time
import requests
from django.shortcuts import render


def index(request):
    API_ID = 'b4ade3e9f47c260f170c8ee12da73bb0'  # ключ с сайта https://openweathermap.org
    city = 'Чита'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={},ru&units=metric&APPID=' + API_ID

    try:

        res = requests.get(url.format(city)).json()# запрос на сервер получение JSON файла
        # выделяем необходимую информацию из url
        city_info = {
            'city': city, #название города
            'dt': time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime(res["dt"])),  # дата и время
            'temp': res["main"]["temp"], #температура
            'icon': res["weather"][0]["icon"],#код иконки погоды
            'description': res['weather'][0]['description']# состояние погоды
             }
        print("city :", city_info)
    except Exception as e:
         print("Exception (find):", e)

    # контекст для передачи в шаблон
    context = {'info': city_info}
    # #print(res.text)

    return render(request, 'weather/index.html', context)
