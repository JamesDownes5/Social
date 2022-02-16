from django.shortcuts import render
from .forms import *

def index(request):
    return render(request, 'core/index.html')

def event(request):
    return render(request, 'core/event.html')

def create(request):
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            image = form.cleaned_data['image']
            location = form.cleaned_data['location']
            time = form.cleaned_data['time']
            tickets = form.cleaned_data['tickets']
            socials = form.cleaned_data['socials']
            tags = form.cleaned_data['tags']
            desc = form.cleaned_data['desc']
    form = CreateForm()
    return render(request, 'core/create.html', {'form' : form})

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm = form.cleaned_data['confirm']

    form = SignupForm()
    return render(request, 'core/signup.html', {'form' : form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            # print(email,password)
    form = LoginForm()
    return render(request, 'core/login.html', {'form': form} )

def account(request):
    return render(request, 'core/account.html')


'''
def LoginForm(reguest):
    return render(request, 'core/login.html')
'''