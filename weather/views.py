import requests
from django.shortcuts import render


API_key = 'b4ade3e9f47c260f170c8ee12da73bb0' # ключ с сайта https://openweathermap.org

def index(request):
    url = 'https://api.openweathermap.org/data/2.5/forecast?q={},RU&unit=metric&appid=' + API_key
    city = 'Chita'
    res = requests.get(url.format(city)).json()
    #выделяем необходимую информацию из url
    city_info = {
        'city': city,
        #'temp': str(res["main"]["temp"]),
        #'info': res['weather']['icon']
    }

    context = {'info': city_info}
    #print(res.text)
    return render(request, 'weather/index.html', context)
