from django.shortcuts import render

from weathers.helper_function.weathers import get_temperature, get_wind, get_humidity
from weathers.models import City

def home(request):
    try:
        favorite_city = City.objects.get(name='Vilnius')
        temperature = get_temperature(favorite_city.coordination_x, favorite_city.coordination_y)
        wind = get_wind(favorite_city.coordination_x, favorite_city.coordination_y)
        humidity = get_humidity(favorite_city.coordination_x, favorite_city.coordination_y)

    except City.DoesNotExist:
        favorite_city = None
        temperature = None
        wind = None
        humidity = None

    context = {
        'favorite_city': favorite_city,
        'temperature': temperature,
        'wind': wind,
        'humidity': humidity,
    }
    return render(request=request, template_name="home.html", context=context)
