import requests
from datetime import datetime

def get_temperature(latitude: float, longitude: float) -> float:
    new_url = f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m'
    data = requests.get(url=new_url)
    json_data = data.json()
    city_temp = json_data['current']['temperature_2m']
    return city_temp

def get_wind(latitude: float, longitude: float) -> float:
    new_url = f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m'
    data = requests.get(url=new_url)
    json_data = data.json()
    city_wind = json_data['current']['wind_speed_10m']
    return city_wind

def get_humidity(latitude: float, longitude: float) -> str:
    new_url = f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m'
    data = requests.get(url=new_url)
    json_data = data.json()
    city_humidity = json_data['hourly']['relative_humidity_2m'][0]
    return city_humidity

def get_hourly_forecast(latitude: float, longitude: float) -> list:
    new_url = f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m'
    data = requests.get(url=new_url)
    json_data = data.json()
    city_hourly_data = json_data.get("hourly", {})
    current_time = datetime.now().strftime("%Y-%m-%dT%H:00")
    current_time_index = city_hourly_data['time'].index(current_time)
    city_hourly_forecast = [
        {
            'time': city_hourly_data['time'][i][11:16],
            'temperature': city_hourly_data['temperature_2m'][i],
            'humidity': city_hourly_data['relative_humidity_2m'][i],
            'wind_speed': city_hourly_data['wind_speed_10m'][i],
        }
        for i in range(current_time_index, min(current_time_index+8,len(city_hourly_data['time'])))
    ]
    return city_hourly_forecast







# url =  "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
#
# new_url = f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m'

# data = requests.get(url = new_url)
#
# json_data = data.json()
#
# print(json_data)
# print(json_data['current']['temperature_2m'])

