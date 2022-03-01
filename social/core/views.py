from django.shortcuts import render
from .forms import *
from .models import Event

def index(request):
    return render(request, 'core/index.html')

def event(request, event_id):

    event = Event.objects.get(id=event_id)
    
    context = {'event_title': event.title, 
               'event_image': event.image.url,
               'event_datetime': event.datetime,
               'event_street': event.street,
               'event_area': event.area,
               'event_city': event.city,
               'event_desc': event.desc,
               'event_ticket': event.ticket,
               'event_facebook': event.facebook,
               'event_instagram': event.instagram,
               'event_discord': event.discord,
               'event_attendance': event.attendance}

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