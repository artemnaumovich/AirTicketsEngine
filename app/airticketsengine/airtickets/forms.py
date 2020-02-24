from django import forms
from .models import *
from django.core.exceptions import ValidationError

from datetime import datetime
from re import match

class AirlineForm(forms.ModelForm):

    class Meta:
        model = Airline
        fields = ['name', 'country', 'appearanceYear', 'slug']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.Select(attrs={'class': 'form-control'}),
            'appearanceYear': forms.NumberInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'})
        }

    def clean_appearanceYear(self):
        new_year = self.cleaned_data['appearanceYear']

        if new_year < 1909 or new_year > datetime.now().year:
            raise ValidationError("Year must be in range (1909, {})".format(datetime.now().year))

        return new_year


class AirportForm(forms.ModelForm):

    class Meta:
        model = Airport
        fields = ['name', 'city', 'address', 'phone', 'slug']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.Select(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'})
        }

    def clean_phone(self):
        new_phone = self.cleaned_data['phone']

        pattern = r"^\+[0-9]+$"
        res = match(pattern, new_phone)
        if res is None:
            raise ValidationError('Phone number must starts with "+" and after that consists only symbhols 0-9')

        return new_phone


class CountryForm(forms.ModelForm):

    class Meta:
        model = Country
        fields = ['name', 'slug']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'})
        }


class CityForm(forms.ModelForm):

    class Meta:
        model = City
        fields = ['name', 'country', 'slug']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.Select(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'})
        }



class RouteForm(forms.ModelForm):

    class Meta:
        model = Route
        fields = ['name', 'airportFrom', 'airportTo', 'slug']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'airportFrom': forms.Select(attrs={'class': 'form-control'}),
            'airportTo': forms.Select(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'})
        }


class FlightForm(forms.ModelForm):

    class Meta:
        model = Flight
        fields = ['name', 'airplane', 'route', 'departureDateTime', 'price', 'duration', 'slug']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'airplane': forms.Select(attrs={'class': 'form-control'}),
            'route': forms.Select(attrs={'class': 'form-control'}),
            'departureDateTime': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'duration': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'})
        }

class AirplaneForm(forms.ModelForm):

    class Meta:
        model = Airplane
        fields = ['name', 'airline', 'capacity', 'numberRows', 'slug']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'airline': forms.Select(attrs={'class': 'form-control'}),
            'capacity': forms.NumberInput(attrs={'class': 'form-control'}),
            'numberRows': forms.NumberInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'})
        }
