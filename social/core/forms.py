from django import forms
from django.db import models
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile




#create forms here
#
# class LoginForm(forms.Form):
#
#     email = forms.CharField(label = 'E-Mail',required=True)
#     password = forms.CharField(label = 'Password',required=True)

#
# class SignupForm(forms.Form):
#     name = forms.CharField(label='Name', required=True)
#     email = forms.CharField(label = 'E-Mail',required=True)
#     password = forms.CharField(label = 'Password',required=True)
#     confirm = forms.CharField(label='Confirm Password', required=True)
#
#
# class CreateForm(forms.Form):
#     title = forms.CharField(label='Title', required=True)
#     image = forms.ImageField(label='Image', required=True)
#     location = forms.CharField(label = 'Location',required=False)
#     time = forms.CharField(label = 'Time',required=False)
#     tickets = forms.CharField(label='Tickets', required=False)
#     socials = forms.CharField(label='Socials', required=False)
#     tags = forms.CharField(label='Tags', required=False)
#     desc = forms.CharField(label='Description', required=False, widget=forms.Textarea)

class CreateUserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# To update username and email
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(label="e-mail")

    class Meta:
        model = User
        fields = ['username', 'email']

# to upload profile picture
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['img']