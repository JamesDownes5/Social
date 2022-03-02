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


class CreateForm(forms.Form):
    title = forms.CharField(label='Title', required=True)
    image = forms.ImageField(label='Image', required=True)
    location = forms.CharField(label = 'Location',required=False)
    time = forms.CharField(label = 'Time',required=False)
    tickets = forms.CharField(label='Tickets', required=False)
    socials = forms.CharField(label='Socials', required=False)
    tags = forms.CharField(label='Tags', required=False)
    desc = forms.CharField(label='Description', required=False, widget=forms.Textarea)
