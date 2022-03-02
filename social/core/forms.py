from django import forms
from .models import Event

#create forms here

class LoginForm(forms.Form):

    email = forms.CharField(label = 'E-Mail',required=True)
    password = forms.CharField(label = 'Password',required=True)


class SignupForm(forms.Form):
    name = forms.CharField(label='Name', required=True)
    email = forms.CharField(label = 'E-Mail',required=True)
    password = forms.CharField(label = 'Password',required=True)
    confirm = forms.CharField(label='Confirm Password', required=True)

class DateInput(forms.DateInput):
    input_type = 'datetime'
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'image', 'datetime', 'street', 'area', 'city',
                  'desc', 'ticket', 'facebook', 'instagram', 'discord']
        widgets = {'title': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Title'}),
                #    'image': forms.ImageField(),
                   'datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
                   'street': forms.TextInput(attrs={'placeholder': 'Address'}),
                   'area': forms.TextInput(attrs={'placeholder': 'Area'}),
                   'city': forms.TextInput(attrs={'placeholder': 'City'}),
                   'desc': forms.Textarea(attrs={'placeholder': 'Description'}),
                   'ticket': forms.URLInput(attrs={'placeholder': 'Ticket Link'}),
                   'facebook': forms.URLInput(attrs={'placeholder': 'Facebook Link'}),
                   'instagram': forms.URLInput(attrs={'placeholder': 'Instagram Link'}),
                   'discord': forms.URLInput(attrs={'placeholder': 'Discord Link'}),}



