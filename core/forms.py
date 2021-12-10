from django.core import validators
from django import forms
from django.forms import fields
from .models import Person

class OwnerRegistration(forms.ModelForm):
    class Meta:
        model = Person
        fields='__all__'
        
