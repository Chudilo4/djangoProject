from django import forms
from .models import *


class AddEvent(forms.ModelForm):
    class Meta:
        model = Events
        fields = ['name', 'data_begin', 'data_end', 'cat', 'list_eq2']
        widgets = {
            'data_begin': forms.DateInput(attrs={'type': 'datetime-local'}),
            'data_end': forms.DateInput(attrs={'type': 'datetime-local'}),
            }

