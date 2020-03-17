from django.forms import ModelForm
from django.contrib.auth import forms
from .models import Items


class QuantityForm(ModelForm):
    class Meta:
        model = Items
        fields = ['qty']
