from django import forms
from django.core.validators import RegexValidator


class InputField(forms.Form):
    number = forms.CharField(
        label='Fibonacci Number',
        validators=[RegexValidator(regex='\d$', message='Please enter a number', code='invalid_number')]
    )
