from django.db.models import DateTimeField
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from . import models
from .helper_function.weathers import get_temperature
from .models import City, CityWeathers
from .helper_function import weathers
from django.urls import reverse
from .forms import NameForm, CityForm


def index(request):
    cities = City.objects.all()
    context = {'cities':cities}
    return render(request=request, template_name= "weathers/cities.html", context= context)

def detail(request, pk):
    # city = get_object_or_404(City,pk=pk) > this not necessary now after try except
    city = None
    try:
        city = City.objects.get(id=pk)
    except City.DoesNotExist:
        pass

    current_temperature = get_temperature(city.coordination_x, city.coordination_y)
    # value = str(pk) * 5
    context = {
        'city':city,
        # 'value':value,
        'cities':City.objects.all(),
        'temperature': current_temperature,
    }

    city_weathers = CityWeathers.objects.create(city=city, temperature=current_temperature)
    city_weathers.save()

    return render(request=request, template_name= "weathers/city.html", context= context)

def weathers_view(request):
    city_weathers = CityWeathers.objects.all().order_by('-time_stamp')
    context = {'city_weathers':city_weathers}
    return render(request = request, template_name = 'weathers/weathers.html', context = context)
"""
def add_city(request):
    if request.method == 'POST':
        city = City.objects.create(
            name = request.POST['city'],
            country = request.POST['country'],
            coordination_x = request.POST['coordination_x'],
            coordination_y = request.POST['coordination_y']
        )
        city.save()
        return HttpResponseRedirect(reverse('weathers:cities'))
    context = {}
    return render(request = request, template_name = 'weathers/city_add.html', context = context)
"""
def delete_city(request, pk):
    city = City.objects.get(id=pk)
    if request.method == 'POST':
        city.delete()
        return HttpResponseRedirect(reverse('weathers:cities'))
    context = {'city':city}
    return render(request=request, template_name='weathers/city_confirm_delete.html', context=context)
"""
def add_city(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            city = City.objects.create(
                name=form.cleaned_data['city'],
                country=form.cleaned_data['country'],
                coordination_x=form.cleaned_data['coordination_x'],
                coordination_y=form.cleaned_data['coordination_y']
            )
            city.save()
            return HttpResponseRedirect(reverse('weathers:cities'))

    else:
        form = NameForm()
    context = {'form':form}
    return render(request=request, template_name='weathers/city_add_1.html', context=context)
"""

def add_city(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            # author = Author(title="Mr")
            # form = PartialAuthorForm(request.POST, instance=author)
            # form.save()
            # city = City()
            form.save()
            # city.save()
            return HttpResponseRedirect(reverse('weathers:cities'))

    else:
        form = CityForm()
    context = {'form':form}
    return render(request=request, template_name='weathers/city_add_1.html', context=context)
