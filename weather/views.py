import requests
from django.shortcuts import render


def index(request):
    API_ID = 'b4ade3e9f47c260f170c8ee12da73bb0'  # ключ с сайта https://openweathermap.org
    city = 'Chita'
    city_id = 0
    url = 'https://api.openweathermap.org/data/2.5/forecast?q={},RU&unit=metric&appid='

    try:
        res = requests.get(url, params={'q': city, 'type': 'like', 'APPID': API_ID}) # запрос на сервер
        data = res.json() # получение JSON файла
        print(data)
        city_info = ["{}  ({})".format(d["name"], d["sys"]["country"]) for d in data["list"]] #получение информации и SON файла
        print("city :", city_info)
    except Exception as e:
        print("Exception (find):", e)

    # url = 'https://api.openweathermap.org/data/2.5/forecast?q={},RU&unit=metric&appid=' + API_key
    #
    # res = requests.get(url.format(city)).json()
    # #выделяем необходимую информацию из url
    # city_info = {
    #     'city': city,
    #     #'temp': str(res["main"]["temp"]),
    #     #'info': res['weather']['icon']
    # }
    #
    # context = {'info': city_info}
    # #print(res.text)

    return render(request, 'weather/index.html')
