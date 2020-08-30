from django import forms
from .models import schedule
from django.contrib.auth.models import User

class DateInput(forms.DateInput):
    input_type = 'date'

class postSchedule(forms.ModelForm):
    class Meta:
        model = schedule
        fields = ['startDate','lastDate','title','content','categoryNum']
        widgets = {
            'startDate': DateInput(attrs={'type': 'date'}),
            'lastDate': DateInput(attrs={'type': 'date'}),
        }

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
