import requests
from pprint import pprint
from datetime import datetime

def Forecast(API, city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric&lang=ru"
    responce = requests.get(url)
    if responce.status_code == 200:
        try:
            data = responce.json()
            city_name = data['name']
            city_description = data['weather'][0]['description']
            city_temp = data['main']['temp']
            city_feels_like = data['main']['feels_like']
            city_humidity = data['main']['humidity']
            city_pressure = data['main']['pressure']
            city_wind = data['wind']['speed']
            city_sunrise = datetime.fromtimestamp(data['sys']['sunrise'])
            city_sunset = datetime.fromtimestamp(data['sys']['sunset'])
            city_length_of_the_day = city_sunset - city_sunrise

            return f"""Погода в городе {city_name}: {str(city_description).capitalize()}
Температура: {city_temp}°C
Ощущается: {city_feels_like}°C
Влажность: {city_humidity}%
Давление воздуха: {city_pressure}ГПа
Ветер: {city_wind}м/с
Восход: {city_sunrise}
Продолжительность дня: {city_length_of_the_day}
Закат: {city_sunset}"""

        except Exception:
            return "Такого города нет!"
    else:
        return "Что-то пошло не так, попробуйте позже!"