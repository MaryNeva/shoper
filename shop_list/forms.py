from django import forms
from django.forms import ModelForm
from .models import Product


class Login_form(forms.Form):
    name = forms.CharField(label='Name', min_length=2, max_length=15, error_messages={
        'min_length': 'Too few characters',
        'max_length': 'Too many characters',
        'required': 'Fill in the field'
    })
    surname = forms.CharField(label='Surname', min_length=2, max_length=15, error_messages={
        'min_length': 'Too few characters',
        'max_length': 'Too many characters',
        'required': 'Fill in the field'
    })
    nickname = forms.CharField(label='Nickname', min_length=2, max_length=15, error_messages={
        'min_length': 'Too few characters',
        'max_length': 'Too many characters',
        'required': 'Fill in the field'
    })
    email = forms.CharField(label='Email', min_length=2, max_length=40, error_messages={
        'min_length': 'Too few characters',
        'max_length': 'Too many characters',
        'required': 'Fill in the field'
    })
    password = forms.CharField(label='Password', min_length=2, max_length=40, error_messages={
        'min_length': 'Too few characters',
        'max_length': 'Too many characters',
        'required': 'Fill in the field'
    })


UNIT_CHOICES = (('kg', 'kilogram'),
                 ('gr', 'gram'),
                 ('l', 'litre'),
                 ('ml', 'milliliter'),
                 ('pkg', 'package'),
                 ('unit', 'unit'),
     )


class Product_form(forms.Form):
    #name = forms.CharField(label='Name')
    name_unit = forms.ChoiceField(choices=UNIT_CHOICES)
    counting = forms.DecimalField(min_value=0)
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows': 5}))

