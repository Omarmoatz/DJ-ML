from django import forms

from .models import Iris

class IrisForm(forms.ModelForm):
    class Meta:
        model = Iris
        exclude = ['species']