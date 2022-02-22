from django.shortcuts import render
from .forms import *
from .models import Event

def index(request):
    return render(request, 'core/index.html')

def event(request, event_id):

    event = Event.objects.get(id=event_id)
    event_title = event.title
   # event_image = event.image
    event_location = event.location
    event_date = event.date
   # event_time = event.time
    event_desc = event.desc
    event_ticket = event.ticket
   # event_social = event.social
   # event_tag = event.tag

    context = {'event_title': event_title, 'event_desc': event_desc, 'event_ticket': event_ticket}

    return render(request, 'core/event.html', context)

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