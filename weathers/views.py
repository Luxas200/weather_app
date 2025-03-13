from django.shortcuts import render
from django.http import HttpResponseRedirect
from .helper_function.weathers import get_temperature, get_wind, get_humidity, get_hourly_forecast
from .models import City, CityWeathers
from django.urls import reverse
from .forms import CityForm


def index(request):
    cities = City.objects.all()
    for city in cities:
        city.temperature = get_temperature(city.coordination_x, city.coordination_y)
    context = {'cities':cities}
    return render(request=request, template_name= "weathers/cities.html", context= context)

def detail(request, pk):
    city = None
    try:
        city = City.objects.get(id=pk)
    except City.DoesNotExist:
        pass

    current_temperature = get_temperature(city.coordination_x, city.coordination_y)
    current_wind = get_wind(city.coordination_x, city.coordination_y)
    current_humidity = get_humidity(city.coordination_x, city.coordination_y)
    city_hourly_forecast = get_hourly_forecast(city.coordination_x, city.coordination_y)

    context = {
        'city':city,
        'cities':City.objects.all(),
        'temperature': current_temperature,
        'wind': current_wind,
        'humidity': current_humidity,
        'forecast': city_hourly_forecast,
    }

    city_weathers = CityWeathers.objects.create(city=city, temperature=current_temperature,
                                                wind = current_wind, humidity = current_humidity)
    city_weathers.save()

    return render(request=request, template_name= "weathers/city.html", context= context)


def weathers_view(request):
    city_weathers = CityWeathers.objects.all().order_by('-time_stamp')
    context = {'city_weathers':city_weathers}
    return render(request = request, template_name = 'weathers/weathers.html', context = context)


def delete_city(request, pk):
    city = City.objects.get(id=pk)
    if request.method == 'POST':
        city.delete()
        return HttpResponseRedirect(reverse('weathers:cities'))
    context = {'city':city}
    return render(request=request, template_name='weathers/city_confirm_delete.html', context=context)

def update_city(request, pk):
    city = City.objects.get(id = pk)
    if request.method == 'POST':
        form = CityForm(request.POST, instance = city)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('weathers:cities'))
    else:
        form = CityForm(instance = city)
    context = {'form': form}
    return render(request=request, template_name='weathers/city_add_1.html', context=context)


def add_city(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('weathers:cities'))

    else:
        form = CityForm()
    context = {'form':form}
    return render(request=request, template_name='weathers/city_add_1.html', context=context)

