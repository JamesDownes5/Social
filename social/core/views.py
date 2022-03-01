from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'core/index.html')

def event(request):
    return render(request, 'core/event.html')

def login(request):
    return render(request, 'core/login.html')

def create(request):
    return render(request, 'core/create.html')
#
# def create(request):
#     if request.method == 'POST':
#         form = CreateForm(request.POST)
#         if form.is_valid():
#             title = form.cleaned_data['title']
#             image = form.cleaned_data['image']
#             location = form.cleaned_data['location']
#             time = form.cleaned_data['time']
#             tickets = form.cleaned_data['tickets']
#             socials = form.cleaned_data['socials']
#             tags = form.cleaned_data['tags']
#             desc = form.cleaned_data['desc']
#     form = CreateForm()
#     return render(request, 'core/create.html', {'form' : form})
#
# def signup(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             confirm = form.cleaned_data['confirm']
#
#     form = SignupForm()
#     return render(request, 'core/signup.html', {'form' : form})
#
# def login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             # print(email,password)
#     form = LoginForm()
#     return render(request, 'core/login.html', {'form': form} )


def signup(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}!')
            return redirect('account')
    else:
        form = CreateUserForm()
    return render(request, 'core/signup.html', {'form':form})



@login_required()
def account(request):
    if request.method == "POST":
        update_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if update_form.is_valid() and profile_form.is_valid():
            update_form.save()
            profile_form.save()
            messages.success(request, f'Account Updated!')
            return redirect('account')
    else:
        update_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'update_form': update_form,
        'profile_form': profile_form
    }
    return render(request, 'core/account.html', context)


