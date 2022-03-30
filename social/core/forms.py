from django import forms
from .models import Event, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


#create forms here

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'image', 'datetime', 'street', 'area', 'city',
                  'desc', 'ticket', 'facebook', 'instagram', 'discord']
        widgets = {'title': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Title'}),
                   'datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
                   'street': forms.TextInput(attrs={'placeholder': 'Address'}),
                   'area': forms.TextInput(attrs={'placeholder': 'Area'}),
                   'city': forms.TextInput(attrs={'placeholder': 'City'}),
                   'desc': forms.Textarea(attrs={'placeholder': 'Description'}),
                   'ticket': forms.URLInput(attrs={'placeholder': 'Ticket Link'}),
                   'facebook': forms.URLInput(attrs={'placeholder': 'Facebook Link'}),
                   'instagram': forms.URLInput(attrs={'placeholder': 'Instagram Link'}),
                   'discord': forms.URLInput(attrs={'placeholder': 'Discord Link'}),}

class CreateUserForm(UserCreationForm):
    email = forms.EmailField()
<<<<<<< HEAD

    def clean_email(self):
        data = self.cleaned_data['email']
        if "@manchester.ac.uk" not in data:  # any check you need
            raise forms.ValidationError("Must be a manchester email address")
        return data

=======
    
    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
    
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
            
>>>>>>> master
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
