from django.shortcuts import render

def index(request):
    return render(request, 'core/index.html')

def event(request):
    return render(request, 'core/event.html')

def create(request):
    return render(request, 'core/create.html')

def signup(request):
    return render(request, 'core/signup.html')

def login(request):
    return render(request, 'core/login.html')

def account(request):
    return render(request, 'core/account.html')