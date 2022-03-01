from django.forms import ModelForm
from .models import Event
from django import forms

#create forms here

class LoginForm(forms.Form):

    email = forms.CharField(label = 'E-Mail',required=True)
    password = forms.CharField(label = 'Password',required=True)


class SignupForm(forms.Form):
    name = forms.CharField(label='Name', required=True)
    email = forms.CharField(label = 'E-Mail',required=True)
    password = forms.CharField(label = 'Password',required=True)
    confirm = forms.CharField(label='Confirm Password', required=True)

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'image', 'datetime', 'street', 'area', 'city',
                  'desc', 'ticket', 'facebook', 'instagram', 'discord']