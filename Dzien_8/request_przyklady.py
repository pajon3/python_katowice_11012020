import sys

import requests



def link_miasto(miasto):
    resp = requests.get("https://www.metaweather.com/api/location/search/?query=" + miasto)
    return str((resp.json()[0]['woeid']))

def link_lokalizacja(lokalizacja):
    resp = requests.get('https://www.metaweather.com/api/location/' + lokalizacja)
    return resp.json()['consolidated_weather']


def pogoda(miasto):
    lokalizacja = link_miasto(miasto)
    result = (link_lokalizacja(lokalizacja))


    for slow in result:
        data = slow['applicable_date']
        min_temp = slow['min_temp']
        max_temp = slow['max_temp']
        air_pressure = slow['air_pressure']
        pogoda = slow['weather_state_name']
        return (f'Dnia {data} w mieście {miasto} pogoda będzie następująca \n - Minimalna temperatura: {min_temp}\n - Maksymalna temperatura: {max_temp}\n - Ciśnienie: {air_pressure}\n - Opady: {pogoda}' )

print(pogoda('warsaw'))