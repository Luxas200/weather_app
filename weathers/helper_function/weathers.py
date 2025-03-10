import requests

def get_temperature(latitude: float, longitude: float) -> float:
    new_url = f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m'
    data = requests.get(url=new_url)
    json_data = data.json()
    city_temp = json_data['current']['temperature_2m']
    return city_temp



# url =  "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
#
# new_url = f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m'

# data = requests.get(url = new_url)
#
# json_data = data.json()
#
# print(json_data)
# print(json_data['current']['temperature_2m'])

