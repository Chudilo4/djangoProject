from django import forms
from .models import *


class AddEvent(forms.ModelForm):
    class Meta:
        model = Events
        fields = ['name', 'data_begin', 'data_end', 'cat']
        widgets = {
            'data_begin': forms.DateInput(attrs={'type': 'datetime-local'}),
            'data_end': forms.DateInput(attrs={'type': 'datetime-local'}),
        }


BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
FAVORITE_COLORS_CHOICES = [(e.pk, e.name) for e in Equipments.objects.all()]


class SimpleForm(forms.Form):
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    favorite_colors = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=FAVORITE_COLORS_CHOICES,
    )
