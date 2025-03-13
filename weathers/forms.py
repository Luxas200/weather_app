from django import forms
from .models import City
from django.forms import ModelForm, Textarea

class NameForm(forms.Form):
    city = forms.CharField(label='city', max_length=50, min_length=3)
    country = forms.CharField(label='country', max_length=50, min_length=3)
    coordination_x = forms.FloatField(label='coordination_x', max_value=120, min_value=0)
    coordination_y = forms.FloatField(label='coordination_y', max_value=120, min_value=0)

class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ('name', 'country', 'coordination_x', 'coordination_y')
